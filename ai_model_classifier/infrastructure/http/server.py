# infrastructure/http/server.py
from fastapi import FastAPI
import uvicorn
from typing import List
from fastapi import APIRouter

class Server:
    def __init__(self, routes: List[APIRouter]):
        self.app = FastAPI(title="Medical Data API", description="API for processing medical data")

        # Register all routes
        for route in routes:
            self.app.include_router(route)

    def run(self, host="0.0.0.0", port=8000, reload=False):
        uvicorn.run(self.app, host=host, port=port, reload=reload)