from fastapi import FastAPI
from src.utils.db import Base,engine
from src.challenges.routes import challeng_routes
from src.user.routes import user_routes


Base.metadata.create_all(engine)

app = FastAPI()
app.include_router(challeng_routes)
app.include_router(user_routes)