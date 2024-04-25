from flaskr.repositories import PackageStatusRepository
from flaskr.schemas import PackageStatusResponse, Page

class PackageStatusService:
    def __init__(self, package_status_repository: PackageStatusRepository):
        self.package_status_repository = package_status_repository
    
    def get_all(self, offset = 0, limit = 10):
        records, total_items= self.package_status_repository.get_all(offset, limit)
        response = [PackageStatusResponse(x.id, x.name) for x in records]
        return Page[PackageStatusResponse](response, total_items)
