from app.services.standings_api import StandingsAPI
from app.config.settings import settings
from app.storage.json_store import JsonStore

class StandingsViewModel:
    def update_standings(self):
        print(f"Fetching standings for League {settings.LEAGUE_ID} Season {settings.SEASON}...")
        data = StandingsAPI.get_standings(settings.SEASON, settings.LEAGUE_ID)
        
        if data:
            JsonStore.save(settings.DATA_DIR / "standings/index.json", data)
