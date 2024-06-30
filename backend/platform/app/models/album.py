from typing import List

from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship

from backend.platform.app.models.base_class import Base
from backend.platform.app.models.songs import Songs
from backend.platform.app.schemas.artist import Artists_Details


class Albums(Base):
    __tablename__ = 'albums'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String, index=True)
    type: Mapped[str] = mapped_column(String, index=True)
    picId: Mapped[int] = mapped_column(Integer, index=True)
    size: Mapped[int] = mapped_column(Integer, index=True)
    blurPicUrl: Mapped[str] = mapped_column(String, index=True)
    companyId: Mapped[int] = mapped_column(Integer, index=True)
    pic: Mapped[int] = mapped_column(Integer, index=True)
    picUrl: Mapped[str] = mapped_column(String, index=True)
    publishTime: Mapped[int] = mapped_column(Integer, index=True)
    description: Mapped[str] = mapped_column(String, index=True)
    company: Mapped[str] = mapped_column(String, index=True)
    briefDesc: Mapped[str] = mapped_column(String, index=True)
    alias: Mapped[str] = mapped_column(String, index=True)
    status: Mapped[int] = mapped_column(Integer, index=True)
    paid: Mapped[bool] = mapped_column(Boolean, index=True)
    onSale: Mapped[bool] = mapped_column(Boolean, index=True)
    picId_str: Mapped[str] = mapped_column(String, index=True)
    author: Mapped[int] = mapped_column(Integer, index=True)

    artist: Mapped[List["Artists_Details"]] = relationship(back_populates="albums", cascade="save-update")
    albums_tags_by_albums: Mapped["Albums_tags_by_albums"] = relationship(back_populates="albums")
    songs: Mapped[List["Songs"]] = relationship(back_populates="albums", cascade="save-update")


class Albums_tags(Base):
    __tablename__ = 'albums_tags'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String, index=True)

    albums: Mapped[List["Albums"]] = relationship(back_populates="albums_tags")
    albums_tags_by_albums: Mapped["Albums"] = relationship(back_populates="albums_tags")


class Albums_tags_by_albums(Base):
    __tablename__ = 'albums_tags_by_albums'

    id: Mapped[int] = mapped_column(primary_key=True)
    albums_id: Mapped[int] = mapped_column(ForeignKey('albums.id'), nullable=False)
    albums_tags_id: Mapped[int] = mapped_column(ForeignKey('albums_tags.id'), nullable=False)

    albums_tags: Mapped["Albums_tags"] = relationship(back_populates="albums_tags_by_albums")
    albums: Mapped["Albums"] = relationship(back_populates="albums_tags_by_albums")