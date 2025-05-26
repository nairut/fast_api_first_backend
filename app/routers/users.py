from fastapi import APIRouter, FastAPI
from ..schemas import UserIn, UserOut, UserList, Login
from ..services.users import Services


router = FastAPI()

services = Services()


router = APIRouter(
    prefix="/auth",
    tags=["users"]
)


@router.post("/register", response_model=UserOut)
async def create_user(new_user: UserIn):
    user = services.add_user_fake_file(new_user)
    return {"username": user.username, "user_id": user.user_id}


@router.get("/users", response_model= UserList)
async def show_user_list():
    list_of_users = services.get_user_list()
    return {"users" : list_of_users}
 

@router.post("/login")
async def user_login(user_login: Login):
    user_is_loged = services.user_log_in(user_login.username, user_login.password)
    if user_is_loged == True:
        return {f"Hi {user_login.username}": 'You are logged in'}
    else:
        return {f"User: {user_login.username}": "Username and Password does not match"}
    

@router.post("/logout")
async def user_login(user_login: Login):
    user_is_loged = services.user_log_in(user_login.username, user_login.password)
    if user_is_loged == True:
        return {f"Hi {user_login.username}": 'You are logged out'}
    else:
        return {f"User: {user_login.username}": "Not found in database"}


if __name__ == '__main__':
    print("Starting server...")
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)