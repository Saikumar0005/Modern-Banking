import bcrypt

def hash_password(password: str) -> str:
    """Hash password using bcrypt with length limit"""
    # Ensure password is not too long for bcrypt
    if len(password) > 72:
        password = password[:72]
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify password using bcrypt with length limit"""
    try:
        # Ensure password is not too long for bcrypt
        if len(plain_password) > 72:
            plain_password = plain_password[:72]
        return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))
    except Exception as e:
        print(f"Password verification error: {e}")
        return False