from .base_api import BaseAPI

class PlayersAPI(BaseAPI):
    @staticmethod
    def get_players(season: int, team_id: int):
        # Note: This endpoint is paginated. 
        # For a single team, it usually fits in 1-2 pages (20 players per page).
        # We might need to handle paging if we want ALL players. 
        # For simplicity and budget, we'll fetch page 1. 
        # Ideally we loop pages, but that consumes quota.
        # "Seasonal" workflow runs rarely so we can loop.
        
        all_players = []
        page = 1
        while True:
            data = BaseAPI._get("players", {"season": season, "team": team_id, "page": page})
            if not data or "response" not in data:
                break
            
            all_players.extend(data["response"])
            
            paging = data.get("paging", {})
            if paging.get("current", 1) >= paging.get("total", 1):
                break
            page += 1
            
        # Reconstruct a single response object to match API structure
        return {
            "get": "players",
            "parameters": {"season": season, "team": team_id},
            "errors": [],
            "results": len(all_players),
            "paging": {"current": 1, "total": 1},
            "response": all_players
        }
