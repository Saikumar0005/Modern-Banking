@echo off
echo ========================================
echo   Exposing Banking App to Internet
echo ========================================

echo.
echo Installing ngrok (if not installed)...
where ngrok >nul 2>nul
if %errorlevel% neq 0 (
    echo Please install ngrok from: https://ngrok.com/download
    echo Then run this script again
    pause
    exit /b 1
)

echo.
echo Starting public tunnels...
echo.

start "Frontend Tunnel" cmd /k "echo Frontend will be available at public URL && ngrok http 4173"
timeout /t 3 /nobreak > nul
start "Backend Tunnel" cmd /k "echo Backend API will be available at public URL && ngrok http 8000"

echo.
echo ========================================
echo   Public URLs will appear in the
echo   opened terminal windows
echo ========================================
echo.
echo Your banking app is now accessible
echo from anywhere on the internet!
echo.
pause