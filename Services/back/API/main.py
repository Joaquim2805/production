from fastapi import FastAPI, Query, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Annotated, Optional
from datetime import datetime, timedelta
import random
import uvicorn
from sqlmodel import select, Session
from model import User,  UserCreate
from database import get_session, init_db
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt


SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

app = FastAPI()


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


app.add_middleware(
    CORSMiddleware,
    # Vous pouvez spécifier les origines autorisées ici
    allow_origins=["http://localhost:8000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: str = payload.get("sub")
        if user_id is None:
            raise HTTPException(status_code=400, detail="Token invalide")
    except JWTError:
        raise HTTPException(status_code=400, detail="Token invalide")
    return user_id


@app.get("/current_user", response_model=User)
def read_current_user(current_user: User = Depends(get_current_user)):
    return current_user


@app.get("/ping")
async def pong():
    return {"ping": "pong!"}


@app.get("/")
def test():
    return "YES API"


@app.post("/add_user")
def add_song(user: UserCreate, session: Session = Depends(get_session)):
    user = User(id=user.id, password=user.password)
    session.add(user)
    session.commit()
    session.refresh(user)
    return user


@app.get("/users")
def get_users(session: Session = Depends(get_session)):
    # Effectuez une requête pour sélectionner tous les enregistrements de la table User
    statement = select(User)
    result = session.exec(statement)

    # Transformez les résultats en une liste de dictionnaires
    users = [user for user in result]

    return users


@app.get("/login")
def authenticate_user(id: str = Query(..., description="User ID"), password: str = Query(..., description="User Password"), session: Session = Depends(get_session)):
    user = session.get(User, id)

    if user is None or user.password != password:
        raise HTTPException(
            status_code=401, detail="L'authentification a échoué")

    # Si l'authentification réussit, un token doit être généré et renvoyé
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": id}, expires_delta=access_token_expires
    )

    return {"access_token": access_token, "token_type": "bearer"}
