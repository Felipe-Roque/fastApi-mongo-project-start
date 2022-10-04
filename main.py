import json
import string

from fastapi import FastAPI
from mongoengine import connect

from models import Device01

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


from pydantic import BaseModel
from datetime import datetime

class NewDeviceData(BaseModel):
    id_tago: str
    time: datetime
    unit: str
    value: float
    variable: str
    metadata: dict
    group: str
    device: str

@app.post("/add_DeviceData")
def add_add_DeviceData(oDevice: NewDeviceData):
    new_device_data = Device01(id_tago=oDevice.id_tago,
                               time=oDevice.time,
                               unit=oDevice.unit,
                               value=oDevice.value,
                               variable=oDevice.variable,
                               metadata=oDevice.metadata,
                               group=oDevice.group,
                               device=oDevice.device)
    new_device_data.save()

    return {"message":"device data added successsufully!"}