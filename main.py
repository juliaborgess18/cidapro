import json
from fastapi import FastAPI
import uvicorn
from infrastructure.repositories.pais_repo import PaisRepo
from presentation.routes import usuario_routes

app = FastAPI()

app.include_router(usuario_routes.router)

# if __name__ == "__main__":
    # uvicorn.run(app="main:app", port=8000, reload=True)



