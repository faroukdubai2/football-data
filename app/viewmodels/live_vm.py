import json
from datetime import datetime, timezone, timedelta
from app.services.fixtures_api import FixturesAPI
from app.config.settings import settings
from app.storage.json_store import JsonStore

class LiveViewModel:
    def check_and_update_live(self):
        """
        Checks for live matches and updates data within API quotas.
        Strategy:
        - Check Index (Local or API?) -> API is safer to detect 'Live' status change.
          (1 Call).
        - If Live:
          - Update Events (Most important for updates) -> (1 Call)
          - Update Lineups -> Only if 0-15 mins in? Or just once? (Skip if exists?)
          - Update Stats -> Every ~10 mins? 
        """
        print("Checking live status...")
        
        # 1. Fetch current fixtures status (Refresh Index)
        # This gives us Score and Status
        fixtures_response = FixturesAPI.get_fixtures_by_team(settings.SEASON, settings.TEAM_ID)
        if not fixtures_response:
            return

        # Save index
        path_index = settings.DATA_DIR / "fixtures/index.json"
        JsonStore.save(path_index, fixtures_response)
        
        # 2. Find live match
        live_statuses = ["1H", "2H", "ET", "BT", "P", "INT", "LIVE"]
        active_match = None
        
        for item in fixtures_response.get("response", []):
            if item["fixture"]["status"]["short"] in live_statuses:
                active_match = item["fixture"]
                break
        
        if not active_match:
            print("No live match found.")
            return

        fixture_id = active_match["id"]
        elapsed = active_match["status"].get("elapsed", 0)
        print(f"Live Match Detected: {fixture_id} ({elapsed}')")

        # 3. Fetch Details High Priority: Events
        events = FixturesAPI.get_events(fixture_id)
        if events:
            JsonStore.save(settings.DATA_DIR / f"fixtures/events/{fixture_id}.json", events)
        
        # 4. Fetch Details Low Priority: Statistics (Every ~10 mins based on elapsed?)
        # Simple modulo logic if we ran strictly every 2 mins? 
        # But we don't have persistent state here between runs easily.
        # We can check the Last Modified time of the stats file!
        stats_path = settings.DATA_DIR / f"fixtures/statistics/{fixture_id}.json"
        should_update_stats = True
        if stats_path.exists():
            mtime = datetime.fromtimestamp(stats_path.stat().st_mtime, tz=timezone.utc)
            if datetime.now(timezone.utc) - mtime < timedelta(minutes=9):
                should_update_stats = False
        
        if should_update_stats:
            print("Updating Statistics...")
            stats = FixturesAPI.get_statistics(fixture_id)
            if stats:
                JsonStore.save(stats_path, stats)
        
        # 5. Fetch Lineups (Once)
        lineups_path = settings.DATA_DIR / f"fixtures/lineups/{fixture_id}.json"
        if not lineups_path.exists():
            print("Updating Lineups...")
            lineups = FixturesAPI.get_lineups(fixture_id)
            if lineups:
                JsonStore.save(lineups_path, lineups)

        # 6. Fetch Players Statistics (Every ~20 mins or once at the end? Let's do similar to stats)
        players_stats_path = settings.DATA_DIR / f"fixtures/players/statistics/{fixture_id}.json"
        should_update_players = True
        if players_stats_path.exists():
            mtime = datetime.fromtimestamp(players_stats_path.stat().st_mtime, tz=timezone.utc)
            if datetime.now(timezone.utc) - mtime < timedelta(minutes=19):
                should_update_players = False
        
        if should_update_players:
            print("Updating Players Statistics...")
            players_stats = FixturesAPI.get_players_statistics(fixture_id)
            if players_stats:
                JsonStore.save(players_stats_path, players_stats)

        # 7. Fetch Head To Head (Once)
        home_id = active_match["teams"]["home"]["id"]
        away_id = active_match["teams"]["away"]["id"]
        h2h_id = f"{home_id}-{away_id}"
        h2h_path = settings.DATA_DIR / f"fixtures/headtohead/{h2h_id}.json"
        
        if not h2h_path.exists():
            print(f"Updating Head To Head for {h2h_id}...")
            h2h = FixturesAPI.get_head_to_head(h2h_id)
            if h2h:
                JsonStore.save(h2h_path, h2h)
