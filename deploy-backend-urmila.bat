@echo off
echo ========================================
echo   Modern Digital Banking Dashboard
echo   Backend Deployment Script
echo ========================================
echo.

echo [1/4] Stopping existing containers...
docker-compose down

echo.
echo [2/4] Building backend image...
docker-compose build backend

echo.
echo [3/4] Starting services...
docker-compose -f docker-compose.backend.yml up -d

echo.
echo [4/4] Checking container status...
docker-compose ps

echo.
echo ========================================
echo   Deployment Complete!
echo ========================================
echo.
echo Backend API: http://localhost:8000
echo API Docs: http://localhost:8000/docs
echo Database: localhost:5433
echo.
echo Default Login Credentials:
echo Admin: admin@bank.com / admin123
echo User: user@bank.com / user123
echo Test: test@test.com / test123
echo.
echo To view logs: docker-compose logs -f
echo To stop: docker-compose down
echo ========================================