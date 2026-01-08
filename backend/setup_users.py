#!/usr/bin/env python3
import sys
sys.path.append('/app')

from app.database import SessionLocal
from app.models.user import User, UserRole
import bcrypt

def hash_password(password: str) -> str:
    """Hash password using bcrypt"""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

def create_default_users():
    print("🚀 Creating default users...")
    
    db = SessionLocal()
    try:
        # Check if users already exist
        existing_count = db.query(User).count()
        if existing_count > 0:
            print(f"✅ Database already has {existing_count} users")
            return
        
        # Create users
        users_to_create = [
            {
                "email": "admin@bank.com",
                "password": "admin123", 
                "name": "System Administrator",
                "role": UserRole.admin
            },
            {
                "email": "user@bank.com",
                "password": "user123",
                "name": "John Doe", 
                "role": UserRole.user
            },
            {
                "email": "auditor@bank.com",
                "password": "auditor123",
                "name": "Jane Auditor",
                "role": UserRole.auditor
            },
            {
                "email": "support@bank.com", 
                "password": "support123",
                "name": "Support Agent",
                "role": UserRole.support
            }
        ]
        
        for user_data in users_to_create:
            user = User(
                email=user_data["email"],
                password=hash_password(user_data["password"]),
                name=user_data["name"],
                role=user_data["role"],
                is_active=True,
                kyc_status="verified"
            )
            db.add(user)
            print(f"✅ Created user: {user_data['email']}")
        
        db.commit()
        print("🎉 All users created successfully!")
        
        # Verify creation
        total_users = db.query(User).count()
        print(f"📊 Total users in database: {total_users}")
        
    except Exception as e:
        print(f"❌ Error creating users: {e}")
        db.rollback()
        raise
    finally:
        db.close()

if __name__ == "__main__":
    create_default_users()