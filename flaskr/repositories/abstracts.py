from abc import ABCMeta, abstractmethod
from typing import TypeVar, Generic
from sqlalchemy.orm import Session
from sqlalchemy import select
from datetime import datetime
from flaskr.db import Base

T = TypeVar("T", bound=Base)

class Repository(Generic[T],metaclass=ABCMeta):
    def __init__(self, session: Session):
        self.session = session

    @abstractmethod
    def get_all(self, offset, limit):
        pass

    def get_by_id(self, id: int):
        record = self.session.get(T, id)
        return record

class RepositoryCRUD(Generic[T],Repository[T], metaclass=ABCMeta):
    
    @abstractmethod
    def create(self, record):
        pass

    @abstractmethod
    def update(self, record, id):
        keys = record.keys()
        record_to_update = self.session.get(T, id)
        if record_to_update == None or len(keys) == 0:
            return None
        for key in keys:
            record_to_update[key] = record[key] if record_to_update[key] != record[key] else record_to_update[key]
        record_to_update["updated_at"] = datetime.now()
        self.session.add(record_to_update)
        self.session.commit()


    def delete(self, id) -> bool:
        record = self.session.get(T, id)
        if record == None:
            return False
        self.session.delete(record)
        self.session.commit()
        return True