from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import mapped_column

from backend.platform.app.models.base_class import Base


class Playlist(Base):
    __tablename__ = 'playlist'

    type = mapped_column(Integer, index=True)
    name = mapped_column(String, index=True)
    copywriter = mapped_column(String, index=True)
    picurl = mapped_column(String, index=True)
    canDislike = mapped_column(Boolean, index=True)
    trackNumberUpdateTime = mapped_column(Integer, index=True)
    playCount = mapped_column(Integer, index=True)
    trackCount = mapped_column(Integer, index=True)
    highQuality = mapped_column(Boolean, index=True)
    alg = mapped_column(String, index=True)


class Playlist_for_search(Base):
    __tablename__ = 'playlist_for_search'

    name = mapped_column(String, index=True)
    trackNumberUpdateTime = mapped_column(Integer, index=True)
    status = mapped_column(Integer, index=True)
    userId = mapped_column(Integer, index=True)
    createTime = mapped_column(Integer, index=True)
    updateTime = mapped_column(Integer, index=True)
    subscribedCount = mapped_column(Integer, index=True)
    trackCount = mapped_column(Integer, index=True)
    cloudTrackCount = mapped_column(Integer, index=True)
    coverImgUrl = mapped_column(String, index=True)
    iconImgUrl = mapped_column(String, index=True)
    coverImgId = mapped_column(Integer, index=True)
    description = mapped_column(String, index=True)
    playlists_tags_for_search = mapped_column(Integer, index=True) #Доделать
    playCount = mapped_column(Integer, index=True)
    trackUpdateTime = mapped_column(Integer, index=True)
    specialType = mapped_column(Integer, index=True)
    totalDuration = mapped_column(Integer, index=True)
    creators = mapped_column(Integer, index=True) #Доделать
    tracks = mapped_column(Integer, index=True) #Доделать
    subscribers = mapped_column(Integer, index=True) #Доделать
    subscribed = mapped_column(Boolean, index=True) #Доделать
    commentThreadId = mapped_column(String, index=True)
    newImported = mapped_column(Boolean, index=True)
    adType = mapped_column(Integer, index=True)
    highQuality = mapped_column(Boolean, index=True)
    privacy = mapped_column(Integer, index=True)
    ordered = mapped_column(Boolean, index=True)
    anonimus = mapped_column(Boolean, index=True)
    coverStatus = mapped_column(String, index=True)
    recommendInfo = mapped_column(String, index=True) #Доделать
    socialPlaylistCover = mapped_column(String, index=True) #Доделать
    recommendText = mapped_column(String, index=True) #Доделать
    coverText = mapped_column(String, index=True) #Доделать
    relateResId = mapped_column(Integer, index=True) #Доделать
    relateResType = mapped_column(String, index=True) #Доделать
    tsSongCount = mapped_column(Integer, index=True)
    shareCount = mapped_column(Integer, index=True)
    alg = mapped_column(String, index=True)
    commentCount = mapped_column(Integer, index=True)


class Playlist_tags(Base):
    __tablename__ = 'playlists_tags'

    name = mapped_column(String, index=True)
    type = mapped_column(Integer, index=True)
    category = mapped_column(Integer, index=True)
    hot = mapped_column(Boolean, index=True)


class Playlist_tags_for_search(Base):
    __tablename__ = 'playlists_tags_for_search'

    name = mapped_column(String, index=True)