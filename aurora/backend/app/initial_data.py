#!/usr/bin/env python3

from app.db.session import get_db
from app.db.crud import create_user
from app.db.schemas import UserCreate
from app.db.session import SessionLocal


def init() -> None:
    db = SessionLocal()

    create_user(
        db,
        UserCreate(
            email="baselinezero0@gmail.com",
            password="password",
            is_active=True,
            is_superuser=True,
        ),
    )


if __name__ == "__main__":
    print("Creating superuser baselinezero0@gmail.com")
    init()
    print("Superuser created")
