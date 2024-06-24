from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy.orm import mapped_column

from backend.platform.app.models.base_class import Base


class Artists_details(Base):
    __tablename__ = 'artists_details'

    imageUrl = mapped_column(String, index=True)
    targetId = mapped_column(Integer, index=True)
    adid = mapped_column(Integer, index=True) #Доделать
    targetType = mapped_column(Integer, index=True)
    titleColor = mapped_column(String, index=True)
    typeTitle = mapped_column(String, index=True)
    url = mapped_column(String, index=True)
    exclusive = mapped_column(Boolean, index=True) #Доделать
    monitorImpress = mapped_column(Integer, index=True) #Доделать
    monitorClick = mapped_column(Integer, index=True) #Доделать
    monitorType = mapped_column(Integer, index=True) #Доделать
    monitorImpressList = mapped_column(Integer, index=True) #Доделать
    monitorClickList = mapped_column(Integer, index=True) #Доделать
    monitorBlackList = mapped_column(Integer, index=True) #Доделать
    extMonitor = mapped_column(Integer, index=True) #Доделать
    extMonitorInfo = mapped_column(Integer, index=True) #Доделать
    adSource = mapped_column(Integer, index=True) #Доделать
    adLocation = mapped_column(Integer, index=True) #Доделать
    adDispatchJson = mapped_column(Integer, index=True) #Доделать
    encodeId = mapped_column(Integer, index=True)
    program = mapped_column(String, index=True) #Доделать
    event = mapped_column(Integer, index=True)  #Доделать
    video = mapped_column(String, index=True)  #Доделать
    song = mapped_column(String, index=True)  #Доделать
    scm = mapped_column(String, index=True)
    bannerBizSize = mapped_column(String, index=True)