
from fastapi import FastAPI, HTTPException, Depends,status
from pydantic import BaseModel
from typing import Annotated
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session


app = FastAPI()

# Create tables
models.Base.metadata.create_all(bind=engine)

# Pydantic models
class read_products( BaseModel):
    title: str
    description: str
    price: int


class read_product(BaseModel):
    id: int
    title: str
    description: str
    price: float


class ProductCreate(BaseModel):
    title: str
    description: str
    price: int

class ProductUpdate(BaseModel):
    title: str
    description: str
    price: float 


# CRUD Operations
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session,Depends(get_db)]

@app.get( "/" , status_code=status.HTTP_200_OK)
async def user (user: None, db: db_dependency):
    if user is None:
        raise HTTPException(status_code=401, detail='Authentication Failed')
    return {"User": user}



#To Retrieve a list of all products from a database.
@app.get("/products/", status_code=status.HTTP_200_OK)
async def read_products(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    products = db.query(models.Product).offset(skip).limit(limit).all()
    if products is None:
        raise HTTPException(status_code=404,detail='No Products available')
    return products


#To Retrieve details of a specific product by its ID.
@app.get("/products/{product_id}", status_code=status.HTTP_200_OK)
async def read_product(product_id: int, db: Session = Depends(get_db)):
    db_product_id = db.query(models.Product).filter(models.Product.id == product_id).first()
    if db_product_id is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product_id


#To Create a new product
@app.post("/products/", status_code=status.HTTP_201_CREATED)
async def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    db_product = models.Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

#To Update an existing product based on its ID.
@app.put("/products/{product_id}", status_code=status.HTTP_202_ACCEPTED)
async def update_product(product_id: int, product: ProductUpdate, db: Session = Depends(get_db)):
    db_product_update = db.query(models.Product).filter(models.Product.id == product_id).first()
    if db_product_update is None:
        raise HTTPException(status_code=404, detail="Product not found")
    for key, value in product.dict().items():
        setattr(db_product_update, key, value)
    db.commit()
    db.refresh(db_product_update)
    return db_product_update


#To Delete a product by its ID.
@app.delete("/products/{product_id}", status_code=status.HTTP_200_OK)
async def delete_product(product_id: int, db: Session = Depends(get_db)):
    db_product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    db.delete(db_product)
    db.commit()
    return {"message": "Product deleted successfully"}
