@echo off
setlocal

set SCRIPT_DIR=%~dp0
set PS1=%SCRIPT_DIR%start-web-only.ps1

where powershell >nul 2>nul
if errorlevel 1 (
  echo [MyCards] ??? powershell??????
  pause
  exit /b 1
)

powershell -NoProfile -ExecutionPolicy Bypass -File "%PS1%"
if errorlevel 1 (
  echo.
  echo [MyCards] ????????????????????
  pause
  exit /b 1
)

endlocal
exit /b 0
