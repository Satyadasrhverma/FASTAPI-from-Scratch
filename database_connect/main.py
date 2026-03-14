from fastapi import FastAPI
from router.router import router as router

import models
import database

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

app.include_router(router)