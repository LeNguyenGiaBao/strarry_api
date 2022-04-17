from fastapi import FastAPI, File, UploadFile, Form
from fastapi.encoders import jsonable_encoder
import uvicorn
from model import User
from query import sign_in_user, sign_up_user

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
async def signup(user: User):
    id_user = sign_up_user(user)
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
    

if __name__ == "__main__":
    # run API
    uvicorn.run('app:app', host="0.0.0.0", port=8000, reload=True)