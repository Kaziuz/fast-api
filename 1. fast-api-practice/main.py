from typing import Optional
from fastapi import FastAPI, status, Response

from enum import Enum

# App sirve para definir nuestros endpoints pero también para correr el servidor de uvicorn
# Cuando definimos un endpoint, por ejemplo @app.get('/'),debajo; definimos una función que se ejecutará cuando se haga una petición a esa ruta especifica

app = FastAPI()

@app.get('/')
def index():
  return { "message": 'Hello World alex'}

# El orden de los endpoints es importante!!!
# Si definimos un endpoint que recibe un parámetro, y luego definimos un endpoint que recibe un string,
# el endpoint que recibe el string nunca se ejecutará, ya que el endpoint que recibe un parámetro siempre se ejecutará primero

# @app.get('/blog/all')
# def blog_all():
#   return {'message': 'All blogs provided'}

# para obtener los parámetros de la url (query parameters), se reciben en la función que se ejecuta después del path
# http://localhost:8000/blogs/all?page=1&page_size=10, aquí los parámetros son page y page_size

# Podemos poner valores por defecto a los parámetros, si no se envían en la url
# @app.get('/blogs/all')
# def get_all_blogs(page = 1, page_size = 10):
#   return { "message": f"All {page_size} blogs on page {page}"}

# Otra forma de poner estos parámetros opcionales es usando Optional, con optional quedan dinámicos
@app.get(
  '/blogs/all',
  tags=['Blog'],
  summary='Retrieve all blogs',
  description='This api call simulates fetching all blogs',
  response_description='The list of available blogs'
)
def get_all_blogs(page = 1, page_size: Optional[int] = None):
  return { "message": f"All {page_size} blogs on page {page}"}

# Aquí combinamos los parámetros por defecto con los parámetros opcionales
@app.get('/blog/{id}/comments/{comment_id}',tags=['Blog', 'comment'])
def get_comment(id: int, comment_id: int, valid: bool = True, username: Optional[str] = None):
  '''
  Estos comentarios aquí aparecerán en la documentación de swagger\n
  Simulates retrieving a comment of a blog
  
  - **id**: mandatory path parameter
  - **comment_id**: mandatory path parameter
  - **valid**: optional query parameter
  - **username**: optional query parameter
  '''
  return { "message": f"blog_id: {id}, comments_id: {comment_id}, valid: {valid}, username: {username}" }

class BlogType(str, Enum):
  short = 'short'
  story = 'story'
  howto = 'howto'

@app.get('/blog/type/{type}',tags=['Blog'])
def get_blog_type(type: BlogType):
  return { 'message': f'Blog type is {type}'}

@app.get(
  '/blog/{id}',
  status_code=status.HTTP_404_NOT_FOUND,
  tags=['Blog']
)
def blog_id(id: int, response: Response):
  if id > 5:
    response.status_code = status.HTTP_404_NOT_FOUND
    return { 'error': f"Blog with id {id} not found"}
  else:
    response.status_code = status.HTTP_200_OK
    return {'message': f"Blog with id {id}"}