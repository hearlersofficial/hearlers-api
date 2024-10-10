from fastapi import APIRouter

user_router = APIRouter()

@user_router.post("/create")
async def create_user():
    # 유저 생성 로직
    return {"message": "User created"}
