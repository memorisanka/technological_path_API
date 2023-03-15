from django.db import models
from pydantic import BaseModel


class Point(BaseModel):
    lat: float
    lon: float


class Path(BaseModel):
    id: str
    name: str
    heading: float
    point_a = Point(alias="aPoint")
    point_b = Point(alias="aPoint")
    last_modified = str
    archived = bool


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
