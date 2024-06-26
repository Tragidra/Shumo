from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped

from backend.platform.app.models.base_class import Base


class Albums(Base):
    __tablename__ = 'albums'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String, index=True)
    type: Mapped[str] = mapped_column(String, index=True)
    picId: Mapped[int] = mapped_column(Integer, index=True) #Доделать
    size: Mapped[int] = mapped_column(Integer, index=True)
    blurPicUrl: Mapped[str] = mapped_column(String, index=True)
    companyId: Mapped[int] = mapped_column(Integer, index=True)
    pic: Mapped[int] = mapped_column(Integer, index=True)
    picUrl: Mapped[str] = mapped_column(String, index=True)
    publishTime: Mapped[int] = mapped_column(Integer, index=True)
    description: Mapped[str] = mapped_column(String, index=True)
    company: Mapped[str] = mapped_column(String, index=True)
    briefDesc: Mapped[str] = mapped_column(String, index=True)
    artist_detail: Mapped[str] = mapped_column(String, index=True) #Доделать
    songs: Mapped[str] = mapped_column(String, index=True) #Доделать
    alias: Mapped[str] = mapped_column(String, index=True)
    status: Mapped[int] = mapped_column(Integer, index=True)
    paid: Mapped[bool] = mapped_column(Boolean, index=True)
    onSale: Mapped[bool] = mapped_column(Boolean, index=True)
    picId_str: Mapped[str] = mapped_column(String, index=True)
    tags_id: Mapped[int] = mapped_column(ForeignKey('artists_details_alias.id'), nullable=False)


class Albums_tags(Base):
    __tablename__ = 'albums_tags'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String, index=True)