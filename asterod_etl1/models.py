from pydantic import BaseModel

class AsteroidModel(BaseModel):
    id: str
    name: str
    magnitude: float
    hazardous: bool
    approach_date: str
    velocity: float
    miss_distance: float
    orbiting_body: str