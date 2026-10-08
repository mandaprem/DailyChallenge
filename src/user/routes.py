from fastapi import FastAPI,APIRouter,Depends,Request
from src.user import controllers
from src.utils.db import get_db
from sqlalchemy.orm import Session
from src.user.models import userModel
from src.user.dtos import userSchema,loginSchema,responseSchema

user_routes = APIRouter(prefix="/user")

@user_routes.get("/")
def user():
    return {"msg":"User Page"}

@user_routes.post("/register")
def user_register(body:userSchema,db:Session = Depends(get_db)):
    return controllers.user_register(db,body)

@user_routes.post("/login")
def user_login(body:loginSchema, db:Session = Depends(get_db)):
    return controllers.user_login(body,db)

@user_routes.get("/is_auth" )
def is_auth(request:Request,db:Session = Depends(get_db)):
    return controllers.is_auth(request,db)

@user_routes.get("/profile")
def user_profile(request:Request,db:Session = Depends(get_db),user:userModel =Depends(is_auth)):
    return controllers.user_profile(request,db,user)