from sqlalchemy import Column, Boolean, Integer, String
from sqlalchemy.orm import mapped_column

from .base_class import Base


class User(Base):
    login = mapped_column(String, unique=True, index=True)
    defaultAvatar = mapped_column(Boolean, unique=True, index=True)
    province = mapped_column(Integer, unique=True, index=True)
    authStatus = mapped_column(Boolean, unique=True, index=True, default=False) #Доделать
    accountStatus = mapped_column(Integer, unique=True, index=True)
    avatarUrl = mapped_column(String, unique=True, index=True)
    nickname = mapped_column(String, unique=True, index=True)
    followed = mapped_column(Boolean, unique=True)
    gender = mapped_column(Integer, unique=True, index=True)
    city = mapped_column(Integer, unique=True, index=True)
    birthday = mapped_column(Integer, unique=True, index=True)
    userType = mapped_column(Integer, unique=True, index=True)
    signature = mapped_column(String, unique=True, index=True)
    description = mapped_column(String, unique=True, index=True)
    detailDescription = mapped_column(String, unique=True, index=True)
    avatarImgId = mapped_column(Integer, unique=True, index=True)
    backgroundImgId = mapped_column(Integer, unique=True, index=True)
    backgroundUrl = mapped_column(String, unique=True, index=True)
    authority = mapped_column(Integer, unique=True, index=True)
    mutual = mapped_column(Boolean, unique=True, index=True)
    expertTags = mapped_column(Boolean, unique=True, index=True) #Доделать
    experts = mapped_column(Boolean, unique=True, index=True) #Доделать
    djStatus = mapped_column(Integer, unique=True, index=True)
    vipStatus = mapped_column(Integer, unique=True, index=True)
    remarkName = mapped_column(Boolean, unique=True, index=True) #Доделать
    authenticationTypes = mapped_column(Integer, unique=True, index=True)
    avatarDetail = mapped_column(Boolean, unique=True, index=True) #Доделать
    avatarImgIdStr = mapped_column(String, unique=True, index=True)
    backgroundImgIdStr = mapped_column(String, unique=True, index=True)
    anchor = mapped_column(Boolean, unique=True, index=True)
    hashed_password = mapped_column(String)

# class User_Other_Data(Base):
#    level
#    subcount
