import json
from pathlib import Path

SETTINGS_FILE = Path.home() /'.cpma_gui_settings.json'
 
def save_config_path(path_to_save):
    settings = {"config_path": str(path_to_save)}
    with open(SETTINGS_FILE, 'w') as f:
        json.dump(settings, f)

def load_config_path():
    try:
        with open(SETTINGS_FILE, 'r') as f:
            settings = json.load(f)
            return Path(settings.get("config_path"))
    except (FileNotFoundError, json.JSONDecodeError):
        return None # Path has not been set yet 