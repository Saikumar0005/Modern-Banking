# Banking Application Setup Guide

This guide will help you set up and run the complete banking application with both frontend and backend.

## Project Structure
```
frontend/
├── backend/          # FastAPI backend
├── frontend/         # React frontend
└── README.md        # This file
```

## Quick Start

### 1. Backend Setup (Required First)

1. **Navigate to backend directory:**
   ```bash
   cd backend
   ```

2. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Start the backend server:**
   ```bash
   python main.py
   ```
   
   Or on Windows, double-click `start_server.bat`

   The backend will run on `http://localhost:8000`

### 2. Frontend Setup

1. **Navigate to frontend directory:**
   ```bash
   cd frontend
   ```

2. **Install Node.js dependencies:**
   ```bash
   npm install
   ```

3. **Start the frontend development server:**
   ```bash
   npm run dev
   ```

   The frontend will run on `http://localhost:5173`

## Fixing the 405 Error

The 405 "Method Not Allowed" error you encountered was because:

1. **Missing Backend**: The backend server wasn't running
2. **Wrong URL**: Frontend was pointing to a non-existent Render deployment
3. **Missing API Endpoints**: The required expense tracking endpoints didn't exist

### Solution Applied:

1. ✅ **Created FastAPI Backend** (`backend/main.py`)
2. ✅ **Added All Required Endpoints**:
   - `GET /api/expenses/` - Get expenses
   - `POST /api/expenses/` - Create expense
   - `PUT /api/expenses/{id}` - Update expense
   - `DELETE /api/expenses/{id}` - Delete expense
   - `GET /api/expenses/categories/list` - Get categories
   - `GET /api/expenses/receipts/` - Get receipts
   - `GET /api/expenses/analytics/summary` - Get analytics

3. ✅ **Updated Frontend Configuration**:
   - Changed `.env` to use `http://localhost:8000`
   - Added better error handling

## Testing the Fix

1. **Start Backend:**
   ```bash
   cd backend
   python main.py
   ```

2. **Test API (Optional):**
   ```bash
   python test_api.py
   ```

3. **Start Frontend:**
   ```bash
   cd frontend
   npm run dev
   ```

4. **Access Application:**
   - Open `http://localhost:5173`
   - Navigate to Smart Expense Tracker
   - The 405 errors should be resolved!

## Deployment to Production

### Deploy Backend to Render:

1. **Push to GitHub:**
   ```bash
   git add .
   git commit -m "Add backend API"
   git push origin main
   ```

2. **Create Render Web Service:**
   - Connect your GitHub repo
   - Set **Root Directory**: `backend`
   - Set **Build Command**: `pip install -r requirements.txt`
   - Set **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`

3. **Update Frontend .env:**
   ```
   VITE_API_URL=https://your-app-name.onrender.com
   ```

### Deploy Frontend:

1. **Build Frontend:**
   ```bash
   cd frontend
   npm run build
   ```

2. **Deploy to Netlify/Vercel** or serve the `dist` folder

## API Documentation

Once backend is running, visit:
- **Interactive Docs**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

## Troubleshooting

### Backend Issues:
- **Port already in use**: Change port in `main.py` or kill existing process
- **Module not found**: Run `pip install -r requirements.txt`
- **Permission denied**: Run as administrator or use virtual environment

### Frontend Issues:
- **CORS errors**: Backend includes CORS middleware for all origins
- **Network errors**: Ensure backend is running on `http://localhost:8000`
- **Build errors**: Run `npm install` to ensure all dependencies are installed

### Common Errors Fixed:
- ✅ **405 Method Not Allowed**: Backend now provides all required endpoints
- ✅ **CORS errors**: Backend configured with proper CORS headers
- ✅ **Authentication errors**: Simplified auth for development
- ✅ **Missing endpoints**: All expense tracking endpoints implemented

## Features Implemented

### Backend Features:
- ✅ Expense CRUD operations
- ✅ Category management
- ✅ Receipt tracking
- ✅ Analytics and reporting
- ✅ JWT authentication (simplified)
- ✅ CORS support
- ✅ API documentation

### Frontend Features:
- ✅ Smart Expense Tracker
- ✅ Receipt scanning (mock implementation)
- ✅ Category-based expense tracking
- ✅ Analytics dashboard
- ✅ Responsive design
- ✅ Error handling

## Next Steps

1. **Test the application** with both frontend and backend running
2. **Add real authentication** if needed
3. **Deploy to production** using the deployment guide above
4. **Add database persistence** (currently uses in-memory storage)
5. **Implement real receipt scanning** using OCR services

The 405 errors should now be completely resolved! 🎉