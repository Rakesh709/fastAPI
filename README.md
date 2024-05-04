# fastAPI
FastAPI is an open-source web framework that uses Python to create APIs

## Requirements

● Using a Python web framework FastAPI to build the API.
● Implement endpoints for the following functionalities:
 - GET /products: Retrieve a list of all products from a database.
 - GET /products/{id}: Retrieve details of a specific product by its ID.
 - POST /products: Create a new product with details like title, description,price, etc. (data should be received in JSON format).
 - PUT /products/{id}: Update an existing product based on its ID.
 - DELETE /products/{id}: Delete a product by its ID.


## Create new python env 
 - python3 -m venv env
 - source env/bin/activate  (if failed)
 - pip install fastapi uvicorn sqlalchemy

## To launch fastAPI
 - uvicorn main:app --reload