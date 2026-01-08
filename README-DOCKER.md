# Modern Digital Banking Dashboard - Docker Deployment

## 🚀 Quick Start

### Prerequisites
- Docker Desktop installed and running
- Git (to clone the repository)

### Deployment Steps

1. **Clone Repository**
```bash
git clone https://github.com/springboardmentor997-create/Modern-Digital-Banking-Dashboard.git
cd Modern-Digital-Banking-Dashboard
git checkout urmila-team1-backend
```

2. **Deploy with Docker**
```bash
# Windows
deploy.bat

# Or manually
docker-compose up -d --build
```

3. **Access Application**
- **Frontend**: http://localhost:4173
- **Backend API**: http://localhost:8000
- **API Docs**: http://localhost:8000/docs
- **Database**: localhost:5432

## 🔧 Management Commands

```bash
# Start services
docker-compose up -d

# Stop services
docker-compose down

# View logs
docker-compose logs -f

# Rebuild images
docker-compose build --no-cache

# Check status
docker-compose ps
```

## 📊 Default Credentials

**Admin User:**
- Email: admin@bank.com
- Password: admin123

**Regular User:**
- Email: user@bank.com  
- Password: user123

## 🗄️ Database Access

**PostgreSQL Connection:**
- Host: localhost
- Port: 5432
- Database: banking_db
- Username: postgres
- Password: password123

## 🛠️ Troubleshooting

**Port Conflicts:**
```bash
# Check what's using ports
netstat -ano | findstr :4173
netstat -ano | findstr :8000
netstat -ano | findstr :5432
```

**Reset Everything:**
```bash
docker-compose down -v
docker system prune -a
docker-compose up -d --build
```

## 📁 Project Structure

```
├── backend/           # FastAPI Backend
├── frontend/          # React Frontend  
├── docker-compose.yml # Docker Configuration
└── deploy.bat        # Deployment Script
```