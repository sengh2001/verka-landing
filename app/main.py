"""
Verka Dairy IIT Ropar — FastAPI Application Entry Point
"""

import os
from pathlib import Path

from dotenv import load_dotenv
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.api.routes import router

# ── Load environment variables ─────────────────────────────────────────────────
load_dotenv()

APP_TITLE = os.getenv("APP_TITLE", "Verka Dairy — IIT Ropar")
APP_ENV   = os.getenv("APP_ENV", "production")

# ── Resolve base paths ─────────────────────────────────────────────────────────
BASE_DIR       = Path(__file__).resolve().parent
TEMPLATES_DIR  = BASE_DIR / "templates"
STATIC_DIR     = BASE_DIR / "static"

# ── FastAPI app instance ───────────────────────────────────────────────────────
app = FastAPI(
    title=APP_TITLE,
    description="Landing page API for Verka Dairy franchise at IIT Ropar.",
    version="1.0.0",
    docs_url="/docs" if APP_ENV != "production" else None,  # hide docs in prod
    redoc_url=None,
)

# ── Mount static files ─────────────────────────────────────────────────────────
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

# ── Jinja2 template engine ─────────────────────────────────────────────────────
templates = Jinja2Templates(directory=TEMPLATES_DIR)

# ── Include API router ─────────────────────────────────────────────────────────
app.include_router(router)


# ── Root route — serves the landing page ──────────────────────────────────────
@app.get("/", response_class=HTMLResponse, include_in_schema=False)
async def index(request: Request):
    """Render the main landing page."""
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "app_title": APP_TITLE,
            "app_env": APP_ENV,
        },
    )
