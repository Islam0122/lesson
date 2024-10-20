from fastapi import FastAPI

app = FastAPI(
    title="FastAPI",
)

fake_users = [
    {"id": 1, "username": "islam", "role": "admin"},
    {"id": 2, "username": "islam1", "role": "user"},
    {"id": 3, "username": "islam3", "role": "admin"},
]


@app.get("/user/{user_id}")
def get_user(user_id: int):
    return [user for user in fake_users if user.get('id') == user_id]


fake_trades = [
    {"id": 1, "date": "2020-01-01", "price": 100, "quantity": 1},
    {"id": 2, "date": "2020-01-02", "price": 200, "quantity": 1},
    {"id": 3, "date": "2020-01-03", "price": 300, "quantity": 1},
]


@app.get("/trades")
def get_trade(limit: int = 1, offset: int = 0):
    return fake_trades[offset:][:limit]


@app.post("/user/{user_id}")
def change_user(user_id: int,new_username: str):
    user1 = list(filter(lambda user: user.get('id') == user_id, fake_users))[0]
    user1['username'] = new_username
    return {"status" :200,
            "data":user1}
