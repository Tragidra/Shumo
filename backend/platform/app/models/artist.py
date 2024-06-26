from typing import List

from sqlalchemy import Column, DateTime, Integer, func, String, Boolean, ForeignKey
from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy.orm import relationship, mapped_column, Mapped

from backend.platform.app.models.base_class import Base


class Artists_details(Base):
    __tablename__ = 'artists_details'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String, index=True)
    picId: Mapped[int] = mapped_column(Integer, index=True)
    img1v1Id: Mapped[int] = mapped_column(Integer, index=True)
    briefDesc: Mapped[str] = mapped_column(String, index=True)
    img1v1Id_str: Mapped[str] = mapped_column(String, index=True)
    img1v1Url: Mapped[str] = mapped_column(String, index=True)
    musicSize: Mapped[int] = mapped_column(Integer, index=True)
    picid_str: Mapped[str] = mapped_column(String, index=True)
    picUrl: Mapped[str] = mapped_column(String, index=True)
    topicPerson: Mapped[int] = mapped_column(Integer, index=True)
    trans: Mapped[str] = mapped_column(String, index=True)
    transNames: Mapped[str] = mapped_column(String, index=True)
    alias_id: Mapped[int] = mapped_column(ForeignKey('artists_details_alias.id', ondelete="SET NULL"),
                                          nullable=False)

    alias: Mapped[List["Artists_alias"]] = relationship(back_populates="artists_details", cascade="save-update")


class Artists_alias(Base):
    __tablename__ = 'artists_alias'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(Integer, nullable=False)
    artists_details_id: Mapped[int] = mapped_column(ForeignKey('artists_details.id', ondelete='CASCADE'),
                                                    nullable=False)
    artists_outsides_id: Mapped[int] = mapped_column(ForeignKey('artists_outsides.id', ondelete='CASCADE'),
                                                     nullable=False)
    artists_details: Mapped[List["Artists_details"]] = relationship(back_populates="alias")
    artists_outsides: Mapped[List["Artists_outsides"]] = relationship(back_populates="alias")


class Artists_for_search(Base):
    __tablename__ = 'artists_for_search'

    id: Mapped[int] = mapped_column(primary_key=True)
    accountId: Mapped[int] = mapped_column(Integer, index=True)
    albumSize: Mapped[int] = mapped_column(Integer, index=True)

    artists_details: Mapped[List["Artists_details"]] = relationship(back_populates="artists_details",
                                                                    cascade="save-update")
    artists_outsides: Mapped[List["Artists_outsides"]] = relationship(back_populates="artists_outsides",
                                                                      cascade="save-update")


@property
def get_artists_details(self):
    return self._artists_details


class Artists_outsides(Base):
    __tablename__ = 'artists_outsides'

    id: Mapped[int] = mapped_column(primary_key=True)
    accountId: Mapped[int] = mapped_column(Integer, index=True)
    albumSize: Mapped[int] = mapped_column(Integer, index=True)
    briefDesc = mapped_column(String, index=True)
    followed = mapped_column(Boolean, index=True)
    img1v1Id = mapped_column(Integer, index=True)
    img1v1Id_str = mapped_column(String, index=True)
    img1v1Url = mapped_column(String, index=True)
    musicSize = mapped_column(Integer, index=True)
    name = mapped_column(String, index=True)
    picId = mapped_column(Integer, index=True)
    picid_str = mapped_column(String, index=True)
    picUrl = mapped_column(String, index=True)
    topicPerson = mapped_column(Integer, index=True)
    trans = mapped_column(String, index=True)

    artists_alias_id: Mapped[int] = mapped_column(ForeignKey('artists_alias.id', ondelete="SET NULL"),
                                                  nullable=False)
    alias: Mapped[List["Artists_alias"]] = relationship(back_populates="artists_outsides", cascade="save-update")
