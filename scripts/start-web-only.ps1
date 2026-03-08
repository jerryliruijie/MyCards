$ErrorActionPreference = "Stop"

try {
  $webPath = (Resolve-Path "$(Join-Path $PSScriptRoot '..\apps\web')").Path

  if (-not (Get-Command npm -ErrorAction SilentlyContinue)) {
    throw "未找到命令: npm（请先安装 Node.js）"
  }

  if (-not (Test-Path (Join-Path $webPath ".env.local"))) {
    Copy-Item (Join-Path $webPath ".env.example") (Join-Path $webPath ".env.local")
  }

  Push-Location $webPath
  npm install
  Pop-Location

  Start-Process powershell -ArgumentList "-NoExit", "-Command", "Set-Location '$webPath'; npm run dev"

  Write-Host "前端已启动： http://localhost:3000" -ForegroundColor Green
}
catch {
  Write-Host "[MyCards] 前端启动失败：$($_.Exception.Message)" -ForegroundColor Red
  exit 1
}
