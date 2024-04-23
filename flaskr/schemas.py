from typing import Generic, TypeVar, List

T = TypeVar("T")

class Page(Generic[T]):
    def __init__(self, elements: List[T], total_items):
        super().__init__()
        self.elements = elements
        self.total_items = total_items

class PackageStatusResponse:
    def __init__(self, package_status_id: int, name: str):
        self.package_status_id = package_status_id
        self.name = name