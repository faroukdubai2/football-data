from pydantic import BaseModel
from typing import Optional, Dict, Any, List

class Fixture(BaseModel):
    id: int
    timezone: str
    date: str
    timestamp: int
    status: Dict[str, Any]

class FixtureResponse(BaseModel):
    fixture: Fixture
    league: Dict[str, Any]
    teams: Dict[str, Any]
    goals: Dict[str, Any]
    score: Dict[str, Any]
