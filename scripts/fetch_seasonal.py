import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from app.viewmodels.season_vm import SeasonViewModel

def main():
    print("--- Starting Seasonal Update ---")
    vm = SeasonViewModel()
    vm.update_team_info()
    vm.update_players()
    print("--- Seasonal Update Complete ---")

if __name__ == "__main__":
    main()
