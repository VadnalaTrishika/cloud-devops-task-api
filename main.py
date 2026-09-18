from fastapi import FastAPI

app = FastAPI(title="Cloud DevOps Task API")


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