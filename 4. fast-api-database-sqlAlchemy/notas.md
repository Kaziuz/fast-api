para correr la api
terminal: uvicorn main:app --reload

-------------------------------------------

para activar el entorno virtual
terminal: source fastapi-env/bin/activate

para crear el entorno virtual
terminal: python3 -m venv fastapi-env

para instalar el archivo requierements.txt
terminal: pip install -r requirements.txt

para ver si el entorno virtual esta activado
terminal: which python

para desactivar el entorno virtual
terminal: deactivate

-------------------------------------------
Documentacion

Definicion de la base de datos: database.py
Definicion de los modelos: models.py
Creación de la base de datos: main.py
Definicion de las rutas: router.py
Definicion de schema: schemas.py 
Deficion de la funcionalidad ORM: db_user.py
API functionality: user.py

COMO PASAMOS DE NADA A TENER UNA BASE DE DATOS CON UNA TABLA Y ALGUNOS DATOS EN ESA TABLA

1. import required libraries: sqlalchemy, passlib, bcrypt and others

2. Create a database definition and run it in main.py 
this line creates a database called fastapi-practice.db
models.Base.metadata.create_all(engine)

3. Create database models (tables): db/models.py

4. Create functionality to write to the database: db/db_user.py

5. Create schema: schemas.py
this is the structure of the data that we expect to receive from the front and show to the front
  - Data from user: UserBase
  - Response to user: UserDisplay

6. Create API operation: router/user.py
-------------------------------------------

