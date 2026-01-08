#!/usr/bin/env python3
import sys
sys.path.append('/app')

from app.database import SessionLocal
from app.models.user import User
from app.models.account import Account
from decimal import Decimal

def create_default_accounts():
    print("🏦 Creating default accounts...")
    
    db = SessionLocal()
    try:
        # Get the regular user
        user = db.query(User).filter(User.email == "user@bank.com").first()
        if not user:
            print("❌ User not found")
            return
        
        # Check if accounts already exist
        existing_accounts = db.query(Account).filter(Account.user_id == user.id).count()
        if existing_accounts > 0:
            print(f"✅ User already has {existing_accounts} accounts")
            return
        
        # Create default accounts
        accounts_to_create = [
            {
                "account_number": "ACC001001",
                "account_type": "savings",
                "balance": Decimal("5000.00"),
                "currency": "USD"
            },
            {
                "account_number": "ACC001002", 
                "account_type": "checking",
                "balance": Decimal("2500.00"),
                "currency": "USD"
            },
            {
                "account_number": "ACC001003",
                "account_type": "credit_card",
                "balance": Decimal("0.00"),
                "currency": "USD"
            }
        ]
        
        for account_data in accounts_to_create:
            account = Account(
                user_id=user.id,
                account_number=account_data["account_number"],
                account_type=account_data["account_type"],
                balance=account_data["balance"],
                currency=account_data.get("currency", "USD"),
                is_active=True
            )
            db.add(account)
            print(f"✅ Created {account_data['account_type']} account: {account_data['account_number']}")
        
        db.commit()
        print("🎉 All accounts created successfully!")
        
        # Verify creation
        total_accounts = db.query(Account).filter(Account.user_id == user.id).count()
        print(f"📊 Total accounts for user: {total_accounts}")
        
    except Exception as e:
        print(f"❌ Error creating accounts: {e}")
        db.rollback()
        raise
    finally:
        db.close()

if __name__ == "__main__":
    create_default_accounts()