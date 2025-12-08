import os 
from dotenv import load_dotenv

load_dotenv()

class Settings:
    def __init__(self):
        self.DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///:memory:")
        self.PASSWORD_LENGTH = int(os.getenv("PASSWORD_LENGTH", 12))
        self.APP_VERSION = os.getenv("APP_VERSION", "1.0.0")
        self.PROJECT_NAME = os.getenv("PROJECT_NAME", "UserManagementAPI")
        self.ENVIRONMENT = os.getenv("ENVIRONMENT", "local")


    def is_enviroment_local(self) -> bool:
        return self.ENVIRONMENT.lower() == "local"

settings = Settings()