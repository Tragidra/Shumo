from sqlalchemy import Column, Boolean, Integer, String
from sqlalchemy.orm import mapped_column

from .base_class import Base


class Songs(Base):
    name = mapped_column(String, unique=True, index=True)
    login = mapped_column(String, unique=True, index=True)
    pst = mapped_column(Integer, unique=True, index=True)
    t = mapped_column(Integer, unique=True, index=True)
    ar = mapped_column(String, unique=True, index=True) #Доделать Array
    allia = mapped_column(String, unique=True, index=True) #Доделать
    pop = mapped_column(Integer, unique=True, index=True)
    st = mapped_column(Integer, unique=True, index=True)
    rt = mapped_column(String, unique=True, index=True)
    fee = mapped_column(Integer, unique=True, index=True)
    v = mapped_column(Integer, unique=True, index=True)
    crbt = mapped_column(Integer, unique=True, index=True) #Доделать
    cf = mapped_column(String, unique=True, index=True)
    al = mapped_column(Integer, unique=True, index=True) #Доделать
    dt = mapped_column(Integer, unique=True, index=True) #Доделать
    h = mapped_column(Integer, unique=True, index=True) #Доделать
    m = mapped_column(Integer, unique=True, index=True) #Доделать
    l = mapped_column(Integer, unique=True, index=True) #Доделать
    sq = mapped_column(Integer, unique=True, index=True) #Доделать
    hr = mapped_column(Integer, unique=True, index=True) #Доделать
    a = mapped_column(Integer, unique=True, index=True) #Доделать
    cd = mapped_column(String, unique=True, index=True)
    no = mapped_column(Integer, unique=True, index=True)
    rtUrl = mapped_column(Integer, unique=True, index=True) #Доделать
    ftype = mapped_column(Integer, unique=True, index=True)
    rtUrls = mapped_column(Integer, unique=True, index=True)#Доделать
    djId = mapped_column(Integer, unique=True, index=True) #Доделать
    copyright = mapped_column(Integer, unique=True, index=True)#Доделать
    s_id = mapped_column(Integer, unique=True, index=True)#Доделать
    mark = mapped_column(Integer, unique=True, index=True)
    originCoverType = mapped_column(Integer, unique=True, index=True)
    originSongSimpleData = mapped_column(Integer, unique=True, index=True) #Доделать
    tagPicList = mapped_column(Integer, unique=True, index=True)#Доделать
    resourceState = mapped_column(Boolean, unique=True, index=True)
    version = mapped_column(Integer, unique=True, index=True)
    songJumpInfo = mapped_column(Integer, unique=True, index=True)#Доделать
    entertainmentTags = mapped_column(Integer, unique=True, index=True)#Доделать
    awardTags = mapped_column(Integer, unique=True, index=True)#Доделать
    single = mapped_column(Integer, unique=True, index=True)
    mv = mapped_column(Integer, unique=True, index=True)
    mst = mapped_column(Integer, unique=True, index=True)
    rtype = mapped_column(Integer, unique=True, index=True)
    cp = mapped_column(Integer, unique=True, index=True)
    rurl = mapped_column(Integer, unique=True, index=True)#Доделать
    publishTime = mapped_column(Integer, unique=True, index=True)


class Origin_song_simple_data(Base):
    songId = mapped_column(Integer, unique=True, index=True) #Доделать
    name = mapped_column(String, unique=True, index=True)
    artists_in_toplist = mapped_column(Integer, unique=True, index=True)#Доделать
    albumMeta = mapped_column(Integer, unique=True, index=True) #Доделать


class Album_meta(Base):
    name = mapped_column(String, unique=True, index=True)


class Artists_in_toplist(Base):
    name = mapped_column(String, unique=True, index=True)


class Ar(Base):
    name = mapped_column(String, unique=True, index=True)
    tns = mapped_column(String, unique=True, index=True) #Доделать
    allias = mapped_column(String, unique=True, index=True) #Доделать

class Al(Base):
    name = mapped_column(String, unique=True, index=True)
    picUrl = mapped_column(String, unique=True, index=True)
    tns = mapped_column(String, unique=True, index=True) #Доделать
    pic_str = mapped_column(String, unique=True, index=True)
    pic = mapped_column(Integer, unique=True, index=True)


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