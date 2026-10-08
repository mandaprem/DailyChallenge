
from fastapi import Request, Depends, HTTPException
from sqlalchemy.orm import Session
import jwt

from src.utils.settings import settings
from src.user.models import userModel
from src.utils.db import get_db


def is_auth(
    request: Request,
    db: Session = Depends(get_db)
):
    token = request.headers.get("authorization")

    if not token:
        raise HTTPException(
            status_code=401,
            detail="You Are Unauthorised User"
        )

    token = token.split(" ")[1]

    data = jwt.decode(
        token,
        settings.SECRET_KEY,
        settings.ALGORITHM
    )

    user = db.query(userModel).filter(
        userModel.id == data.get("_id")
    ).first()

    if not user:
        raise HTTPException(
            status_code=401,
            detail="You Are Unauthorised User"
        )

    return user