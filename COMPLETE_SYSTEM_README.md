# Modern Digital Banking Dashboard

A comprehensive personal banking hub that unifies accounts, transactions, budgeting, bills, and rewards into a single platform with insights and alerts.

## 🚀 Project Overview

This is a complete 8-week milestone banking system implementation featuring:
- Multi-account overview & transaction feeds
- Expense categorization & monthly budgets  
- Bill payment reminders & workflows
- Rewards tracking & insights
- Currency conversion summaries
- Role-based access control
- JWT authentication
- CSV/PDF export functionality

## 🏗️ Tech Stack

- **Frontend**: React.js + Tailwind CSS + Vite
- **Backend**: FastAPI + SQLAlchemy
- **Database**: PostgreSQL
- **Authentication**: JWT (access + refresh tokens)
- **Extras**: Currency conversion API, CSV import/export

## 📋 Implemented Modules

### ✅ Module A: Auth & User Setup
- User registration and login
- JWT-based authentication
- Role-based access control (Admin, User, Auditor, Support)
- KYC status management
- Password hashing and security

### ✅ Module B: Accounts & Transactions  
- Multi-account management (Savings, Checking, Credit Card, Loan, Investment)
- Transaction CRUD operations
- CSV import/export functionality
- Real-time balance updates
- Transaction categorization
- Currency support (INR, USD, EUR, GBP)

### ✅ Module C: Budgeting & Categorization
- Monthly budget creation and tracking
- Expense categorization (Food, Transportation, Entertainment, Shopping, Bills)
- Budget progress monitoring
- Spending analytics
- Category-wise expense breakdown

### ✅ Module D: Bills, Reminders & Rewards
- Bill management with due dates
- Auto-pay configuration
- Rewards program tracking
- Points balance management
- Bill payment reminders
- Multiple reward programs support

### ✅ Module E: Insights, Alerts & Admin
- Financial insights and analytics
- Cash flow analysis
- Top merchants tracking
- Burn rate calculations
- System alerts (Low balance, Bill due, Budget exceeded)
- Admin dashboard with system monitoring
- Audit logs and user management
- CSV/PDF export reports

## 🗄️ Database Schema

### Users Table
- `id` (INT, PK)
- `name` (VARCHAR)
- `email` (VARCHAR, UNIQUE)
- `password` (VARCHAR, hashed)
- `phone` (VARCHAR)
- `role` (ENUM: admin, user, auditor, support)
- `kyc_status` (ENUM: unverified, verified)
- `is_active` (BOOLEAN)
- `created_at` (TIMESTAMP)

### Accounts Table
- `id` (INT, PK)
- `user_id` (FK to Users.id)
- `name` (VARCHAR)
- `bank_name` (VARCHAR)
- `account_type` (ENUM: savings, checking, credit_card, loan, investment)
- `account_number` (VARCHAR)
- `masked_account` (VARCHAR)
- `currency` (CHAR(3))
- `balance` (NUMERIC)
- `is_active` (BOOLEAN)
- `created_at` (TIMESTAMP)

### Transactions Table
- `id` (INT, PK)
- `account_id` (FK to Accounts.id)
- `user_id` (FK to Users.id)
- `description` (VARCHAR)
- `category` (VARCHAR)
- `amount` (NUMERIC)
- `currency` (CHAR(3))
- `txn_type` (ENUM: debit, credit)
- `merchant` (VARCHAR)
- `txn_date` (TIMESTAMP)
- `posted_date` (TIMESTAMP)

### Budgets Table
- `id` (INT, PK)
- `user_id` (FK to Users.id)
- `name` (VARCHAR)
- `month` (INT)
- `year` (INT)
- `category` (VARCHAR)
- `category_id` (INT)
- `limit_amount` (NUMERIC)
- `spent_amount` (NUMERIC)
- `created_at` (TIMESTAMP)

### Bills Table
- `id` (INT, PK)
- `user_id` (FK to Users.id)
- `biller_name` (VARCHAR)
- `due_date` (DATE)
- `amount_due` (NUMERIC)
- `status` (ENUM: upcoming, paid, overdue)
- `auto_pay` (BOOLEAN)
- `created_at` (TIMESTAMP)

