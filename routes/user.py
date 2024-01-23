from fastapi import APIRouter
from config.db import engine
from models.user import users
from schemas.user import User
from cryptography.fernet import Fernet

key = Fernet.generate_key()
cryp = Fernet(key)

user = APIRouter()

@user.get('/users')
def retrieveUser():
    with engine.connect() as conn:
        return conn.execute(users.select()).mappings().all()

@user.post('/')
def generateUser(user: User):
    newUser = user.model_dump()
    with engine.connect() as conn:
        result = conn.execute(users.insert().values(newUser))
        conn.commit()
        return conn.execute(users.select().where(users.c.id == result.lastrowid)).mappings().first()