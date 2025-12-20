from .base_api import BaseAPI

class FixturesAPI(BaseAPI):
    @staticmethod
    def get_fixtures_by_team(season: int, team_id: int):
        return BaseAPI._get("fixtures", {"season": season, "team": team_id})

    @staticmethod
    def get_rounds(season: int, league_id: int):
        return BaseAPI._get("fixtures/rounds", {"season": season, "league": league_id})

    @staticmethod
    def get_head_to_head(h2h: str):
        return BaseAPI._get("fixtures/headtohead", {"h2h": h2h})

    @staticmethod
    def get_events(fixture_id: int):
        return BaseAPI._get("fixtures/events", {"fixture": fixture_id})
        
    @staticmethod
    def get_lineups(fixture_id: int):
        return BaseAPI._get("fixtures/lineups", {"fixture": fixture_id})

    @staticmethod
    def get_statistics(fixture_id: int):
        return BaseAPI._get("fixtures/statistics", {"fixture": fixture_id})

    @staticmethod
    def get_players_statistics(fixture_id: int):
        return BaseAPI._get("fixtures/players", {"fixture": fixture_id})
