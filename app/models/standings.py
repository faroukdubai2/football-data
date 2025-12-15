from pydantic import BaseModel
from typing import Dict, Any, List

class Standing(BaseModel):
    rank: int
    team: Dict[str, Any]
    points: int
    goalsDiff: int
    group: str
    form: str
    status: str
    description: str | None
    all: Dict[str, Any]
    home: Dict[str, Any]
    away: Dict[str, Any]
    update: str

class StandingsResponse(BaseModel):
    league: Dict[str, Any]
