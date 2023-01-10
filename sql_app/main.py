from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import SessionLocal, engine
from fastapi.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app.add_middleware(
CORSMiddleware,
allow_origins=['*'],
allow_credentials=True,
allow_methods=['*'],
allow_headers=['*'],
)

#Создание админа
@app.post("/admins/", response_model=schemas.Admin)
def create_admin(admin: schemas.AdminCreate, db: Session = Depends(get_db)):
    db_admin = crud.get_admin_by_email(db, email=admin.email)
    if db_admin:
        raise HTTPException(status_code=200, detail="Email already registered")
    return crud.create_admin(db=db, admin=admin)

#Создание должностей
@app.post("/positions/", response_model=schemas.Position)
def create_position(position: schemas.PositionCreate, db: Session = Depends(get_db)):
    # db_position = crud.create_position(db, position=schemas.Position)
    return crud.create_position(db=db, position=position)

#Создание юзеров
@app.post("/users/", response_model=schemas.UserPut)
def create_user(user: schemas.UserPut, db: Session = Depends(get_db)):
    # db_position = crud.create_position(db, position=schemas.Position)
    return crud.create_user(db=db, user=user)


# Получение должностей
@app.get("/posiations/all", response_model=list[schemas.Position])
def read_positions(db: Session = Depends(get_db)):
    positions = crud.get_positions(db)
    return positions

# Получение юзеров
@app.get("/users/all", response_model=list[schemas.User])
def read_users(db: Session = Depends(get_db)):
    users = crud.get_users(db)
    return users

# Обновление юзеров
@app.put("/users/put/{id}", response_model=schemas.UserPut)
def read_users(id:int, user: schemas.UserPut, db: Session = Depends(get_db)):
    users = crud.put_user(db=db, id=id, data=user )
    return users

# Удаление юзера
@app.delete("/users/delete/{id}", response_model=str)
def delete_user(id:int, db: Session = Depends(get_db)):
    
    return crud.delete_user(db=db, id=id )

# @app.get("/users/{user_id}", response_model=schemas.User)
# def read_user(user_id: int, db: Session = Depends(get_db)):
#     db_user = crud.get_user(db, user_id=user_id)
#     if db_user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     return db_user


# @app.post("/users/{user_id}/positions/", response_model=schemas.Position)
# def create_position_for_user(
#     user_id: int, position: schemas.PositionCreate, db: Session = Depends(get_db)
# ):
#     return crud.create_user_position(db=db, position= position, user_id=user_id)


# @app.get("/positions/", response_model=list[schemas.Position])
# def read_positions(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     positions = crud.get_positions(db, skip=skip, limit=limit)
#     return positions