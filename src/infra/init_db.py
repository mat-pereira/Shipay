from src.infra.db import SessionLocal, engine
from src.domain.user_model import Base, RoleModel

def init_db():
    Base.metadata.create_all(bind=engine)
    
    db = SessionLocal()
    
    try:
        existing_roles = db.query(RoleModel).count()
        
        if existing_roles == 0:
            roles = [
                RoleModel(description="Admin"),
                RoleModel(description="User"),
                RoleModel(description="Manager"),
            ]
            db.add_all(roles)
            db.commit()
            print("✅ Roles criadas com sucesso!")
        else:
            print("✅ Roles já existem no banco")
            
    finally:
        db.close()

if __name__ == "__main__":
    init_db()