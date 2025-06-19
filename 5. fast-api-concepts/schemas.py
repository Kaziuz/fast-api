# En los esquemas estan relacionados los tipos de datos
# de los usuarios
# Un schema es un tipo de datos que se utiliza
# para definir la estructura y validaciones
# de los datos que se desean enviar/recibir
# a un endpoint
# RESUMEN: un schema define la estructura
# esperada de los datos

from pydantic import BaseModel
from typing import List

# Article esta dentro de la class UserDisplay
class Article(BaseModel):
  title: str
  content: str
  published: bool
  # class Config(): from_attributes = True
  # se usa para configurar opciones específicas relacionadas con el
  # comportamiento del modelo
  class Config():
    from_attributes = True

# Estructura de como se deben de recibir los datos desde el front
class UserBase(BaseModel):
  username: str
  email: str
  password: str
  
# Estructura de como se deben de enviar los datos al front
# una vez almacenados en la base de datos
class UserDisplay(BaseModel):
  username: str
  email: str
  items: List[Article] = []
  class Config():
    from_attributes = True

# User esta dentro de la class ArticleDisplay
class User(BaseModel):
  id: int
  username: str
  class Config():
    from_attributes = True

# como se deben de recibir los datos desde el front
class ArticleBase(BaseModel):
  title: str
  content: str
  published: bool
  creator_id: int
  
# como se envían los datos al front una vez almacenados en la base de datos
class ArticleDisplay(BaseModel):
  title: str
  content: str
  published: bool
  user: User
  class Config():
    from_attributes= True