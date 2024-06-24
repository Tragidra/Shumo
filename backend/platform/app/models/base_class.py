from sqlalchemy import Column, DateTime, Integer, func
from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy.orm import mapped_column


@as_declarative()
class Base:
    id: int = mapped_column(Integer, primary_key=True, autoincrement=True)
    created_at = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at = mapped_column(DateTime(timezone=True), onupdate=func.now(), nullable=True)
    deleted_at = mapped_column(DateTime(timezone=True), nullable=True)
