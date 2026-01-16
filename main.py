from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from data import getData, add_user, add_signup, LoginData, SignupData

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/all_user')
def user_login_detail():
    return getData()

@app.post('/login')
def add_login_detail(LoginData:LoginData):
    return add_user(LoginData)

@app.post('/signup')
def signup_user(SignupData:SignupData):
    return add_signup(SignupData)
