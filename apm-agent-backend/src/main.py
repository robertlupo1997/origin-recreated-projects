from fastapi import FastAPI
from .routers import health, metrics, alerts

app = FastAPI(
    title="APM Agent Backend",
    description="Application Performance Monitoring agent backend service",
    version="0.1.0"
)

app.include_router(health.router)
app.include_router(metrics.router, prefix="/api/v1")
app.include_router(alerts.router, prefix="/api/v1")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)