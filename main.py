import asyncio

from aiogram import Bot, Dispatcher, types
from fastapi import FastAPI, HTTPException
from fastapi.responses import ORJSONResponse

from src.admin.sql_admin import app as a_router
from src.api.controllers.base import router as base_router

app = FastAPI(default_response_class=ORJSONResponse, debug=True)
app.include_router(base_router)

app.mount("/", a_router)
