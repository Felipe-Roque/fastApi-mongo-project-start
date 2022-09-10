from fastapi import FastAPI
from models import Device01
from mongoengine import connect
import json

app = FastAPI()
connect(db="dbSenai", host="localhost", port=27017)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/get_all_devices")
def get_all_devices():
    devices = Device01.objects().to_json()
    devices_list = json.loads(devices)

    # print(type(devices_list))
    # print(type(devices))
    # print(devices)

    return {"devices": devices_list}
