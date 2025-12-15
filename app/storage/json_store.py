import json
import os
from pathlib import Path
from typing import Any, Dict

class JsonStore:
    @staticmethod
    def save(path: Path, data: Any) -> bool:
        """
        Saves data to JSON file. Returns True if file was updated, False if skipped (unchanged).
        """
        # Ensure directory exists
        path.parent.mkdir(parents=True, exist_ok=True)

        # Check existing data
        if path.exists():
            try:
                with open(path, 'r', encoding='utf-8') as f:
                    existing_data = json.load(f)
                
                # If data is identical, skip write
                if existing_data == data:
                    print(f"Values unchanged for {path}, skipping.")
                    return False
            except (json.JSONDecodeError, OSError):
                pass # Overwrite if corrupt

        # Write new data
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        
        print(f"Saved update to {path}")
        return True
