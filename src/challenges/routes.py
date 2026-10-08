from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from src.challenges import controllers
from src.challenges.dtos import (
    ChallengeCreate,
    ChallengePublicResponse
)

from src.utils.db import get_db
from src.utils.helpers import is_auth
from src.user.models import userModel


challenge_routes = APIRouter(
    prefix="/challenge"
)


@challenge_routes.post("/create")
def create_challenge(
    body: ChallengeCreate,
    db: Session = Depends(get_db),
    user:userModel = Depends(is_auth)
):

    return controllers.create_challenge(
        db,
        body,
        user
    )


@challenge_routes.get(
    "/today",
    response_model=ChallengePublicResponse
)
def get_today_challenge(
    db: Session = Depends(get_db),
    user:userModel = Depends(is_auth)
):

    return controllers.get_today_challenge(
        db
    )


@challenge_routes.get(
    "get/{challenge_id}",
    response_model=ChallengePublicResponse
)
def get_challenge_by_id(
    challenge_id: int,
    db: Session = Depends(get_db),
    user:userModel = Depends(is_auth)
):

    return controllers.get_challenge_by_id(
        db,
        challenge_id
    )

@challenge_routes.delete(
    "/{challenge_id}"
)   
def delete_challenge(
    challenge_id: int,
    db: Session = Depends(get_db),
    user:userModel = Depends(is_auth)
):

    return controllers.delete_challenge(
        db,
        challenge_id,
        user
    )

@challenge_routes.get("/all"
)
def get_all_challenges(
    db: Session = Depends(get_db),
    user:userModel = Depends(is_auth)
):
    return controllers.get_all_challenges(
        db
    )

@challenge_routes.put("update/{challenge_id}"
)
def update_challenge(
    challenge_id: int,
    body: ChallengeCreate,
    db: Session = Depends(get_db),
    user:userModel = Depends(is_auth)
):
    return controllers.update_challenge(
        db,
        challenge_id,
        body,
        user
    )