from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import mapped_column

from backend.platform.app.models.base_class import Base


class Albums(Base):
    __tablename__ = 'hot_request'

    name = mapped_column(String, index=True)
    type = mapped_column(String, index=True)
    picId = mapped_column(Integer, index=True) #Доделать
    size = mapped_column(Integer, index=True)
    blurPicUrl = mapped_column(String, index=True)
    companyId = mapped_column(Integer, index=True)
    pic = mapped_column(Integer, index=True)
    picUrl = mapped_column(String, index=True)
    publishTime = mapped_column(Integer, index=True)
    description = mapped_column(String, index=True)
    tags = mapped_column(String, index=True)
    company = mapped_column(String, index=True)
    briefDesc = mapped_column(String, index=True)
    artist_detail = mapped_column(String, index=True) #Доделать
    songs = mapped_column(String, index=True) #Доделать
    alias = mapped_column(String, index=True)
    status = mapped_column(Integer, index=True)
    paid = mapped_column(Boolean, index=True)
    onSale = mapped_column(Boolean, index=True)
    picId_str = mapped_column(String, index=True)

