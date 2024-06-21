from fastapi import FastAPI
import uvicorn
from presentation.routes import usuario_routes

app = FastAPI()

app.include_router(usuario_routes.router)

if __name__ == "__main__":
    uvicorn.run(app="main:app", port=8000, reload=True)



