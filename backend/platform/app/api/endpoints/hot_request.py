from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ...schemas import hot_reauests as hot_requests_schemas
from ...crud import hot_request as hot_request_crud
from ...api import deps

router = APIRouter()


@router.post("/search/hot/detail", response_model=hot_requests_schemas.Hot_Reauests)
def create_hot_request(hot_request: hot_requests_schemas.Hot_ReauestsCreate, db: Session = Depends(deps.get_db)):
    res = hot_request_crud.create_hot_request(db=db, hot_request=hot_request)
    return res


@router.get("/search/hot/detail", response_model=hot_requests_schemas.Hot_Reauests)
def read_hot_request(db: Session = Depends(deps.get_db)):
    hot_requests = hot_request_crud.get_hot_requests(db=db)
    if hot_requests is None:
        raise HTTPException(status_code=404, detail="Горячие запросы не найдены")
    return hot_requests


@router.put("/{hot_request_id}", response_model=hot_requests_schemas.Hot_Reauests)
def update_user(hot_request_id: int, hot_request_up: hot_requests_schemas.Hot_ReauestsUpdate,
                db: Session = Depends(deps.get_db)):
    hot_request = hot_request_crud.get_hot_request(db=db, hot_request_id=hot_request_id)
    if hot_request is None:
        raise HTTPException(status_code=404, detail="Горячий запрос не найден")
    hot_request = hot_request_crud.update_hot_request(db=db, hot_request_update=hot_request_up)
    return hot_request


@router.delete("/{hot_request_id}", response_model=hot_requests_schemas.Hot_Reauests)
def delete_user(hot_request_id: int, db: Session = Depends(deps.get_db)):
    hot_request = hot_request_crud.get_hot_request(db=db, hot_request_id=hot_request_id)
    if hot_request is None:
        raise HTTPException(status_code=404, detail="User not found")
    hot_request = hot_request_crud.delete_hot_request(db=db, hot_request_id=hot_request_id)
    return hot_request
