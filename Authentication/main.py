from fastapi import FastAPI
import database, models
from router.user_router import router as router

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

app.include_router(router)