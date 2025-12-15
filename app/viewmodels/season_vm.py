from app.services.teams_api import TeamsAPI
from app.services.players_api import PlayersAPI
from app.config.settings import settings
from app.storage.json_store import JsonStore

class SeasonViewModel:
    def update_team_info(self):
        print(f"Fetching team info for Team {settings.TEAM_ID}...")
        # Team Info
        data = TeamsAPI.get_team(settings.TEAM_ID)
        if data:
            JsonStore.save(settings.DATA_DIR / f"teams/{settings.TEAM_ID}.json", data)
            
            # Extract Venue ID if present and update venue
            try:
                venue_id = data["response"][0]["venue"]["id"]
                if venue_id:
                    self.update_venue_info(venue_id)
            except (IndexError, KeyError, TypeError):
                pass

    def update_venue_info(self, venue_id: int):
        print(f"Fetching venue info for Venue {venue_id}...")
        data = TeamsAPI.get_venue(venue_id)
        if data:
            JsonStore.save(settings.DATA_DIR / f"venues/{venue_id}.json", data)

    def update_players(self):
        print(f"Fetching players for Team {settings.TEAM_ID} Season {settings.SEASON}...")
        data = PlayersAPI.get_players(settings.SEASON, settings.TEAM_ID)
        if data:
            JsonStore.save(settings.DATA_DIR / f"players/{settings.SEASON}.json", data)
