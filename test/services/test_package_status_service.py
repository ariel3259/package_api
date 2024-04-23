from unittest import TestCase
from flaskr.db import get_db, PackageStatus
from sqlalchemy import create_engine
from flaskr.services import PackageStatusService

class TestPackageStatusRepository(TestCase):
    def setUp(self):
        db_url = "sqlite:///data.db"
        engine = create_engine(db_url, echo=True)
        self.session = get_db(engine)
        package_status = [PackageStatus(name="En sucursal de origen"), PackageStatus(name="En camino a sucursal de destino"), PackageStatus(name = "Listo para su retiro"), PackageStatus(name = "Retirado")]
        self.session.add_all(package_status)
    
    def tearDown(self) -> None:
        self.session.close()

    def test_get_all(self):
        service = PackageStatusService(self.session)
        page = service.get_all()
        assert page.elements > 0
        assert page.total_items == 3
