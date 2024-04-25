from sqlalchemy.orm import create_session, Session

def get_db(engine):
    session: Session = create_session(engine)
    return session

class MockSession:
    def query(self, entity):
        return self

    def where(self, condition):
        return self

    def offset(self, offset):
        return self

    def limit(self, limit):
        return self

    def all(self):
        # Return some mock data
        return []
