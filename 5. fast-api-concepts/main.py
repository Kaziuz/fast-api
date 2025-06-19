from fastapi import FastAPI, Request 
from router import blog_get
from router import blog_post
from router import user
from router import article
from router import product
from db import models
from db.database import engine
from exceptions import StoryException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

# App sirve para definir nuestros endpoints pero también para correr el servidor de uvicorn
# Cuando definimos un endpoint, por ejemplo @app.get('/'),debajo; definimos una función que se ejecutará cuando se haga una petición a esa ruta especifica

app = FastAPI()
app.include_router(user.router)
app.include_router(article.router)
app.include_router(product.router)
app.include_router(blog_get.router)
app.include_router(blog_post.router)

@app.get('/')
def index():
  return { "message": 'Hello World'}

# Los manejadores de excepciones personalizadas que hemos escrito
# se ejecutan cuando se lanzan excepciones en nuestro código
@app.exception_handler(StoryException)
def story_exception_handler(request: Request, exc: StoryException):
  return JSONResponse(
    status_code = 418,
    content = {"detail": exc.name}
  )


# Creamos la base de datos
# esto crea un archivo en la raiz llamado fastapi-practice.db
# pero si el archivo ya existe, no se sobrescribe
models.Base.metadata.create_all(engine)

# Añadimos el setup de CORS
origins = [
  'http://localhost:3000', # url del front
]

app.add_middleware(
  CORSMiddleware,
  allow_origins = origins,
  allow_credentials = True,
  allow_methods = ["*"],
  allow_headers = ["*"],
)
