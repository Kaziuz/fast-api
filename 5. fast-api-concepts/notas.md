para correr la api
terminal: uvicorn main:app --reload

-------------------------------------------

para activar el entorno virtual
terminal: source fastapi-env/bin/activate

para crear el entorno virtual
terminal: python3 -m venv fastapi-env

para instalar el archivo requierements.txt
terminal: pip3 install -r requirements.txt

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

CAP 5: FastAPI Concepts

- Error handling: debemos manejar los errores que puedan ocurrir en el codigo

- Custom responses: hay varias formas de devolver datos al cliente

- Headers: necesitamos agregar headers al response para poder pasar informacion a nuestro api y desde nuestra api.

- Cookies: Como podemos pasar informacion de cookies, las cookies basicamente se usan para almacenar cierta informacion en el navegador del usuario, como un token de autenticacion, un id de usuario, etc, que 
necesitemos almacenar y recuperar en una fecha posterior.

- Form data: hablaremos sobre datos de formularios, a veces queremos que los datos sean enviados como datos de un
formulario HTML en lugar de JSON

Cors: agregar un poco de seguridad a nuestra api.
COrs significa compartir recursos entre origenes (dominios).

Normalmente a un sitio web que esta corriendo localmente, osea 
en la maquina que estamos usando, de forma predeterminada no se le permite acceder a recursos de la misma maquina, hasta que se especifique lo realmente.
esto quiere decir que si estamos corriendo una app react por ejemplo por el 
puerto 8000 y estamos corriendo un back por el puerto 8000  tambien, esta conexion no esta permitida de forma predeterminada.





