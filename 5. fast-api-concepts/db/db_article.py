from sqlalchemy.orm.session import Session
from db.models import DbArticle
from schemas import ArticleBase
from fastapi import HTTPException, status
from exceptions import StoryException

def create_article(db: Session, request: ArticleBase):
  # Esto es una excepción personalizada
  # que se lanza cuando el usuario intenta
  # crear un articulo con un texto que comienza con 
  # el texto entre ""
  if request.content.startswith("Erase una vez"):
    raise StoryException("Por favor no comentes con Erase una vez")
  new_article = DbArticle(
    title = request.title,
    content = request.content,
    published = request.published,
    user_id = request.creator_id
  )
  db.add(new_article)
  db.commit()
  db.refresh(new_article)
  return new_article

def get_article(db:Session, id: int):
  article = db.query(DbArticle).filter(DbArticle.id == id).first()
  # Si el articulo no existe, lanza una excepción
  if not article:
    raise HTTPException(
      status_code=status.HTTP_404_NOT_FOUND,
      detail=f"Article with id: {id} not found"
    )
  return article