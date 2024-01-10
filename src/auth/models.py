from datetime import datetime

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import Integer, String, ForeignKey, TIMESTAMP, JSON
from sqlalchemy.orm import Mapped, mapped_column

from database import Base

MC = mapped_column


# Define the base class

class Role(Base):
    __tablename__ = 'role'
    id: Mapped[int] = MC(Integer, primary_key=True)
    name: Mapped[str] = MC(String, nullable=False)
    permissions: Mapped[JSON] = MC(JSON)


class User(SQLAlchemyBaseUserTable[int], Base):
    id: Mapped[int] = MC(Integer, primary_key=True)
    username: Mapped[str] = MC(String(length=100), nullable=False)
    registered_at: Mapped[datetime] = MC(TIMESTAMP, default=datetime.utcnow)
    role_id: Mapped[int] = MC(Integer, ForeignKey(Role.id))

    # From parent class
    # email: Mapped[str] = mapped_column(
    #     String(length=320), unique=True, index=True, nullable=False
    # )
    # hashed_password: Mapped[str] = mapped_column(
    #     String(length=1024), nullable=False
    # )
    # is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    # is_superuser: Mapped[bool] = mapped_column(
    #     Boolean, default=False, nullable=False
    # )
    # is_verified: Mapped[bool] = mapped_column(
    #     Boolean, default=False, nullable=False
    # )
