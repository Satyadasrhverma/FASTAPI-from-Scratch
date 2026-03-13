from fastapi import FastAPI
from router.calculator_router import viv

app = FastAPI()

app.include_router(viv)