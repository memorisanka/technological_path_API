import requests
from django.db import models
from pydantic import BaseModel


class Point(BaseModel):
    type: str
    lat: float
    lon: float


response = requests.get('https://mocki.io/v1/cbf7bb1d-c5b1-4dfa-83d2-5800f78ffb8d')
data = response.json()

for item in data['values'][0]:
    print(item)


class Path(BaseModel):
    id: str
    name: str
    heading: float
    point_a = Point(alias="aPoint")
    point_b = Point(alias="bPoint")
    last_modified = str
    archived = bool


response = requests.get('https://mocki.io/v1/cbf7bb1d-c5b1-4dfa-83d2-5800f78ffb8d')
data = response.json()

for item in data['values']:
    Path(**item)


class Field(models.Model):
    id = models.CharField()


class PathModel(models.Model):
    id = models.CharField()
    name = models.CharField()
    a_lat = models.FloatField()
    a_lon = models.FloatField()
    b_lat = models.FloatField()
    b_lon = models.FloatField()
    last_modified_time = models.DateTimeField()
    archived = models.BooleanField()
    field = models.ForeignKey(Field, related_name='path', on_delete=models.CASCADE)
