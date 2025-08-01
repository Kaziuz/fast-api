# Configuración básica para trabajar con SQLAlchemy, (Object-Relational Mapper) en Python
# que facilita la interacción con bases de datos relacionales

from sqlalchemy import create_engine # create_engine: Se utiliza para configurar la conexión con la base de datos
from sqlalchemy.ext.declarative import declarative_base # declarative_base: Crea una clase base a partir de la cual definimos las tablas de la base de datos como modelos en Python.
from sqlalchemy.orm import sessionmaker # sessionmaker: Crea sesiones que se utilizan para realizar operaciones (consultas, inserciones, actualizaciones) en la base de datos.
 
# En este enlace "sqlite:///./fastapi-practice.db"
# la palabra fastapi-practice especifica el nombre de la base de datos
# En la url esta sqlite, indicando que usaremos una base de datos SQLite
SQLALCHEMY_DATABASE_URL = "sqlite:///./fastapi-practice.db"

# create_engine: Definimos la conexión con la base de datos
# connect_args={"check_same_thread": False}: Es un parámetro específico de SQLite que desactiva la verificación del mismo hilo.
# SQLite, por defecto, no permite que diferentes hilos compartan la misma conexión. Este ajuste lo permite, lo cual es útil en
# aplicaciones multihilo como FastAPI

engine = create_engine(
  SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# sessionmaker: Creación de sesiones de base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# declarative_base: Proporciona una clase base de la cual derivan todos los modelos de la base de datos.
Base = declarative_base()

# Esta función (generadora por el yield) nos permitirá acceder a la base de datos para realizar algunas operaciones
# desde cualquier parte de nuestro código
def get_db():
  db = SessionLocal() # Creamos una sesión de base de datos
  try:
    # Proporcionamos la db
    yield db # Cedemos la session al contexto que la necesite
  finally:
    db.close() # Cerramos la sesión al finalizar