from sqlalchemy.orm import create_session, Session
from flask import current_app


def get_db():
    engine = current_app.config["ENGINE"]
    session: Session = create_session(engine)
    try:
        yield session
    finally:
        session.close()