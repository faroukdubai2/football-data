from pydantic import BaseModel
from typing import Dict, Any

class Team(BaseModel):
    id: int
    name: str
    code: str
    country: str
    founded: int
    national: bool
    logo: str

class TeamResponse(BaseModel):
    team: Team
    venue: Dict[str, Any]
