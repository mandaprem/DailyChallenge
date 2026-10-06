from src.user.models import userModel
from src.user.dtos import userSchema,loginSchema
from sqlalchemy.orm import Session
from src.utils.settings import settings
from pwdlib import PasswordHash
import jwt


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
    return user_data


def user_login(body:loginSchema, db:Session):
      user = db.query(userModel).filter(userModel.user_name == body.user_name).first() 

      if not user:
            return {"msg":"Incorrect user name"}
      if not verify_password(body.password,user.password_hashed ):
           return {"msg":"Incorrect Password"}

      token = jwt.encode({"_id":user.id},settings.SECRET_KEY,settings.ALGORITHM)
      return {"token":token}
