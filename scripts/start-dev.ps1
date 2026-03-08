param(
  [switch]$SkipInstall
)

$ErrorActionPreference = "Stop"

try {
  Write-Host "[MyCards] 开始启动开发环境..." -ForegroundColor Cyan

  function Ensure-Command($name) {
    if (-not (Get-Command $name -ErrorAction SilentlyContinue)) {
      throw "未找到命令: $name"
    }
  }

  Ensure-Command python

  $hasNpm = [bool](Get-Command npm -ErrorAction SilentlyContinue)
  if (-not $hasNpm) {
    throw "未找到命令: npm（请先安装 Node.js LTS，可运行 scripts/install-node-lts.bat）"
  }

  $hasDocker = [bool](Get-Command docker -ErrorAction SilentlyContinue)

  $apiPath = (Resolve-Path "$(Join-Path $PSScriptRoot '..\\apps\\api')").Path
  $webPath = (Resolve-Path "$(Join-Path $PSScriptRoot '..\\apps\\web')").Path

  if ($hasDocker) {
    Write-Host "[1/4] 启动 PostgreSQL 容器（Docker 模式）" -ForegroundColor Yellow
    Push-Location "$(Join-Path $PSScriptRoot '..\\infra')"
    docker compose up -d
    Pop-Location
  }
  else {
    Write-Host "[1/4] 未检测到 Docker，切换 SQLite 预览模式" -ForegroundColor Yellow
    $env:DATABASE_URL = "sqlite:///./mycards.db"
    $sqliteEnv = "DATABASE_URL=sqlite:///./mycards.db`nSTORAGE_DIR=./storage`n"
    $sqliteEnv | Set-Content -Encoding UTF8 (Join-Path $apiPath ".env")
  }

  Write-Host "[2/4] 准备后端环境" -ForegroundColor Yellow
  if (-not (Test-Path (Join-Path $apiPath ".venv"))) {
    Push-Location $apiPath
    python -m venv .venv
    Pop-Location
  }

  if (-not (Test-Path (Join-Path $apiPath ".env"))) {
    Copy-Item (Join-Path $apiPath ".env.example") (Join-Path $apiPath ".env")
  }

  if (-not $SkipInstall) {
    Push-Location $apiPath
    & .\\.venv\\Scripts\\python.exe -m pip install --upgrade pip
    & .\\.venv\\Scripts\\python.exe -m pip install -e ".[dev]"

    if ($hasDocker) {
      & .\\.venv\\Scripts\\python.exe -m alembic upgrade head
    }

    & .\\.venv\\Scripts\\python.exe -m app.db.seed
    Pop-Location
  }

  Write-Host "[3/4] 准备前端环境" -ForegroundColor Yellow
  if (-not (Test-Path (Join-Path $webPath ".env.local"))) {
    Copy-Item (Join-Path $webPath ".env.example") (Join-Path $webPath ".env.local")
  }

  if (-not $SkipInstall) {
    Push-Location $webPath
    npm install
    Pop-Location
  }

  Write-Host "[4/4] 启动后端与前端服务" -ForegroundColor Yellow
  if ($hasDocker) {
    Start-Process powershell -ArgumentList "-NoExit", "-Command", "Set-Location '$apiPath'; .\\.venv\\Scripts\\Activate.ps1; uvicorn app.main:app --reload --port 8000"
  }
  else {
    Start-Process powershell -ArgumentList "-NoExit", "-Command", "Set-Location '$apiPath'; `$env:DATABASE_URL='sqlite:///./mycards.db'; .\\.venv\\Scripts\\Activate.ps1; uvicorn app.main:app --reload --port 8000"
  }

  Start-Process powershell -ArgumentList "-NoExit", "-Command", "Set-Location '$webPath'; npm run dev"

  Write-Host "完成：" -ForegroundColor Green
  Write-Host "- 前端: http://localhost:3000"
  Write-Host "- 后端: http://localhost:8000"
  Write-Host "- 接口文档: http://localhost:8000/docs"

  if (-not $hasDocker) {
    Write-Host "提示：当前为 SQLite 预览模式。部署建议使用 PostgreSQL。" -ForegroundColor Yellow
  }

  Write-Host "提示：下次可用 scripts\\start-dev.bat --skip-install 更快启动。"
}
catch {
  Write-Host "[MyCards] 启动失败：$($_.Exception.Message)" -ForegroundColor Red
  exit 1
}
