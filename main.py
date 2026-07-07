import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from config.config import settings
from config.database import Base, engine
from api.v1 import routers

import models

if settings.ENV == "development":
    Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)
    
app = FastAPI(
    title="Teleoperation Robot Backend",
    description="Teleoperation Robot backend",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.FRONTEND_URL],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(routers.router)

if __name__ == "__main__":
    uvicorn.run(app)
