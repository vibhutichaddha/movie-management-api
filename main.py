from fastapi import FastAPI
from routes import router
app=FastAPI(title="Movie Management API", description="REST API for managing movies", version="1.0.0")
app.include_router(router)