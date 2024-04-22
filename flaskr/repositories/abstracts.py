from abc import ABCMeta, abstractmethod
from typing import TypeVar, Generic
from sqlalchemy.orm import Session
from sqlalchemy import select
from flaskr.db import Base

T = TypeVar("T", bound=Base)

class Repository(Generic[T],metaclass=ABCMeta):
    def __init__(self, session: Session):
        self.session = session

    @abstractmethod()
    def get_all(self, offset, limit):
        pass

    def get_by_id(self, id: int):
        record = self.session.get(T, id)
        return record
    
    @abstractmethod()
    def get_by_args(self, **kwargs):
        pass

class RepositoryCRUD(Generic[T],Repository[T], metaclass=ABCMeta):
    
    @abstractmethod()
    def create(self, record):
        pass

    @abstractmethod()
    def update(self, record):
        pass

    def delete(self, id) -> bool:
        record = self.session.get(T, id)
        if record == None:
            return False
        self.session.delete(record)
        self.session.commit()
        return True