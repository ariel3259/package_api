from typing import List, Optional
from sqlalchemy import String, ForeignKey, Integer, DATETIME, Boolean
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from datetime import datetime

class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    created_at: Mapped[datetime] = mapped_column(DATETIME, default_factory=datetime.now)
    created_by: Mapped[str] = mapped_column(String, default="system")
    updated_at: Mapped[datetime] = mapped_column(DATETIME, default_factory=datetime.now)
    updated_by: Mapped[str] = mapped_column(String, default="system")
    state: Mapped[bool] = mapped_column(Boolean, default=True)

class PackageStatus(Base):
    __tablename__ = "package_status"
    name: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    packages: Mapped[List["Packages"]] = relationship(
        "package_status",
        cascade="all, delete-orphan"
    )

class Packages(Base):
    __tablename__ = "packages"
    package_status_id: Mapped[int] = mapped_column(ForeignKey("package_status.id"))
    package_status: Mapped["PackageStatus"] = relationship(back_populates="packages")
    receiver_address: Mapped[str] = mapped_column(String, nullable=False)
    sender_address: Mapped[str] = mapped_column(String, nullable=False)
    