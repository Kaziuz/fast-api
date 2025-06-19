# Este archivo se encarga de poner los datos que 
# llegan del front en nuestra base de datos 

from sqlalchemy.orm.session import Session
from schemas import UserBase
from db.models import DbUser
from db.hash import Hash
from fastapi import HTTPException, status

def create_user(db: Session, request: UserBase):
  new_user = DbUser(
    username = request.username,
    email = request.email,
    password = Hash.bcrypt(request.password)
  )
  
  db.add(new_user) # Agregamos aquí un nuevo usuario a la base de datos
  db.commit() # Guardamos la operación anterior en la base de datos
  db.refresh(new_user) # Actualizamos el objeto new_user con los datos nuevos porque deben de generarse unos datos automáticos (primarykey)
  return new_user

def get_all_users(db: Session):
  return db.query(DbUser).all()

def get_user(db: Session, id: int):
  user = db.query(DbUser).filter(DbUser.id == id).first()
  # Si el id no existe, lanza una excepción
  if not user:
    raise HTTPException(
      status_code=status.HTTP_404_NOT_FOUND,
      detail=f"User with id: {id} not found"
    )
  return user

def update_user(db: Session, id:int, request: UserBase):
  user = db.query(DbUser).filter(DbUser.id == id)
  # Si el id no existe, lanza una excepción
  if not user.first():
    raise HTTPException(
      status_code=status.HTTP_404_NOT_FOUND,
      detail=f"User with id: {id} not found"
    )
  user.update({
    DbUser.username: request.username,
    DbUser.email: request.email,
    DbUser.password: Hash.bcrypt(request.password)
  })
  db.commit()
  return 'OK'

def delete_user(db: Session, id: int):
  user = db.query(DbUser).filter(DbUser.id == id)
  # Si el id no existe, lanza una excepción
  if not user.first():
    raise HTTPException(
      status_code=status.HTTP_404_NOT_FOUND,
      detail=f"User with id: {id} not found"
    )
  db.delete(user)
  db.commit()
  return 'OK'