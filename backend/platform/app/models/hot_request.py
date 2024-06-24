from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import declared_attr, mapped_column

from backend.platform.app.models.base_class import Base


class Hot_request(Base):
    __tablename__ = 'hot_request'

    searchWord = mapped_column(String, index=True)
    score = mapped_column(Integer, index=True)
    content = mapped_column(String, index=True) #Доделать
    source = mapped_column(Integer, index=True)
    iconType = mapped_column(String, index=True)
    iconUrl = mapped_column(String, index=True)
    url = mapped_column(String, index=True)
    alg = mapped_column(String, index=True)

@declared_attr
def tablename(cls) -> str:
    return cls.name.lower()