### Rewards Table
- `id` (INT, PK)
- `user_id` (FK to Users.id)
- `program_name` (VARCHAR)
- `points_balance` (INT)
- `title` (VARCHAR)
- `last_updated` (TIMESTAMP)

### Alerts Table
- `id` (INT, PK)
- `user_id` (FK to Users.id)
- `type` (ENUM: low_balance, bill_due, budget_exceeded)
- `message` (TEXT)
- `is_read` (BOOLEAN)
- `created_at` (TIMESTAMP)

### AdminLogs Table
- `id` (INT, PK)
- `admin_id` (FK to Users.id)
- `action` (TEXT)
- `target_type` (VARCHAR)
- `target_id` (INT)
- `timestamp` (TIMESTAMP)

## 🚀 Quick Start

### Prerequisites
- Docker and Docker Compose
- Node.js 16+ and npm
- Python 3.8+
- PostgreSQL (or use Docker)

### Option 1: Docker Deployment (Recommended)
```bash
# Clone the repository
git clone <repository-url>
cd frontend

# Deploy with Docker
docker-compose up --build -d
```

### Option 2: Manual Setup
```bash
# Backend setup
cd backend
pip install -r requirements.txt
python setup_complete_system.py
python -m uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

# Frontend setup (in new terminal)
cd frontend
npm install
npm run dev
```

### Option 3: Windows Batch Script
```bash
# Run the complete deployment script
deploy_complete.bat
```

## 🌐 Access Points

- **Frontend**: http://localhost:5173
- **Backend API**: http://localhost:8000
- **API Documentation**: http://localhost:8000/docs
- **PostgreSQL**: localhost:5433 (Docker) / localhost:5432 (Local)

## 🔐 Default Login Credentials

| Role | Email | Password |
|------|-------|----------|
| Admin | admin@bank.com | admin123 |
| User | user@bank.com | user123 |
| Auditor | auditor@bank.com | auditor123 |
| Support | support@bank.com | support123 |

## 📊 Key Features

### 🏦 Multi-Account Management
- Support for multiple account types
- Real-time balance tracking
- Account linking and management
- Currency support (INR, USD, EUR, GBP)

### 💳 Transaction Management
- CRUD operations for transactions
- CSV import/export functionality
- Automatic categorization
- Transaction search and filtering
- Balance reconciliation

### 💰 Budget & Expense Tracking
- Monthly budget creation
- Category-wise spending limits
- Progress tracking with visual indicators
- Budget vs actual spending analysis
- Overspend alerts

### 📄 Bill Management
- Bill creation and tracking
- Due date reminders
- Auto-pay configuration
- Payment status tracking
- Recurring bill support

### 🎁 Rewards Program
- Multiple reward programs
- Points balance tracking
- Reward redemption history
- Program-specific benefits

### 📈 Financial Insights
- Cash flow analysis
- Spending trends
- Category breakdown
- Top merchants
- Burn rate calculations
- Monthly/yearly comparisons

### 🚨 Smart Alerts
- Low balance warnings
- Bill due notifications
- Budget exceeded alerts
- Suspicious activity detection
- Customizable alert preferences

### 🔄 Currency Conversion
- Real-time exchange rates
- Multi-currency support
- Conversion history
- Rate comparison tools

### 📤 Export & Import
- CSV transaction export
- PDF report generation
- Transaction import templates
- Bulk data operations

### 👥 Role-Based Access
- **Admin**: Full system access, user management, system monitoring
- **User**: Personal banking features, transactions, budgets
- **Auditor**: Read-only access, audit trails, compliance reports
- **Support**: Customer service tools, ticket management

## 🛠️ API Endpoints

### Authentication
- `POST /api/auth/register` - User registration
- `POST /api/auth/login` - User login
- `POST /api/auth/refresh` - Token refresh

### Accounts
- `GET /api/accounts/` - Get user accounts
- `POST /api/accounts/` - Create new account
- `PUT /api/accounts/{id}` - Update account
- `DELETE /api/accounts/{id}` - Delete account

### Transactions
- `GET /api/transactions/` - Get transactions
- `POST /api/transactions/` - Create transaction
- `PUT /api/transactions/{id}` - Update transaction
- `DELETE /api/transactions/{id}` - Delete transaction
- `POST /api/transactions/import-csv` - Import CSV

