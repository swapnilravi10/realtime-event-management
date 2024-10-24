from pydantic import BaseModel
from typing import List

class Event(BaseModel):
    id: int = None
    title: str
    organizer: str
    date_time: str
    duration: str
    location: str
    joiners: List[str] = []