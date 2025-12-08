from fastapi import FastAPI
from src.api.router import router
from src.infra.db import engine
from src.domain.user_model import Base 
from src.infra.init_db import init_db
from src.utils.logger import log_error
from src.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    description="API para Gerenciamento de Usuários",
    version=settings.APP_VERSION,
)

try:
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    init_db()
    
except Exception as e:
    log_error(f"Erro ao inicializar banco: {e}", e)
    raise

app.include_router(router)

@app.get("/liveness", tags=["Health"])
def health_check():
    return {"status": "healthy", "version": settings.APP_VERSION}