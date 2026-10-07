from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from src.challenges import controllers
from src.challenges.dtos import (
    ChallengeCreate,
    ChallengePublicResponse
)

from src.utils.db import get_db


challenge_routes = APIRouter(
    prefix="/challenge"
)


@challenge_routes.post("/create")
def create_challenge(
    body: ChallengeCreate,
    db: Session = Depends(get_db)
):

    return controllers.create_challenge(
        db,
        body
    )


@challenge_routes.get(
    "/today",
    response_model=ChallengePublicResponse
)
def get_today_challenge(
    db: Session = Depends(get_db)
):

    return controllers.get_today_challenge(
        db
    )


@challenge_routes.get(
    "/{challenge_id}",
    response_model=ChallengePublicResponse
)
def get_challenge_by_id(
    challenge_id: int,
    db: Session = Depends(get_db)
):

    return controllers.get_challenge_by_id(
        db,
        challenge_id
    )