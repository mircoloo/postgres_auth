from fastapi import FastAPI
from dotenv import load_dotenv
load_dotenv()
app = FastAPI()

from fastapi import FastAPI
from .database import Base, engine
from .routes import auth, users

Base.metadata.create_all(bind=engine)

app = FastAPI(title="User Service")

app.include_router(auth.router)
app.include_router(users.router)
