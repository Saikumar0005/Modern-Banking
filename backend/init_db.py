#!/usr/bin/env python3
"""
Database initialization script for Banking System
Creates tables and default users
"""

import asyncio
import sys
import os
sys.path.append('/app')

from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from app.database import Base, get_db
from app.models.user import User
from app.models.account import Account
from app.auth.password import get_password_hash
from app.config import settings

# Simple password hashing (max 72 chars for bcrypt)
def hash_password_simple(password: str) -> str:
    """Hash password with length limit for bcrypt"""
    if len(password) > 72:
        password = password[:72]
    return get_password_hash(password)

def init_database():
    """Initialize database with tables and default users"""
    try:
        # Create engine
        engine = create_engine(settings.DATABASE_URL)
        SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
        
        print("🔧 Creating database tables...")
        Base.metadata.create_all(bind=engine)
        print("✅ Tables created successfully")
        
        # Create session
        db = SessionLocal()
        
        try:
            # Check if users already exist
            existing_users = db.query(User).count()
            if existing_users > 0:
                print(f"✅ Database already has {existing_users} users")
                return
            
            print("👤 Creating default users...")
            
            # Create Admin User
            admin_user = User(
                email="admin@bank.com",
                full_name="System Administrator",
                hashed_password=hash_password_simple("admin123"),
                role="admin",
                is_active=True,
                is_verified=True
            )
            db.add(admin_user)
            db.flush()  # Get the ID
            
            # Create Regular User
            regular_user = User(
                email="user@bank.com", 
                full_name="John Doe",
                hashed_password=hash_password_simple("user123"),
                role="user",
                is_active=True,
                is_verified=True
            )
            db.add(regular_user)
            db.flush()
            
            # Create Auditor User
            auditor_user = User(
                email="auditor@bank.com",
                full_name="Jane Auditor", 
                hashed_password=hash_password_simple("auditor123"),
                role="auditor",
                is_active=True,
                is_verified=True
            )
            db.add(auditor_user)
            db.flush()
            
            # Create Support User
            support_user = User(
                email="support@bank.com",
                full_name="Support Agent",
                hashed_password=hash_password_simple("support123"), 
                role="support",
                is_active=True,
                is_verified=True
            )
            db.add(support_user)
            db.flush()
            
            # Create default accounts for regular user
            savings_account = Account(
                user_id=regular_user.id,
                account_number="ACC001001",
                account_type="savings",
                balance=5000.00,
                is_active=True
            )
            db.add(savings_account)
            
            checking_account = Account(
                user_id=regular_user.id,
                account_number="ACC001002", 
                account_type="checking",
                balance=2500.00,
                is_active=True
            )
            db.add(checking_account)
            
            # Commit all changes
            db.commit()
            
            print("✅ Default users created successfully:")
            print("   👨‍💼 Admin: admin@bank.com / admin123")
            print("   👤 User: user@bank.com / user123") 
            print("   🔍 Auditor: auditor@bank.com / auditor123")
            print("   🎧 Support: support@bank.com / support123")
            print("✅ Default accounts created for user@bank.com")
            
        except Exception as e:
            db.rollback()
            print(f"❌ Error creating users: {e}")
            raise
        finally:
            db.close()
            
    except Exception as e:
        print(f"❌ Database initialization failed: {e}")
        raise

if __name__ == "__main__":
    print("🚀 Initializing Banking System Database...")
    init_database()
    print("🎉 Database initialization complete!")