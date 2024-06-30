from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy.orm import mapped_column

from backend.platform.app.models.base_class import Base


class Banners(Base):
    __tablename__ = 'banners'

    imageUrl = mapped_column(String, index=True)
    targetId = mapped_column(Integer, index=True)
    adid = mapped_column(Integer, index=True)
    targetType = mapped_column(Integer, index=True)
    titleColor = mapped_column(String, index=True)
    typeTitle = mapped_column(String, index=True)
    url = mapped_column(String, index=True)
    exclusive = mapped_column(Boolean, index=True)
    monitorImpress = mapped_column(Integer, index=True)
    monitorClick = mapped_column(Integer, index=True)
    monitorType = mapped_column(Integer, index=True)
    monitorImpressList = mapped_column(Integer, index=True)
    monitorClickList = mapped_column(Integer, index=True)
    monitorBlackList = mapped_column(Integer, index=True)
    extMonitor = mapped_column(Integer, index=True)
    extMonitorInfo = mapped_column(Integer, index=True)
    adSource = mapped_column(Integer, index=True)
    adLocation = mapped_column(Integer, index=True)
    adDispatchJson = mapped_column(Integer, index=True)
    encodeId = mapped_column(Integer, index=True)
    program = mapped_column(String, index=True) #Доделать
    event = mapped_column(String, index=True)  #Доделать
    video = mapped_column(String, index=True)  #Доделать
    song = mapped_column(String, index=True)  #Доделать
    scm = mapped_column(String, index=True)
    bannerBizSize = mapped_column(String, index=True)