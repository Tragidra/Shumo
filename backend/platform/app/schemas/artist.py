from typing import Optional
from pydantic import BaseModel, typing, Field, ConfigDict


class Artists_DetailsBase(BaseModel):
    name: str
    picId: int
    img1v1Id: int
    briefDesc: str
    img1v1Id_str: str
    img1v1Url: str
    musicSize: int
    picid_str: str
    picUrl: str
    topicPerson: int
    trans: str
    transNames: str
    alias: str


class Artists_Details(Artists_DetailsBase):
    id: int

    class Config:
        model_config = ConfigDict(from_attributes=True)
        metadata: typing.Dict[str, str] = Field(alias='metadata_')


class Artists_DetailsCreate(Artists_DetailsBase):
    pass


class Artists_DetailsUpdate(BaseModel):
    id: [int]
    name: [str]
    picId: Optional[int]
    img1v1Id: Optional[int]
    briefDesc: Optional[str]
    img1v1Id_str: Optional[str]
    img1v1Url: Optional[str]
    musicSize: Optional[int]
    picid_str: Optional[str]
    picUrl: Optional[str]
    topicPerson: Optional[int]
    trans: Optional[str]
    transNames: Optional[str]
    alias: Optional[str]


class Artists_for_searchBase(BaseModel):
    accountId = Column(Integer, index=True)
    albumSize = Column(Integer, index=True)
    artists_details_id = mapped_column(ForeignKey('artists_details.id'), nullable=False)