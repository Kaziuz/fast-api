# este archivo es solo para definir un producto dummy para pruebas
# donde probamos los diferentes tipos de respuestas
# que pueden devolver el sistema, entre ella:
# HTML, XML, FILES, STREAMING, PLAIN TEXT, etc

# las respuestas personalizadas son necesarios por: Headers, Cookies, etc
# manejar un lógica compleja

from typing import Optional, List
from fastapi import APIRouter, Header, Cookie, Form
from fastapi.responses import Response, HTMLResponse, PlainTextResponse

router = APIRouter(
  prefix = '/product',
  tags = ['product']
)

products = ['watch', 'camera', 'phone']

# En este endpoint añadimos un nuevo producto
# Form es una function proporcionada por fastAPi para indicar que un parametro
# provenga de un formulario HTML
# la ellipsos (...) indica que el parametro es obligatorio
# https://fastapi.tiangolo.com/tutorial/request-forms/?h=form#define-form-parameters
@router.post('/new')
def create_product(name: str = Form(...)):
  products.append(name)
  return products


@router.get('/all')
def get_all_products():
  # Por defecto el sistema devuelve en formato JSON
  # return products
  
  # Devolvemos entonces como texto sin formato (string)
  data = " ".join(products)

  # construimos aquí una respuesta personalizada
  response = Response(content=data, media_type='text/plain')
  
  # Aquí voy a configurar una cookie solo paa ejemplo
  # https://fastapi.tiangolo.com/advanced/response-cookies/#return-a-response-directly
  response.set_cookie(key="test_cookie", value="mi_valor_de_la_cookie")
  
  return response


# aquí voy a definir un endpoint que usa headers
# el parámetro custom_header habilita un campo en el swagger para
# añadir información en el header
# para este caso usamos solo un header
@router.get('/withheader')
def get_products(response: Response, custom_header: Optional[str] = Header(None)):
  return products

# para este caso usamos multiples headers
# con el mismo nombre pero diferentes valores
@router.get('/withheaders')
def get_products_list(
  response: Response,
  custom_header: Optional[List[str]] = Header(None),
  test_cookie: Optional[str] = Cookie(None) # Aqui obtengo el valor de la cookie que setie en la funt get_all_products
  ):
  # Cualquier header que proporcionemos en la entrada sera mostrado 
  # en custom_response_header
  # https://fastapi.tiangolo.com/es/advanced/response-headers/
  if custom_header:
    response.headers['custom-response-header'] = ", ".join(custom_header) 
  
  return {
    'data': products,
    'custom_header': custom_header,
    'test_cookie': test_cookie
    }


# Endpoint que responde con un html
# el parámetro responses es para documentar el endpoint, 
# muy muy importante porque si no lo hacemos, puede haber confusion para
# quienes usen nuestra API
@router.get('/{id}', responses={
  200: {
    "content": {
      "text/html": {
        # example value
        "example": "<div>Product</div>"
      }
    },
    "description": "Retorna un HTML para un objeto"
  },
  404: {
    "content": {
      "text/plain": {
        # example value
        "example": "Product not available"
      }
    },
    "description": "Un mensaje limpio para errores"
  }
})
def get_product(id: int):
  if id > len(products):
    out = f"Example product not found"
    return PlainTextResponse(status_code=404,content=out,media_type='text/plain')
  else:
    product = products[id]
    out = f"""
    <head>
      <style>
      .product {{
        width: 500px;
        height: 30px;
        border: 2px inset green;
        background-color: lightblue;
        text-align: center;
      }}
      </style>
    </head>
    <div class="product">
      {product}
    </div>
    """
    return HTMLResponse(content=out, media_type='text/html')
