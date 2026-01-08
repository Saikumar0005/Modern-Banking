@echo off
echo ========================================
echo   Modern Digital Banking Dashboard
echo   Docker Deployment Script
echo ========================================

echo.
echo [1/4] Stopping existing containers...
docker-compose down

echo.
echo [2/4] Building Docker images...
docker-compose build --no-cache

echo.
echo [3/4] Starting services...
docker-compose up -d

echo.
echo [4/4] Checking service status...
timeout /t 10 /nobreak > nul
docker-compose ps

echo.
echo ========================================
echo   Deployment Complete!
echo ========================================
echo   Frontend: http://localhost:4173
echo   Backend:  http://localhost:8000
echo   Database: localhost:5432
echo ========================================

echo.
echo Press any key to view logs...
pause > nul
docker-compose logs -f