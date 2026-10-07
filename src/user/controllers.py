from src.user.models import userModel
from src.user.dtos import userSchema,loginSchema,responseSchema
from sqlalchemy.orm import Session
from src.utils.settings import settings
from pwdlib import PasswordHash
import jwt
from fastapi import Request


password_hash = PasswordHash.recommended()

def get_password_hash(password):
     return password_hash.hash(password)

def verify_password(plain_password, hashed_password):
    return password_hash.verify(plain_password, hashed_password)

def user_register(db:Session,body:userSchema):

    new_user_name = db.query(userModel).filter(
    userModel.user_name == body.user_name

        ).first() 
    if new_user_name :
         return {"msg":"User name already exist"}
    
    new_user_name = db.query(userModel).filter(
        userModel.email == body.email
        
            ).first() 
    if new_user_name :
            return {"msg":"User email already exist"}

    hash_password = get_password_hash(body.password)

    user_data = userModel(
        user_name = body.user_name,
        email = body.email,
        password_hashed = hash_password,
        role = body.role
    )
    db.add(user_data)
    db.commit()
    db.refresh(user_data)
    return {
                 "id": user_data.id,
                "user_name": user_data.user_name,
                "email": user_data.email,
                "role": user_data.role
}


def user_login(body:loginSchema, db:Session):
      user = db.query(userModel).filter(userModel.user_name == body.user_name).first() 

      if not user:
            return {"msg":"Incorrect user name"}
      if not verify_password(body.password,user.password_hashed ):
           return {"msg":"Incorrect Password"}

      token = jwt.encode({"_id":user.id},settings.SECRET_KEY,settings.ALGORITHM)
      return {"token":token}

def is_auth(request:Request,db:Session):
     print(request)
     print(request.headers)
     token = request.headers.get("authorization")
     if not token :
          return {"msg":"You Are Unautherised User"}
     token = token.split(" ")[1]
     data = jwt.decode(token, settings.SECRET_KEY, settings.ALGORITHM)

     user = db.query(userModel).filter(userModel.id == data.get("_id")).first() 
     if user :
        return {
                 "id": user.id,
                "user_name": user.user_name,
                "email": user.email,
                "role": user.role
}
     else:
        return {"msg" : "You Are Unautherised User"}
    #  print(user.id)
    #  print(user.password_hashed)
     
    
    #  print(token)
    #  print(data)
    #  print(data.get("_id"))
    