from pydantic import BaseModel
from typing import Dict, Any

class Player(BaseModel):
    id: int
    name: str
    age: int
    number: Dict[str, Any] | None
    position: str
    photo: str

class PlayerResponse(BaseModel):
    player: Player
    statistics: list[Dict[str, Any]]
