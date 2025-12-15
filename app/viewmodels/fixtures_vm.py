from app.services.fixtures_api import FixturesAPI
from app.config.settings import settings
from app.storage.json_store import JsonStore

class FixturesViewModel:
    def update_fixtures(self):
        """
        Fetches all fixtures for the season and updates fixtures/index.json
        """
        print(f"Fetching fixtures for Team {settings.TEAM_ID} Season {settings.SEASON}...")
        data = FixturesAPI.get_fixtures_by_team(settings.SEASON, settings.TEAM_ID)
        
        if data:
            JsonStore.save(settings.DATA_DIR / "fixtures/index.json", data)
            return data.get("response", [])
        return []
        
    def update_fixture_details(self, fixture_id: int):
        """
        Fetches details for a specific fixture: Events, Lineups, Statistics
        """
        print(f"Updating details for fixture {fixture_id}...")
        
        # Events
        events = FixturesAPI.get_events(fixture_id)
        if events:
            JsonStore.save(settings.DATA_DIR / f"fixtures/events/{fixture_id}.json", events)
            
        # Lineups
        lineups = FixturesAPI.get_lineups(fixture_id)
        if lineups:
            JsonStore.save(settings.DATA_DIR / f"fixtures/lineups/{fixture_id}.json", lineups)
            
        # Statistics
        stats = FixturesAPI.get_statistics(fixture_id)
        if stats:
            JsonStore.save(settings.DATA_DIR / f"fixtures/statistics/{fixture_id}.json", stats)
