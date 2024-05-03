from fastapi import FastAPI

from core.configs import settings
from api.v1.api import api_router


app = FastAPI(
    title='Curso API - Segurança',
    version="0.0.1",
    description="Projeto de teste do FastAPI",
)
app.include_router(api_router, prefix=settings.API_V1_STR)


if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000,
                log_level='info', reload=True)


"""
access_token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0eXBlIjoiYWNjZXNzX3Rva2VuIiwiZXhwIjoxNzE1MzYxMzk2LCJpYXQiOjE3MTQ3NTY1OTYsInN1YiI6IjIifQ.FiwxMUSkYxYYHxdd8bXvs_C_zkAPIzg1I-QOJ28ZsNk
token_type: bearer
"""
