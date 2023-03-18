from pydantic import BaseModel, Field

"""Validation models for incoming data"""

class Point(BaseModel):
    type: str
    lat: float
    lon: float


class Path(BaseModel):
    id: str
    name: str
    heading: float
    archived: bool
    point_a: Point = Field(alias="aPoint")
    point_b: Point = Field(alias="bPoint")
    last_modified: str = Field(alias="lastModifiedTime")
