from pydantic import BaseModel

class userSchema(BaseModel):
    user_name:str
    email:str
    password:str
    role : str

class responseSchema(BaseModel):
    id:int
    user_name:str
    email:str
    role : str

class loginSchema(BaseModel):
    user_name:str
    password:str    