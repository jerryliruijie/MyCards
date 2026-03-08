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

  Ensure-Command docker
  Ensure-Command python
  Ensure-Command npm

  Write-Host "[1/4] 启动 PostgreSQL 容器" -ForegroundColor Yellow
  Push-Location "$(Join-Path $PSScriptRoot '..\infra')"
  docker compose up -d
  Pop-Location

  $apiPath = (Resolve-Path "$(Join-Path $PSScriptRoot '..\apps\api')").Path
  $webPath = (Resolve-Path "$(Join-Path $PSScriptRoot '..\apps\web')").Path

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
    & .\.venv\Scripts\python.exe -m pip install --upgrade pip
    & .\.venv\Scripts\python.exe -m pip install -e ".[dev]"
    & .\.venv\Scripts\python.exe -m alembic upgrade head
    & .\.venv\Scripts\python.exe -m app.db.seed
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
  Start-Process powershell -ArgumentList "-NoExit", "-Command", "Set-Location '$apiPath'; .\.venv\Scripts\Activate.ps1; uvicorn app.main:app --reload --port 8000"
  Start-Process powershell -ArgumentList "-NoExit", "-Command", "Set-Location '$webPath'; npm run dev"

  Write-Host "完成：" -ForegroundColor Green
  Write-Host "- 前端: http://localhost:3000"
  Write-Host "- 后端: http://localhost:8000"
  Write-Host "- 接口文档: http://localhost:8000/docs"
  Write-Host "提示：下次可用 scripts\start-dev.bat --skip-install 更快启动。"
}
catch {
  Write-Host "[MyCards] 启动失败：$($_.Exception.Message)" -ForegroundColor Red
  exit 1
}
