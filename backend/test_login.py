#!/usr/bin/env python3
import sys
sys.path.append('/app')

from app.database import SessionLocal
from app.models.user import User
import bcrypt

def verify_password_simple(plain_password: str, hashed_password: str) -> bool:
    """Simple password verification using bcrypt directly"""
    try:
        # Ensure password is not too long for bcrypt
        if len(plain_password) > 72:
            plain_password = plain_password[:72]
        return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))
    except Exception as e:
        print(f"Password verification error: {e}")
        return False

def test_login():
    """Test login functionality"""
    print("🔐 Testing login functionality...")
    
    db = SessionLocal()
    try:
        # Test user login
        user = db.query(User).filter(User.email == "user@bank.com").first()
        if not user:
            print("❌ User not found")
            return False
        
        print(f"✅ User found: {user.email}")
        print(f"   Name: {user.name}")
        print(f"   Role: {user.role}")
        print(f"   Active: {user.is_active}")
        
        # Test password verification
        test_password = "user123"
        is_valid = verify_password_simple(test_password, user.password)
        
        if is_valid:
            print("✅ Password verification successful!")
            return True
        else:
            print("❌ Password verification failed!")
            return False
            
    except Exception as e:
        print(f"❌ Login test error: {e}")
        return False
    finally:
        db.close()

if __name__ == "__main__":
    test_login()