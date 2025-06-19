from fastapi import FastAPI
from router import blog_get
from router import blog_post
from router import user
from router import article
from db import models
from db.database import engine

# App sirve para definir nuestros endpoints pero también para correr el servidor de uvicorn
# Cuando definimos un endpoint, por ejemplo @app.get('/'),debajo; definimos una función que se ejecutará cuando se haga una petición a esa ruta especifica

app = FastAPI()
app.include_router(user.router)
app.include_router(article.router)
app.include_router(blog_get.router)
app.include_router(blog_post.router)

@app.get('/')
def index():
  return { "message": 'Hello World'}

# Creamos la base de datos
# esto crea un archivo en la raiz llamado fastapi-practice.db
# pero si el archivo ya existe, no se sobrescribe
models.Base.metadata.create_all(engine)
