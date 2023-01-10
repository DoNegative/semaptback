from sqlalchemy.orm import Session
from . import models, schemas

#Создание админа
def create_admin(db: Session, admin: schemas.Admin):
    fake_hashed_password = admin.password + "notreallyhashed"
    db_admin = models.Admin(email=admin.email, hashed_password=fake_hashed_password)
    db.add(db_admin)
    db.commit()
    db.refresh(db_admin)
    return db_admin

def get_admin_by_email(db: Session, email: str):
    return db.query(models.Admin).filter(models.Admin.email == email).first()

## Создание должностей
def create_position(db: Session, position: schemas.Position):
    db_position = models.Position(name = position.name, wage =position.wage)
    db.add(db_position)
    db.commit()
    db.refresh(db_position)
    return db_position

## Создание юзеров
def create_user(db: Session, user: schemas.UserPut):
    db_user = models.User(FIO = user.FIO  , email = user.email,  number_phone=user.number_phone, position_id=user.position_id)
    db.add(db_user)
    db.commit()
    db.refresh( db_user)
    return db_user

# Получние должностей
def get_positions(db: Session):
    return db.query(models.Position).all()

# Получние людей
def get_users(db: Session):
    users = db.query(models.User).all()
    arr = []
    for user in users:
        arr.append(schemas.User(id = user.id, FIO = user.FIO, email = user.email, number_phone=user.number_phone, position_id=user.position_id, position= schemas.PositionBase.func(db.query(models.Position).filter(models.Position.id == user.position_id).first())))
    return arr

#Обноволение  юзера
def put_user(db: Session, id:int, data):
    user = db.query(models.User).filter(models.User.id==id).first()
    print(user)
    for name, val in data.dict().items():
        setattr(user, name, val)
    db.commit()
    db.refresh(user)
    return user

#Удаление  юзера
def delete_user(db: Session, id:int):
    user = db.query(models.User).filter(models.User.id==id).first()
    db.delete(user)
    db.commit()
    return "Удалено"
# def get_user(db: Session, user_id: int):
#     return db.query(models.User).filter(models.User.id == user_id).first()

# def get_positions(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.Position).offset(skip).limit(limit).all()


# def create_user_position(db: Session, position: schemas.PositionCreate, user_id: int):
#     db_position = models.Position(**position.dict(), user_id=user_id)
#     db.add(db_position)
#     db.commit()
#     db.refresh(db_position)
#     return db_position