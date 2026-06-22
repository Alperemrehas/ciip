from fastapi import FastAPI

from app.api.v1.routes_health import router as health_router
from app.core.config import get_settings

settings = get_settings()


def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.app_name,
        version="0.1.0",
        description=(
            "CIIP imports external interoperability test results and analyzes "
            "company, industry, capability, system, partner, and year-over-year "
            "interoperability maturity."
        ),
    )

    app.include_router(
        health_router,
        prefix=settings.api_v1_prefix,
    )

    return app


app = create_app()