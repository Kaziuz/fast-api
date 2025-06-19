from fastapi import APIRouter, Query, Body, Path
from pydantic import BaseModel
from typing import Optional, List, Dict

# https://fastapi.tiangolo.com/es/reference/apirouter/?h=apirouter
router = APIRouter(
  prefix="/blog",
  tags=["blog"]
)

# Image esta heredando de baseModel para poder usar los validadores de pydantic
class Image(BaseModel):
  url: str
  alias: str

# En esta clase model definimos los campos que queremos recibir en la ruta post /new
# para poder validarlos cuando lleguen
class BlogModel(BaseModel):
  title: str
  content: str
  nb_comments: int
  published: Optional[bool] # puede ser booleano, o None
  tags: List[str] = [] # Podemos crear nuestros propios validadores, en este caso creamos una lista de strings que por defecto es vacia, pero podrias tener List, Set, dict, tuple
  metadata: Dict[str, str] = {'key1': 'val1'} # Podemos crear un diccionario de strings que por defecto es vacio
  image: Optional[Image] = None

@router.post('/new/{id}')
def create_blog(blog: BlogModel, id: int, version: int = 1): # los datos que entran deben de ser como estan en la clase, de lo contrario no se aceptará y lanzara un 422 al cliente
  return {
    "id": id,
    "data": blog,
    "version": version,
  }
  
# Al usar Query, se declara que comment_title será un parámetro de consulta,
# es decir, se pasará en la URL usando ?comment_title=valor.
# La función Query permite personalizar el parámetro de consulta,
# agregando validaciones, descripciones y metadatos que se mostrarán en la documentación automática de Swagger
@router.post('/new/{id}/comment/{comment_id}')
def create_comment(
  blog: BlogModel,
  id: int,
  comment_title: int = Query(None, title="title of the comment", description="some description for the comment title", alias="must a number", deprecated=False ),
    # content: str = Body('Hi how are you') # el valor por defecto es Hi how are you para el body, y para este ejemplo es opcional porque le pasamos un texto
    # content: str = Body(...), # cuando a content le pasamos una ellipses en el body (...) lo hacemos obligatorio en el cliente
    content: str = Body(
      'Hi how are you',
      min_length=10,
      max_length=20,
      regex='^[a-z\s]*$'
    ), # podemos validar el contenido del body con min_length y max_length, regex y muchos mas
    # v: Optional[List[str]] = Query(None) # estos son parametros de query, /blog/new/4/comment?commentId=5&v=string1&v=string2&v=string3&v=string4'
    v: Optional[List[str]] = Query(['1.0', '2.0', '3.0']), # podemos pasar tambien valores por defecto a los parametros de query
    comment_id: int = Path(gt=5, le=10) # podemos validar el valor de comment_id con gt y le, que significa que el valor debe ser mayor a 5 y menor o igual a 10
):
  return {
    "blog": blog,
    "id": id,
    "comment_title": comment_title,
    "content": content, # este valor content es el que esta en el body, el que dice hi how are you
    "version": v,
    "comment_id": comment_id,
  }