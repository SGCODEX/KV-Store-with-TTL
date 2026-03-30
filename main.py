from fastapi import FastAPI
from store import KVStore
from models import SetRequest

app = FastAPI()
kv = KVStore()


@app.get("/")
def home():
    return {"message": "KV Store Running"}


# SET (Create / Update)
@app.post("/set")
def set_value(request: SetRequest):
    kv.set(request.key, request.value, request.ttl)
    return {"message": "Key stored successfully"}


# GET
@app.get("/get/{key}")
def get_value(key: str):
    value = kv.get(key)

    if value is None:
        return {"message": "Key not found or expired"}

    return {"key": key, "value": value}


# DELETE
@app.delete("/delete/{key}")
def delete_value(key: str):
    success = kv.delete(key)

    if not success:
        return {"message": "Key not found"}

    return {"message": "Key deleted successfully"}