# tokenizer_query/infrastructure/http/server.py
from fastapi import FastAPI
import uvicorn
from typing import List, Optional
from fastapi import APIRouter
from tokenizer_query.domain.port_tokenizer_repo import ITokenizerRepository


class ServerHTTP:
    def __init__(self, repo: ITokenizerRepository,  routes: Optional[List[APIRouter]] = None):
        self.app = FastAPI(title="Tokenizer Query API")
        self.repo = repo

        # Add default routes
        @self.app.get("/data")
        async def root():
            try:
                data = self.repo.get_all_records()
                return {"data": data}
            except Exception as e:
                return {"error": str(e)}

        @self.app.get("/health")
        async def health_check():
            return {"status": "healthy"}

        # Register additional routes
        if routes:
            for route in routes:
                self.app.include_router(route)

    def run(self, host="0.0.0.0", port=8001):
        uvicorn.run(self.app, host=host, port=port)