from fastapi import FastAPI, File, UploadFile, Form
from fastapi.encoders import jsonable_encoder
import uvicorn
from model import User, Product
from query import sign_in_user, sign_up_user_to_db, get_list_product, insert_product_to_db
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
async def signin(user: User):
    id_user = sign_in_user(user)
    if id_user is not None:
        return jsonable_encoder({
            'code': '200',
            'success': 'true',
            'id': id_user,
            'msg': 'sign in success'
        })

    else:
        return jsonable_encoder({
            'code': '200',
            'success': 'false',
            'msg': 'sign in failed'
        })

@app.post("/signup/")
async def signup(email: str = Form(None), password: str = Form(None)):
    if email is None or password is None:
        return jsonable_encoder({
            'code': '200',
            'success': 'false',
            'msg': 'sign in failed'
        })
    user = User(email=email, password=password)
    print(user.email)
    id_user = sign_up_user_to_db(user)
    if id_user is not None:
        return jsonable_encoder({
            'code': '200',
            'success': 'true',
            'id': id_user,
            'msg': 'sign up success'
        })

    else:
        return jsonable_encoder({
            'code': '200',
            'success': 'false',
            'msg': 'sign in failed'
        })

@app.get('/products/')
async def get_product():
    products = get_list_product()
    return jsonable_encoder({
        'code': '200',
        'products': products,
        'msg': 'load product success'
    })

@app.post('/products/insert/')
async def insert_product(name: str, id_category: int, description: str = Form(None), price: int = Form(0), quantity: int = Form(0), image: UploadFile = File(None)):
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
            'code': '200',
            'success': 'true',
            'id': id_product,
            'msg': 'add product success'
        })

    else:
        return jsonable_encoder({
            'code': '200',
            'success': 'false',
            'msg': 'add product failed'
        })

    

    

if __name__ == "__main__":
    # run API
    uvicorn.run('app:app', host="0.0.0.0", port=8000, reload=True)