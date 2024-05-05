# database.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base



# Database URL for products
URL_DATABASE = "mysql+mysqlconnector://root:root@localhost:3306/products"

# Database URL for JWT authentication
USERS_DATABASE_URL = 'mysql+mysqlconnector://root:root@localhost:3306/users'

engine = create_engine(URL_DATABASE)

auth_engine = create_engine(USERS_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

AuthSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=auth_engine)

Base = declarative_base()

AuthBase = declarative_base()