### Budgets
- `GET /api/budgets/` - Get budgets
- `POST /api/budgets/` - Create budget
- `PUT /api/budgets/{id}` - Update budget
- `DELETE /api/budgets/{id}` - Delete budget

### Bills
- `GET /api/bills/` - Get bills
- `POST /api/bills/` - Create bill
- `PUT /api/bills/{id}` - Update bill
- `DELETE /api/bills/{id}` - Delete bill

### Rewards
- `GET /api/rewards/` - Get rewards
- `POST /api/rewards/` - Create reward
- `PUT /api/rewards/{id}` - Update reward

### Insights
- `GET /api/insights/` - Get financial insights
- `GET /api/insights/spending` - Spending analysis
- `GET /api/insights/categories` - Category breakdown
- `GET /api/insights/trends` - Monthly trends

### Admin
- `GET /api/admin/users` - Get all users
- `GET /api/admin/system-summary` - System statistics
- `PUT /api/admin/users/{id}/activate` - Activate user
- `PUT /api/admin/users/{id}/deactivate` - Deactivate user

### Currency
- `GET /api/currency/rates` - Get exchange rates
- `GET /api/currency/convert` - Convert currency
- `GET /api/currency/supported` - Supported currencies

### Export
- `GET /api/export/transactions/csv` - Export transactions CSV
- `GET /api/export/transactions/template` - Download CSV template

## 🔧 Configuration

### Environment Variables
Create `.env` files in backend and frontend directories:

**Backend (.env)**
```env
DATABASE_URL=postgresql://postgres:password@localhost:5432/banking_db
JWT_SECRET_KEY=your-secret-key-here
JWT_ALGORITHM=HS256
JWT_EXPIRATION_HOURS=24
```

**Frontend (.env)**
```env
VITE_API_BASE_URL=http://localhost:8000
VITE_APP_NAME=Banking Dashboard
```

### Docker Configuration
The system includes Docker configuration for easy deployment:
- `docker-compose.yml` - Development environment
- `docker-compose.prod.yml` - Production environment
- `Dockerfile` - Backend container
- `frontend/Dockerfile` - Frontend container

## 🧪 Testing

### Backend Testing
```bash
cd backend
pytest tests/
```

### Frontend Testing
```bash
cd frontend
npm test
```

## 📈 Performance Features

- **Lazy Loading**: Components loaded on demand
- **Caching**: API response caching
- **Pagination**: Large dataset handling
- **Debouncing**: Search input optimization
- **Connection Pooling**: Database optimization
- **Index Optimization**: Fast query performance

## 🔒 Security Features

- **JWT Authentication**: Secure token-based auth
- **Password Hashing**: bcrypt encryption
- **CORS Protection**: Cross-origin security
- **SQL Injection Prevention**: Parameterized queries
- **XSS Protection**: Input sanitization
- **Rate Limiting**: API abuse prevention
- **Role-Based Access**: Permission management

## 🚀 Deployment

### Production Deployment
1. Update environment variables for production
2. Configure SSL certificates
3. Set up reverse proxy (nginx)
4. Configure database backups
5. Set up monitoring and logging

### Scaling Considerations
- Database read replicas
- Redis caching layer
- Load balancer configuration
- Container orchestration (Kubernetes)
- CDN for static assets

## 📝 Development

### Project Structure
```
frontend/
├── backend/                 # FastAPI backend
│   ├── app/
│   │   ├── models/         # Database models
│   │   ├── routers/        # API endpoints
│   │   ├── schemas/        # Pydantic schemas
│   │   └── utils/          # Utility functions
│   └── requirements.txt
├── frontend/               # React frontend
│   ├── src/
│   │   ├── components/     # React components
│   │   ├── pages/          # Page components
│   │   ├── api/           # API client
│   │   └── utils/         # Utility functions
│   └── package.json
└── docker-compose.yml
```

### Contributing
1. Fork the repository
2. Create feature branch
3. Make changes with tests
4. Submit pull request

## 📄 License

This project is licensed under the MIT License.

## 🆘 Support

For support and questions:
- Check the API documentation at `/docs`
- Review the troubleshooting section in README
- Create an issue in the repository

---

**Banking System Status**: ✅ **FULLY IMPLEMENTED AND OPERATIONAL**

All 8-week milestone requirements have been completed successfully!