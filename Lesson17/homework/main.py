from fastapi import FastAPI, Request
from routers import users, auth

app = FastAPI()
app.include_router(users.router, prefix='/users', tags=['Users'])
app.include_router(auth.router, prefix='/auth', tags=['Auth'])

@app.middleware('http')
async def log_requests(request: Request, call_next):
    print(f'Запрос: {request.method} {request.url}')
    response = await call_next(request)
    print(f'Ответ: {response.status_code}')
    return response

