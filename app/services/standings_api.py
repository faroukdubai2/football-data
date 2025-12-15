from .base_api import BaseAPI

class StandingsAPI(BaseAPI):
    @staticmethod
    def get_standings(season: int, league_id: int):
        return BaseAPI._get("standings", {"season": season, "league": league_id})
