from sqlalchemy import Column, Integer, String, Date, DateTime, Text, UniqueConstraint

from src.utils.db import Base


class challengeModel(Base):
    __tablename__ = "Challenge"

    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True,
        unique=True
    )

    question = Column(
        Text,
        nullable=False
    )

    option1 = Column(
        String,
        nullable=False
    )

    option2 = Column(
        String,
        nullable=False
    )

    option3 = Column(
        String,
        nullable=False
    )

    correct_option = Column(
        Integer,
        nullable=False
    )

    challenge_date = Column(
        Date,
        nullable=False,
        unique=True
    )

    created_at = Column(
        DateTime,
        nullable=False
    )

    updated_at = Column(
        DateTime,
        nullable=False
    )