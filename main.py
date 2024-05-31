from fastapi import FastAPI

app = FastAPI()


@app.get("/users")
async def all_users():
    return {"User": "David"}


@app.post("/products")
async def all_products(title: str, price: int):
    return {"status": f"Your product name {title} and price {price}"}