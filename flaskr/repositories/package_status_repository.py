from flaskr.repositories.abstracts import Repository
from flaskr.db.model import PackageStatus

class PackageStatusRepository(Repository[PackageStatus]):
    def __init__(self, session):
        super().__init__(session)
    
    def get_all(self, offset, limit):
        query = self.session.query(PackageStatus).where(PackageStatus.state == True)
        records = query.offset(offset).limit(limit).all()
        total_items = query.count()
        return (records, total_items)