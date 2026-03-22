from fastapi import FastAPI
import database, models
from router.user_router import router as router
from router.notes_router import create_note, get_notes, delete_note 

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

app.include_router(router)




