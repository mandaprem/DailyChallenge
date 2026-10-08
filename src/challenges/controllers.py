from datetime import date, datetime

from fastapi import HTTPException, status,Depends
from sqlalchemy.orm import Session

from src.challenges.models import challengeModel
from src.challenges.dtos import ChallengeCreate
from src.user.models import userModel
from src.utils.helpers import is_auth

def create_challenge(
    db: Session,
    body: ChallengeCreate,
    user:userModel
):
    if user.role != "admin":
        return {
            "msg": "only Admins Can Create Challenges"
        }
    
    existing_challenge = db.query(challengeModel).filter(
        challengeModel.challenge_date == body.challenge_date
    ).first()

    if existing_challenge:
        return {
            "msg": "Challenge already exists for this date"
        }

    challenge_data = challengeModel(
        question=body.question,
        option1=body.option1,
        option2=body.option2,
        option3=body.option3,
        correct_option=body.correct_option,
        challenge_date=body.challenge_date,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    db.add(challenge_data)
    db.commit()
    db.refresh(challenge_data)

    return challenge_data


def get_today_challenge(
    db: Session
):

    today = date.today()

    challenge = db.query(challengeModel).filter(
        challengeModel.challenge_date == today
    ).first()

    if not challenge:
        return {
            "msg": "Today's challenge is not available"
        }

    return challenge


def get_challenge_by_id(
    db: Session,
    challenge_id: int
):

    challenge = db.query(challengeModel).filter(
        challengeModel.id == challenge_id
    ).first()

    if not challenge:
        return {
            "msg": "Challenge not found"
        }

    return challenge

def delete_challenge(
    db: Session,
    challenge_id: int,
    user:userModel
):
    if user.role != "admin":
        return {
            "msg": "only Admins Can Create / Delete Challenges"
        }

    challenge = db.query(challengeModel).filter(
        challengeModel.id == challenge_id
    ).first()

    if not challenge:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Challenge not found"
        )

    db.delete(challenge)
    db.commit()

    return {
        "msg": "Challenge deleted successfully"
    }

def get_all_challenges(
        db: Session,        
):
    challenges = db.query(challengeModel).all()
    return challenges


def update_challenge(
        db:Session,
        challenge_id:int,
        body:ChallengeCreate,
        user:userModel
):
    if user.role != "admin":
        return {
            "msg": "only Admins Can Update Challenges"
        }

    challenge = db.query(challengeModel).filter(
      challengeModel.id == challenge_id  
    ).first()

    if not challenge:
        return {
            "msg": "Challenge not found"
        }

    challenge.question = body.question
    challenge.option1 = body.option1
    challenge.option2 = body.option2
    challenge.option3 = body.option3
    challenge.correct_option = body.correct_option
    challenge.challenge_date = body.challenge_date
    challenge.updated_at = datetime.utcnow()

    db.commit()

    db.refresh(challenge)

    return challenge