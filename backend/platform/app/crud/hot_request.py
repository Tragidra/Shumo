from sqlalchemy.orm import Session
from ..models.hot_request import Hot_request
from ..schemas.hot_reauests import Hot_ReauestsCreate, Hot_ReauestsUpdate


def get_hot_request(db: Session, hot_request_id: int):
    return db.query(Hot_request).filter(Hot_request.id == hot_request_id).first()


def get_hot_requests(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Hot_request).offset(skip).limit(limit).all()


def create_hot_request(db: Session, hot_request: Hot_ReauestsCreate):
    db_hot_request = hot_request(searchWord=hot_request.searchWord, score=hot_request.score,
                                 content=hot_request.content,
                                 source=hot_request.source, iconType=hot_request.iconType, iconUrl=hot_request.iconUrl,
                                 url=hot_request.url, alg=hot_request.alg)
    db.add(db_hot_request)
    db.commit()
    db.refresh(db_hot_request)
    return db_hot_request


def update_hot_request(db: Session, hot_request_update: Hot_ReauestsUpdate):
    db_hot_request = db.query(Hot_request).filter(Hot_request.id == hot_request_update.id).one_or_none()

    for key, value in hot_request_update.dict().items():
        setattr(db_hot_request, key, value) if value else None

    db.commit()
    db.refresh(db_hot_request)
    return db_hot_request


def delete_hot_request(db: Session, hot_request_id: int):
    hot_request = db.query(Hot_request).filter(Hot_request.id == hot_request_id).first()
    db.delete(hot_request)
    db.commit()
    return hot_request
