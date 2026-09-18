import logging

from fastapi import FastAPI, Request
from prometheus_fastapi_instrumentator import Instrumentator

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

app = FastAPI(title="Cloud DevOps Task API")

Instrumentator().instrument(app).expose(app)


@app.middleware("http")
async def log_requests(request: Request, call_next):
    logger.info("Request started: %s %s", request.method, request.url.path)

    response = await call_next(request)

    logger.info(
        "Request completed: %s %s - Status %s",
        request.method,
        request.url.path,
        response.status_code
    )

    return response


@app.get("/")
def home():
    return {
        "message": "Cloud DevOps Task API is running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }