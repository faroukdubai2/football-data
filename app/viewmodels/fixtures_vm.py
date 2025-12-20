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

    def update_rounds(self):
        """
        Fetches all rounds for the season and updates fixtures/rounds/index.json
        """
        print(f"Fetching rounds for League {settings.LEAGUE_ID} Season {settings.SEASON}...")
        data = FixturesAPI.get_rounds(settings.SEASON, settings.LEAGUE_ID)
        
        if data:
            JsonStore.save(settings.DATA_DIR / "fixtures/rounds/index.json", data)
            return data.get("response", [])
        return []

    def update_head_to_head(self, team1_id: int, team2_id: int):
        """
        Fetches head-to-head data for two teams
        """
        h2h_id = f"{team1_id}-{team2_id}"
        print(f"Fetching head-to-head for {h2h_id}...")
        data = FixturesAPI.get_head_to_head(h2h_id)
        
        if data:
            JsonStore.save(settings.DATA_DIR / f"fixtures/headtohead/{h2h_id}.json", data)
            return data.get("response", [])
        return []
        
    def update_fixture_details(self, fixture_id: int):
        """
        Fetches details for a specific fixture: Events, Lineups, Statistics, Players Statistics
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

        # Players Statistics
        players_stats = FixturesAPI.get_players_statistics(fixture_id)
        if players_stats:
            JsonStore.save(settings.DATA_DIR / f"fixtures/players/statistics/{fixture_id}.json", players_stats)
