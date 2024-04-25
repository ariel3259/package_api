from unittest import TestCase
from flaskr.db import MockSession, PackageStatus
from flaskr.repositories import PackageStatusRepository
from sqlalchemy import create_engine
from unittest.mock import Mock
from flaskr.services import PackageStatusService

class TestPackageStatusService(TestCase):
    def setUp(self):
        #db_url = "sqlite:///data.db"
        #engine = create_engine(db_url, echo=True)
        #self.session = get_db(engine)
        #self.session.add_all(package_status)
        self.package_status_repository_mock = PackageStatusRepository(MockSession())


    def tearDown(self) -> None:
        self.package_status_repository_mock = None

    def test_get_all(self):
        package_status = [PackageStatus(id = 1, name = "En sucursal de origen"), PackageStatus(id = 2, name = "En camino a sucursal de destino"), PackageStatus(id = 3, name = "Listo para su retiro"), PackageStatus(name = "Retirado")]
        response = (package_status, int(100))
        self.package_status_repository_mock.get_all = Mock(response)
        service = PackageStatusService(self.package_status_repository_mock)
        
        page = service.get_all()
        assert page.elements > 0
        assert page.total_items > 0
