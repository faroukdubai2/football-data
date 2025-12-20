import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from app.viewmodels.fixtures_vm import FixturesViewModel
from app.viewmodels.standings_vm import StandingsViewModel
from app.viewmodels.season_vm import SeasonViewModel

def main():
    print("--- Starting Daily Update ---")
    
    # Fixtures
    fixtures_vm = FixturesViewModel()
    fixtures_vm.update_fixtures()
    fixtures_vm.update_rounds()
    
    # Standings
    standings_vm = StandingsViewModel()
    standings_vm.update_standings()
    
    # Season Check
    season_vm = SeasonViewModel()
    season_vm.update_team_info()

    print("--- Daily Update Complete ---")

if __name__ == "__main__":
    main()
