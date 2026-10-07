from datetime import date, datetime
from pydantic import BaseModel, ConfigDict, Field


class ChallengeCreate(BaseModel):
    question: str = Field(...,min_length=5,max_length=1000)

    option1: str = Field(..., min_length=1, max_length=255)

    option2: str = Field(..., min_length=1, max_length=255)

    option3: str = Field(..., min_length=1, max_length=255)

    correct_option: int = Field(..., ge=1, le=3)

    challenge_date: date


class ChallengeUpdate(BaseModel):
    question: str | None = Field( default=None, min_length=5, max_length=1000)

    option1: str | None = Field( default=None, min_length=1,max_length=255)

    option2: str | None = Field( default=None, min_length=1, max_length=255)

    option3: str | None = Field(default=None, min_length=1, max_length=255)

    correct_option: int | None = Field( default=None, ge=1,le=3)

    challenge_date: date | None = None


class ChallengePublicResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    question: str
    option1: str
    option2: str
    option3: str
    challenge_date: date


class ChallengeAdminResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    question: str
    option1: str
    option2: str
    option3: str
    correct_option: int
    challenge_date: date
    created_at: datetime
    updated_at: datetime