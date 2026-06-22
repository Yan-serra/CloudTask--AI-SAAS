from fastapi import FastAPI
from database import engine, SessionLocal, Base
from models import User

Base.metadata.create_all(bind=engine)

app = FastAPI()

#CREATE ITEM
@app.post("/users")
def create_item(name: str, age: int, email: str):
    db = SessionLocal()
    user = User(name=name, age=age, email=email)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

#LIST ITEMS
@app.get("/users")
def list_users():
    db = SessionLocal()
    return db.query(User).all()

#DELETE ITEM
@app.delete("/users/{id}")
def delete_item(id: int):
    db = SessionLocal()
    user = db.query(User).filter(User.id == id).first()
    db.delete(user)
    db.commit()
    return {"message": "Usuario deletado com sucesso!"}
