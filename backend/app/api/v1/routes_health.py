from fastapi import APIRouter

from app.core.config import get_settings
from app.db.session import check_database_connection

router = APIRouter(prefix="/health", tags=["Health"])

settings = get_settings()


@router.get("")
def health_check() -> dict:
    db_ok = check_database_connection()

    return {
        "status": "ok" if db_ok else "degraded",
        "app_name": settings.app_name,
        "environment": settings.app_env,
        "database": "connected" if db_ok else "disconnected",
    }