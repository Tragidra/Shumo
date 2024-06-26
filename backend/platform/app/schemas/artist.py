from typing import Optional
from pydantic import BaseModel, typing, Field, ConfigDict


class Artists_aliasBase(BaseModel):
    name: str
    artists_details_id: Optional[int]
    artists_outsides_id: Optional[int]


class Artists_alias(Artists_aliasBase):
    id: int


class Artists_aliasCreate(Artists_aliasBase):
    pass


class Artists_aliasUpdate(Artists_aliasBase):
    name: Optional[str]
    artists_details_id: Optional[int]
    artists_outsides_id: Optional[int]


class Artists_DetailsBase(BaseModel):
    name: str
    picId: int
    img1v1Id: int
    briefDesc: Optional[str]
    img1v1Id_str: str
    img1v1Url: str
    musicSize: int
    picid_str: str
    picUrl: str
    topicPerson: int
    trans: Optional[str]
    transNames: str
    alias: str
    alias_id: int


class Artists_Details(Artists_DetailsBase):
    id: int
    alias: list[Artists_alias] = []

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
    alias_id: Optional[int]

