import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from app.viewmodels.season_vm import SeasonViewModel

def main():
    print("--- Starting Annual Update ---")
    vm = SeasonViewModel()
    # Team info updates venue info as well
    vm.update_team_info()
    print("--- Annual Update Complete ---")

if __name__ == "__main__":
    main()
