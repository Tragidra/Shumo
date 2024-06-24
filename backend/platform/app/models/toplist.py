from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import mapped_column

from backend.platform.app.models.base_class import Base


class Toplist(Base):
    __tablename__ = 'toplist'

    subscribers = mapped_column(Integer, index=True) #Доделать - Users
    subscribed = mapped_column(Boolean, index=True)
    creator = mapped_column(String, index=True) #Доделать - Users
    artists = mapped_column(String, index=True) #Доделать
    tracks = mapped_column(String, index=True) #Доделать
    updateFrequency = mapped_column(String, index=True)
    backgroundCoverId = mapped_column(Integer, index=True)
    backgroundCoverUrl = mapped_column(String, index=True)
    titleImage = mapped_column(Integer, index=True)
    coverText = mapped_column(String, index=True)
    titleImageUrl = mapped_column(String, index=True)
    coverImageUrl = mapped_column(String, index=True)
    englishTitle = mapped_column(String, index=True)
    opRecommend = mapped_column(Boolean, index=True)
    recommendInfo = mapped_column(String, index=True) #Доделать
    socialPlaylistCover = mapped_column(String, index=True) #Доделать
    tsSongCount = mapped_column(Integer, index=True)
    highQuality = mapped_column(Boolean, index=True)
    specialType = mapped_column(Integer, index=True)
    coverImgId = mapped_column(Integer, index=True)
    newImported = mapped_column(Boolean, index=True)
    anonimus = mapped_column(Boolean, index=True)
    updateTime = mapped_column(Integer, index=True)
    coverImgUrl = mapped_column(String, index=True)
    trackCount = mapped_column(Integer, index=True)
    commentThreadId = mapped_column(String, index=True)
    trackUpdateTime = mapped_column(Integer, index=True)
    totalDuration = mapped_column(Integer, index=True)
    playCount = mapped_column(Integer, index=True)
    privacy = mapped_column(Integer, index=True)
    adType = mapped_column(Integer, index=True)
    subscribedCount = mapped_column(Integer, index=True)
    cloudTrackCount = mapped_column(Integer, index=True)
    createTime = mapped_column(Integer, index=True)
    ordered = mapped_column(Boolean, index=True)
    description = mapped_column(String, index=True)
    status = mapped_column(Integer, index=True)
    tags = mapped_column(Integer, index=True) #Доделать
    userId = mapped_column(Integer, index=True) #Доделать
    name = mapped_column(String, index=True)
    ToplistType = mapped_column(String, index=True)