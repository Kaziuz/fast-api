from fastapi import FastAPI
from routers import blog_get
from routers import blog_post
# App sirve para definir nuestros endpoints pero también para correr el servidor de uvicorn
# Cuando definimos un endpoint, por ejemplo @app.get('/'),debajo; definimos una función que se ejecutará cuando se haga una petición a esa ruta especifica

app = FastAPI()
app.include_router(blog_get.router)
app.include_router(blog_post.router)

@app.get('/')
def index():
  return { "message": 'Hello World'}

