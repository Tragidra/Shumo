from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ...schemas import user as user_schemas
from ...crud import user as user_crud
from ...api import deps
from ...core.security import create_access_token, verify_password

router = APIRouter()


@router.post("/", response_model=user_schemas.User)
def create_user(user_in: user_schemas.UserCreate, db: Session = Depends(deps.get_db)):
    user = user_crud.create_user(db=db, user=user_in)
    return user


@router.get("/{user_id}", response_model=user_schemas.User)
def read_user(user_id: int, db: Session = Depends(deps.get_db)):
    user = user_crud.get_user(db=db, user_id=user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.put("/{user_id}", response_model=user_schemas.User)
def update_user(user_id: int, user_in: user_schemas.UserUpdate, db: Session = Depends(deps.get_db)):
    user = user_crud.get_user(db=db, user_id=user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    user = user_crud.update_user(db=db, db_user=user, user_update=user_in)
    return user


@router.delete("/{user_id}", response_model=user_schemas.User)
def delete_user(user_id: int, db: Session = Depends(deps.get_db)):
    user = user_crud.get_user(db=db, user_id=user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    user = user_crud.delete_user(db=db, user_id=user_id)
    return user


@router.post("/token", response_model=user_schemas.Token)
def login_for_access_token(form_data: user_schemas.LoginForm, db: Session = Depends(deps.get_db)):
    user = user_crud.authenticate_user(db, email=form_data.email, password=form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}
