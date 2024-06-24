from typing import Optional
from pydantic import BaseModel, typing, Field, ConfigDict


class Hot_ReauestsBase(BaseModel):
    searchWord: Optional[str]
    score: Optional[int]
    content: Optional[str]
    source: Optional[int]
    iconType: Optional[str]
    iconUrl: Optional[str]
    url: Optional[str]
    alg: Optional[str]


class Hot_Reauests(Hot_ReauestsBase):
    id: int

    class Config:
        model_config = ConfigDict(from_attributes=True)
        metadata: typing.Dict[str, str] = Field(alias='metadata_')


class Hot_ReauestsCreate(Hot_ReauestsBase):
    pass


class Hot_ReauestsUpdate(Hot_ReauestsBase):
    searchWord: Optional[str]
    score: Optional[str]
    content: Optional[str]
    source: Optional[str]
    iconType: Optional[str]
    iconUrl: Optional[str]
    url: Optional[str]
    alg: Optional[str]
