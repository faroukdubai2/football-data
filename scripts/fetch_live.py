import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from app.viewmodels.live_vm import LiveViewModel

def main():
    print("--- Starting Live Update ---")
    vm = LiveViewModel()
    vm.check_and_update_live()
    print("--- Live Update Complete ---")

if __name__ == "__main__":
    main()
