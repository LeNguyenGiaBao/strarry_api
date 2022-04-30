from fastapi import FastAPI, File, UploadFile, Form
from fastapi.encoders import jsonable_encoder
import uvicorn
from model import Cart, User, Product
from query import signin_controller, signup_controller, get_list_product, insert_product_to_db, update_cart_by_account_product, get_list_cart_by_id
import cv2 
import asyncio
import numpy as np 
import base64

# Fast API
app = FastAPI()

@app.get("/")
def index():
    return {"name" : "giabao"}

@app.post("/signin/")
async def signin(email: str = Form(...), password: str = Form(...)):
    if email is None or password is None:
        return jsonable_encoder({
            'code': 200,
            'success': 'false',
            'msg': 'email and password is required'
        })
    print(email)
    user = User(email=email, password=password)
    id_user = signin_controller(user)
    if id_user is not None:
        return jsonable_encoder({
            'code': 200,
            'success': 'true',
            'id': id_user,
            'msg': 'sign in success'
        })

    else:
        return jsonable_encoder({
            'code': 200,
            'success': 'false',
            'msg': 'sign in failed'
        })

@app.post("/signup/")
async def signup(email: str = Form(...), password: str = Form(...)):
    if email is None or password is None:
        return jsonable_encoder({
            'code': 200,
            'success': 'false',
            'msg': 'email and password is required'
        })
    user = User(email=email, password=password)
    id_user = signup_controller(user)
    if id_user is not None:
        return jsonable_encoder({
            'code': 200,
            'success': 'true',
            'id': id_user,
            'msg': 'sign up success'
        })

    else:
        return jsonable_encoder({
            'code': 200,
            'success': 'false',
            'msg': 'sign in failed'
        })

@app.get('/products/')
async def get_product():
    products = get_list_product()
    return jsonable_encoder({
        'code': 200,
        'success': 'true',
        'products': products,
        'msg': 'load product success'
    })

@app.post('/products/insert/')
async def insert_product(name: str, id_category: int, description: str = None, price: int = 0, quantity: int = 0, image: UploadFile = File(None)):
    str_img = None 
    if image is not None:
        contents = await asyncio.wait_for(image.read(), timeout=1.0)
        nparr = np.fromstring(contents, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        _, encoded_image = cv2.imencode('.png', img)
        str_img = base64.b64encode(encoded_image)

    product = Product(name=name, description=description, price=price, quantity=quantity, image=str_img, id_category=id_category)
    id_product = insert_product_to_db(product)
    if id_product is not None:
        return jsonable_encoder({
            'code': 200,
            'success': 'true',
            'id': id_product,
            'msg': 'add product success'
        })

    else:
        return jsonable_encoder({
            'code': 200,
            'success': 'false',
            'msg': 'add product failed'
        })

@app.post('/cart/')
async def get_cart_by_id(id_account: int = Form(...)):
    carts = get_list_cart_by_id(id_account)
    return jsonable_encoder({
        'code': 200,
        'success': 'true',
        'cart': carts,
        'msg': 'load product success'
    })

# @app.post('/cart/insert/')
# async def insert_cart(id_account: int, id_product: int, amount_product: int = 0):
#     if id_account is None or id_product is None:
#         return jsonable_encoder({
#             'code': 200,
#             'success': 'false',
#             'msg': 'id account and id product is required'
#         })

#     cart = Cart(id_account=id_account, id_product=id_product, amount_product=amount_product)
#     id_cart = insert_cart_to_db(cart)
#     if id_cart is not None:
#         return jsonable_encoder({
#             'code': 200,
#             'success': 'true',
#             'id': id_cart,
#             'msg': 'add product success'
#         })

#     else:
#         return jsonable_encoder({
#             'code': 200,
#             'success': 'false',
#             'msg': 'add product failed'
#         })

@app.post('/cart/update/')
async def update_cart(id_account: int = Form(...), id_product: int = Form(...), amount_product: int = Form(0)):
    print(id_account, id_product, amount_product)
    if id_account is None or id_product is None:
        return jsonable_encoder({
            'code': 200,
            'success': 'false',
            'msg': 'id account and id product is required'
        })

    cart = Cart(id_account=id_account, id_product=id_product, amount_product=amount_product)
    id_cart = update_cart_by_account_product(cart)
    if id_cart is not None:
        return jsonable_encoder({
            'code': 200,
            'success': 'true',
            'id': id_cart,
            'msg': 'get product success'
        })

    else:
        return jsonable_encoder({
            'code': 200,
            'success': 'false',
            'msg': 'get product failed'
        })
    

if __name__ == "__main__":
    # run API
    uvicorn.run('app:app', host="0.0.0.0", port=8000, reload=True)