from fastapi import APIRouter, HTTPException
from starlette.responses import Response
from starlette.status import HTTP_202_ACCEPTED, HTTP_406_NOT_ACCEPTABLE

router = APIRouter()


@router.get("/hello")
async def get_hello():
    return {"hello": "world"}
