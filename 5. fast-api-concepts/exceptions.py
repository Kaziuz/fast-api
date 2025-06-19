# En este archivo están contenidas las
# excepciones personalizadas (respuestas de errores)que se pueden lanzar
# en nuestro código

class StoryException(Exception):
  def __init__(self, name: str):
    self.name = name