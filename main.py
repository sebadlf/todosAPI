from dotenv import load_dotenv
load_dotenv() 

from fastapi.middleware.cors import CORSMiddleware

from fastapi import FastAPI
import models
from database import engine
from routers import todos

app = FastAPI()

models.Base.metadata.create_all(bind=engine)


app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:5173'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(todos.router)