
from api_gateway.app.presentations.rest.controller import router as api_router
from dotenv import load_dotenv
from fastapi import FastAPI

load_dotenv()


app = FastAPI(title="API Gateway")

app.include_router(api_router, prefix="/api")
