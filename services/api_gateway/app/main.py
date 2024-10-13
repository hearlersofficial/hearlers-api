
from api_gateway.app.presentations.rest.controller import router as api_router
from dotenv import load_dotenv
from fastapi import FastAPI

from common.filter.exception_middleware import global_exception_handler

load_dotenv()


app = FastAPI(title="API Gateway")
app.add_exception_handler(Exception,global_exception_handler)
app.include_router(api_router, prefix="")
