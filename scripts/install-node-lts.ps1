$ErrorActionPreference = "Stop"

try {
  if (-not (Get-Command winget -ErrorAction SilentlyContinue)) {
    throw "未找到 winget。请先安装 App Installer，或手动安装 Node.js LTS。"
  }

  Write-Host "正在安装 Node.js LTS..." -ForegroundColor Yellow
  winget install OpenJS.NodeJS.LTS --accept-package-agreements --accept-source-agreements

  Write-Host "安装命令已执行。请关闭并重新打开终端后重试启动脚本。" -ForegroundColor Green
}
catch {
  Write-Host "[MyCards] Node 安装失败：$($_.Exception.Message)" -ForegroundColor Red
  exit 1
}
