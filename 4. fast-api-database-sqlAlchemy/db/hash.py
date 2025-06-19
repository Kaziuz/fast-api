# Este archivo se encarga
# de encriptar la contraseña del usuario

from passlib.context import CryptContext

pwd_ctx = CryptContext(schemes='bcrypt', deprecated='auto')

class Hash():
  def bcrypt(password: str):
    # Se utiliza para encriptar la contraseña
    return pwd_ctx.hash(password)

  def verify(hashed_password, plain_password):
    # Se utiliza para verificar si una contraseña
    # proporcionada es la contraseña almacenada
    return pwd_ctx.verify(plain_password, hashed_password)
