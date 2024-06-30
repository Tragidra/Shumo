from typing import List

from sqlalchemy import Column, Boolean, Integer, String, ForeignKey, Table
from sqlalchemy.orm import mapped_column, Mapped, relationship

from .album import Albums
from .artist import Artists_alias
from .base_class import Base

association_table_artists_alias_songs = Table(
    "association_table_artists_alias_songs",
    Base.metadata,
    Column("artists_alias", ForeignKey("artists_alias.id"), primary_key=True),
    Column("songs", ForeignKey("songs.id"), primary_key=True),
)


class Songs(Base):
    __tablename__ = 'songs'

    name = mapped_column(String, unique=True, index=True)
    pst = mapped_column(Integer, unique=True, index=True)
    t = mapped_column(Integer, unique=True, index=True)
    allia = mapped_column(String, unique=True, index=True)  #Доделать
    pop = mapped_column(Integer, unique=True, index=True)
    st = mapped_column(Integer, unique=True, index=True)
    rt = mapped_column(String, unique=True, index=True)
    fee = mapped_column(Integer, unique=True, index=True)
    v = mapped_column(Integer, unique=True, index=True)
    crbt = mapped_column(Integer, unique=True, index=True)  #Доделать
    cf = mapped_column(String, unique=True, index=True)
    dt = mapped_column(Integer, unique=True, index=True)  #Непонятно, целое число
    a = mapped_column(Integer, unique=True, index=True)  #Непонятно
    cd = mapped_column(String, unique=True, index=True)
    no = mapped_column(Integer, unique=True, index=True)
    rtUrl = mapped_column(Integer, unique=True, index=True)  #Доделать
    ftype = mapped_column(Integer, unique=True, index=True)
    rtUrls = mapped_column(Integer, unique=True, index=True)  #Доделать
    djId = mapped_column(Integer, unique=True, index=True)  #Доделать
    copyright = mapped_column(Integer, unique=True, index=True)  #Доделать
    s_id = mapped_column(Integer, unique=True, index=True)  #Доделать
    mark = mapped_column(Integer, unique=True, index=True)
    originCoverType = mapped_column(Integer, unique=True, index=True)
    originSongSimpleData = mapped_column(Integer, unique=True, index=True)  #Доделать
    tagPicList = mapped_column(Integer, unique=True, index=True)  #Доделать
    resourceState = mapped_column(Boolean, unique=True, index=True)
    version = mapped_column(Integer, unique=True, index=True)
    songJumpInfo = mapped_column(Integer, unique=True, index=True)  #Доделать
    entertainmentTags = mapped_column(Integer, unique=True, index=True)  #Доделать
    awardTags = mapped_column(Integer, unique=True, index=True)  #Доделать
    single = mapped_column(Integer, unique=True, index=True)
    mv = mapped_column(Integer, unique=True, index=True)
    mst = mapped_column(Integer, unique=True, index=True)
    rtype = mapped_column(Integer, unique=True, index=True)
    cp = mapped_column(Integer, unique=True, index=True)
    rurl = mapped_column(Integer, unique=True, index=True)  #Доделать
    publishTime = mapped_column(Integer, unique=True, index=True)
    h = mapped_column(Integer, unique=True, index=True)  # Доделать
    m = mapped_column(Integer, unique=True, index=True)  # Доделать
    l = mapped_column(Integer, unique=True, index=True)  # Доделать
    sq = mapped_column(Integer, unique=True, index=True)  # Доделать
    hr = mapped_column(Integer, unique=True, index=True)  # Доделать
    artist_allias_id = mapped_column(ForeignKey('artists_alias.id'), nullable=False)  #бывший ar
    albums_id = mapped_column(ForeignKey('albums.id'), nullable=False)  #бывший al

    alias: Mapped[List["Artists_alias"]] = relationship(secondary=association_table_artists_alias_songs,
                                                        back_populates="songs")
    albums: Mapped["Albums"] = relationship(back_populates="songs")


class Origin_song_simple_data(Base):
    songId = mapped_column(Integer, unique=True, index=True)  #Доделать
    name = mapped_column(String, unique=True, index=True)
    artists_in_toplist = mapped_column(Integer, unique=True, index=True)  #Доделать
    albumMeta = mapped_column(Integer, unique=True, index=True)  #Доделать


class Album_meta(Base):
    name = mapped_column(String, unique=True, index=True)


class Artists_in_toplist(Base):
    name = mapped_column(String, unique=True, index=True)


class Sq(Base):
    br = mapped_column(Integer, unique=True, index=True)
    fid = mapped_column(Integer, unique=True, index=True)
    size = mapped_column(Integer, unique=True, index=True)
    vd = mapped_column(Integer, unique=True, index=True)
    sr = mapped_column(Integer, unique=True, index=True)


class Hr(Base):
    br = mapped_column(Integer, unique=True, index=True)
    fid = mapped_column(Integer, unique=True, index=True)
    size = mapped_column(Integer, unique=True, index=True)
    vd = mapped_column(Integer, unique=True, index=True)
    sr = mapped_column(Integer, unique=True, index=True)


class H(Base):
    br = mapped_column(Integer, unique=True, index=True)
    fid = mapped_column(Integer, unique=True, index=True)
    size = mapped_column(Integer, unique=True, index=True)
    vd = mapped_column(Integer, unique=True, index=True)
    sr = mapped_column(Integer, unique=True, index=True)


class M(Base):
    br = mapped_column(Integer, unique=True, index=True)
    fid = mapped_column(Integer, unique=True, index=True)
    size = mapped_column(Integer, unique=True, index=True)
    vd = mapped_column(Integer, unique=True, index=True)
    sr = mapped_column(Integer, unique=True, index=True)


class L(Base):
    br = mapped_column(Integer, unique=True, index=True)
    fid = mapped_column(Integer, unique=True, index=True)
    size = mapped_column(Integer, unique=True, index=True)
    vd = mapped_column(Integer, unique=True, index=True)
    sr = mapped_column(Integer, unique=True, index=True)
