from fastapi import FastAPI,Request,Depends
from sqlalchemy.orm import Session
from src.utils.settings import settings
from src.user.models import userModel
import jwt
from src.utils.db import get_db


def is_auth(request:Request,db:Session = Depends(get_db)):
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
