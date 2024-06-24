from sqlalchemy import Column, DateTime, Integer, func, String, Boolean, ForeignKey
from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy.orm import relationship, mapped_column

from backend.platform.app.models.base_class import Base


class Artists_details(Base):
    __tablename__ = 'artists_details'

    name = mapped_column(String, index=True)
    picId = mapped_column(Integer, index=True)
    img1v1Id = mapped_column(Integer, index=True)
    briefDesc = mapped_column(String, index=True)
    img1v1Id_str = mapped_column(String, index=True)
    img1v1Url = mapped_column(String, index=True)
    musicSize = mapped_column(Integer, index=True)
    picid_str = mapped_column(String, index=True)
    picUrl = mapped_column(String, index=True)
    topicPerson = mapped_column(Integer, index=True)
    trans = mapped_column(String, index=True)
    transNames = mapped_column(String, index=True)
    alias = mapped_column(String, index=True)


class Artists_for_search(Base):
    __tablename__ = 'artists_for_search'

    accountId = mapped_column(Integer, index=True)
    albumSize = mapped_column(Integer, index=True)
    artists_details_id = mapped_column(ForeignKey('artists_details.id'), nullable=False)

    artists_details = relationship(back_populates="Artists_Details", ondelete='', cascade="save-update")


@property
def get_artists_details(self):
    return self._artists_details


class Artists_outsides(Base):
    __tablename__ = 'artists_outsides'

    accountId = mapped_column(Integer, index=True)
    albumSize = mapped_column(Integer, index=True)
    alias = mapped_column(String, index=True)
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
