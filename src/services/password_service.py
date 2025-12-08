import secrets
import bcrypt
from src.config import settings

class PasswordService:
    def generate(self) -> str:
        return secrets.token_urlsafe(settings.PASSWORD_LENGTH)
    
    def hash(self, password: str) -> str:
        return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    
    def verify(self, password: str, hashed: str) -> bool:
        return bcrypt.checkpw(password.encode(), hashed.encode())