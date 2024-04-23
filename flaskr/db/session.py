from sqlalchemy.orm import create_session, Session

def get_db(engine):
    session: Session = create_session(engine)
    return session