import mysql.connector as sql
from pydantic import BaseModel

class LoginData(BaseModel):
    userID:str
    password:str

class SignupData(BaseModel):
    userID:str
    email:str
    password:str

conn = sql.connect(host="localhost", user='root', password='root')
conn.autocommit = True
cur = conn.cursor()

cur.execute("create database if not exists project;")
cur.execute("use project;")
# cur.execute("drop table if exists loginData;")
cur.execute("create table if not exists loginData(userID varchar(50) not null, email varchar(100), password varchar(15) not null, primary key(userID));")

def getData():
    userData = []
    cur.execute("select * from loginData;")
    Data = cur.fetchall()
    for i in  Data:
        userData.append(LoginData(userID=i[0], password=i[2]))
    return userData

def add_user(LoginData:LoginData):
    # Check if user exists and password matches
    cur.execute(f"select * from loginData where userID = '{LoginData.userID}' and password = '{LoginData.password}';")
    if cur.fetchone():
        return {"message": "Login successful"}
    else:
        raise Exception("Invalid userID or password")

def add_signup(SignupData:SignupData):
    # Check if user already exists
    cur.execute(f"select * from loginData where userID = '{SignupData.userID}';")
    if cur.fetchone():
        raise Exception("User already exists")
    
    query = f"insert into loginData (userID, email, password) values ('{SignupData.userID}', '{SignupData.email}', '{SignupData.password}');"
    cur.execute(query)
    return {"message": "Account created successfully"}