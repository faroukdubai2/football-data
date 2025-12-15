from .base_api import BaseAPI

class TeamsAPI(BaseAPI):
    @staticmethod
    def get_team(team_id: int):
        return BaseAPI._get("teams", {"id": team_id})

    @staticmethod
    def get_venue(venue_id: int):
        return BaseAPI._get("venues", {"id": venue_id})
