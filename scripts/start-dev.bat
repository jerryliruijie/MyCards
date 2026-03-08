@echo off
setlocal

set SCRIPT_DIR=%~dp0
set PS1=%SCRIPT_DIR%start-dev.ps1

if /I "%1"=="--skip-install" (
  powershell -ExecutionPolicy Bypass -File "%PS1%" -SkipInstall
) else (
  powershell -ExecutionPolicy Bypass -File "%PS1%"
)

endlocal
