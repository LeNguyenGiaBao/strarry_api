from fastapi import FastAPI, File, UploadFile, Form
from fastapi.encoders import jsonable_encoder
import uvicorn
from model import Cart, User, Product, Bill_product, Bill
from query import update_user_by_id,get_user_by_id,signin_controller, signup_controller,get_email_by_id, get_list_product, insert_product_to_db, update_cart_by_account_product, get_list_cart_by_id, get_product_by_idCategory
from query import insert_bill_product_to_db,delete_cart_by_id_account, update_bill_product_to_db, get_list_bill_product_by_id, insert_bill_to_db, update_bill_to_db, get_list_bill_by_id
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

@app.post('/account/email/')
async def get_email(id_account: int =Form(...)):
    email = get_email_by_id(id_account)
    print(type(email))
    return jsonable_encoder({
        'code': 200,
        'success': 'true',
        'email': email,
        'msg': 'get email success'
    })

@app.post('/account/update/')
async def update_account_byid(name: str=Form(...), phone: str=Form(...), address: str=Form(...),id_account: int=Form(...) ):
    index = update_user_by_id(name, phone, address, id_account)
    status=False
    if index >=0:
        status=True
    return jsonable_encoder({
        'code': 200,
        'success': 'true',
        'status': status,
        'msg': 'update account success'
    })

@app.post('/account/id/')
async def get_account_byid(id_account: int =Form(...)):
    account = get_user_by_id(id_account)
    print(type(account))
    return jsonable_encoder({
        'code': 200,
        'success': 'true',
        'account': account,
        'msg': 'get account success'
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
@app.post('/products/get/')
async def get_product_by_id_Category(id_category: int =Form(...)):
    products = get_product_by_idCategory(id_category)
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
@app.post('/cart/delete/')
async def delete_cart(id_account: int =Form(...)):
    check = delete_cart_by_id_account(id_account)
    return jsonable_encoder({
        'code': 200,
        'success': 'true',
        'cart': check,
        'msg': 'delete cart success'
    })

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

# bill product
@app.post('/bill_product/')
async def get_list_bill_product_by_id(id: int = Form(...)):
    bill_product = get_list_bill_product_by_id(id)
    return jsonable_encoder({
        'code': 200,
        'success': 'true',
        'bill_product': bill_product,
        'msg': 'load bill_product success'
    })

@app.post('/bill_product/insert/')
async def insert_bill_product(id: int = Form(...), id_product: int = Form(...), amount_product: int = Form(0)):
    if id is None or id_product is None:
        return jsonable_encoder({
            'code': 200,
            'success': 'false',
            'msg': 'id  and id product is required'
        })

    bill_product = Bill_product(id=id, id_product=id_product, amount_product=amount_product)
    id_bill_product = insert_bill_product_to_db(bill_product)
    if id_bill_product is not None:
        return jsonable_encoder({
            'code': 200,
            'success': 'true',
            'id': id_bill_product,
            'msg': 'add bill product success'
        })

    else:
        return jsonable_encoder({
            'code': 200,
            'success': 'false',
            'msg': 'add bill product failed'
        })

@app.post('/bill_product/update/')
async def update_bill_product(id: int = Form(...), id_product: int = Form(...), amount_product: int = Form(0)):
    print(id, id_product, amount_product)
    if id is None or id_product is None:
        return jsonable_encoder({
            'code': 200,
            'success': 'false',
            'msg': 'id  and id product is required'
        })

    bill_product = Bill_product(id=id, id_product=id_product, amount_product=amount_product)
    id_bill_product = update_bill_product_to_db(bill_product)
    if id_bill_product is not None:
        return jsonable_encoder({
            'code': 200,
            'success': 'true',
            'id': id_bill_product,
            'msg': 'get bill product success'
        })

    else:
        return jsonable_encoder({
            'code': 200,
            'success': 'false',
            'msg': 'get bill product failed'
        })

# bill
@app.post('/bill/insert/')
async def insert_bill(id_account: int = Form(...) , price: int = Form(...), discount: int = Form(0), phone: str = Form(...), address: str = Form(...) ):
    if id is None or id_account is None:
        return jsonable_encoder({
            'code': 200,
            'success': 'false',
            'msg': 'id  and  id_account is required'
        })

    bill = Bill(id_account = id_account, price = price, discount = discount, phone = phone, address = address )
    id_bill = insert_bill_to_db(bill)
    if id_bill is not None:
        return jsonable_encoder({
            'code': 200,
            'success': 'true',
            'id': id_bill,
            'msg': 'add bill  success'
        })

    else:
        return jsonable_encoder({
            'code': 200,
            'success': 'false',
            'msg': 'add bill  failed'
        })

@app.post('/bill/update/')
async def update_bill(id: int = Form(...), id_account: int = Form(...), price: int = Form(...), discount: int = Form(...), phone: str = Form(...), address: str = Form(...)):
    print(id, id_account)
    if id is None or id_account is None:
        return jsonable_encoder({
            'code': 200,
            'success': 'false',
            'msg': 'id  and  id_account is required'
        })

    bill = Bill(id = id, id_account = id_account, price = price, discount = discount, phone = phone, address = address )
    id_bill = update_bill_to_db(bill)
    if id_bill is not None:
        return jsonable_encoder({
            'code': 200,
            'success': 'true',
            'id': id_bill,
            'msg': 'get bill  success'
        })

    else:
        return jsonable_encoder({
            'code': 200,
            'success': 'false',
            'msg': 'get bill  failed'
        })

@app.post('/bill/')
async def get_list_bill_by_id(id_account: int = Form(...)):
    bill = get_list_bill_by_id(id_account)
    return jsonable_encoder({
        'code': 200,
        'success': 'true',
        'bill': bill,
        'msg': 'load bill success'
    })

if __name__ == "__main__":
    # run API
    uvicorn.run('app:app', host="0.0.0.0", port=8000, reload=True)