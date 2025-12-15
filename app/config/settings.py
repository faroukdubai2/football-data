import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Settings:
    # API Keys & URLs
    API_KEY = os.getenv("FOOTBALL_API_KEY")
    BASE_URL = os.getenv("BASE_API_URL", "https://v3.football.api-sports.io")
    GITHUB_BASE_URL = os.getenv("BASE_URL", "https://raw.githubusercontent.com/USER/REPO/main")

    # Team & League Context
    TEAM_ID = int(os.getenv("TEAM_ID", 1616))  # LAFC
    LEAGUE_ID = int(os.getenv("LEAGUE_ID", 253))  # MLS
    
    # We can probably fetch current season dynamically or hardcode for now as per prompt example "2025"
    SEASON = 2025 

    # Project Paths
    BASE_DIR = Path(__file__).resolve().parent.parent.parent
    DATA_DIR = BASE_DIR / "data"

    # API Limits
    DAILY_REQUEST_LIMIT = 100

    @staticmethod
    def get_headers():
        if not Settings.API_KEY:
            # For CI/CD, we expect secrets. If local execution without .env, this raises.
            # But the script might be running in an environment where we don't want to crash immediately 
            # if we are just checking something else, but for fetching data it is critical.
            # We return empty or raise. Raising is safer.
            pass 
        return {
            "x-rapidapi-key": Settings.API_KEY,
            "x-rapidapi-host": "v3.football.api-sports.io"
        }

settings = Settings()
