from fastapi import FastAPI, File, UploadFile, Form
from fastapi.encoders import jsonable_encoder
import uvicorn
from model import User
from query import sign_in_user

# Fast API
app = FastAPI()

@app.get("/")
def index():
    return {"name" : "giabao"}

@app.post("/login/")
async def login(user: User):
    id_user = sign_in_user(user)
    if id_user is not None:
        return jsonable_encoder({
            'code': '200',
            'is_login': 'true',
            'id': id_user,
            'msg': 'login success'
        })

    else:
        return jsonable_encoder({
            'code': '200',
            'is_login': 'false',
            'msg': 'login failed'
        })
    

if __name__ == "__main__":
    # run API
    uvicorn.run('app:app', host="0.0.0.0", port=8000, reload=True)