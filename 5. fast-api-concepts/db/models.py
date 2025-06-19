# El modelo es el tipo de datos que queremos
# almacenar en la base de datos

# SIEMPRE QUE SE HAGA UN CAMBIO AQUI
# SE DEBE BORRAR LA BASE DE DATOS 'fastapi-practice.db' Y VOLVER A EJECUTAR EL SERVER

# back_populates: es una propiedad que se usa para establecer una relación bidireccional entre dos objetos
# en este caso: usuario.items o articulo.user

# https://docs.sqlalchemy.org/en/20/orm/basic_relationships.html#declarative-vs-imperative-forms
# relationship: función que se utiliza para establecer una relación entre dos objetos, en este caso se usa de modo declarativo
# porque se le pasa el nombre de la tabla que se quiere relacionar

from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String, Boolean
from db.database import Base
from sqlalchemy import Column
from sqlalchemy.orm import relationship

class DbUser(Base):
  __tablename__ = 'users'
  id = Column(Integer, primary_key=True, index=True) # el Index crea un indice en la tabla
  username = Column(String)
  email = Column(String)
  password = Column(String)
  items = relationship('DbArticle', back_populates='user') # Un usuario puede tener múltiples artículos

class DbArticle(Base):
  __tablename__ = 'articles'
  id = Column(Integer, primary_key=True, index=True)
  title = Column(String)
  content = Column(String)
  published = Column(Boolean)
  user_id = Column(Integer, ForeignKey('users.id')) # Cada artículo pertenece a un usuario
  user = relationship('DbUser', back_populates='items')
