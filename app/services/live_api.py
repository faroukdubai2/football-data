from .base_api import BaseAPI

class LiveAPI(BaseAPI):
    @staticmethod
    def get_live_fixtures(team_id: int):
        return BaseAPI._get("fixtures", {"live": "all", "team": team_id})
