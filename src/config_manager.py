from pathlib import Path
from .settings_manager import load_config_path 
import re

def get_config_file_path():
    """
    Utility function to get the current valid config path.
    You'll call this once at the start of your operations.
    """
    config_path = load_config_path()
    if not config_path:
        raise FileNotFoundError("Config path is not set in application settings.")
    return config_path

def get_value(key_to_find):
    """
    Finds and returns the value for a given key in the user's config file.
    """
    try:
        # 1. Get the validated Path object
        file_path = get_config_file_path()

        # 2. Use the Path object for the file operation
        # This will open the correct user file (e.g., /Users/UserA/quake3/cpma/q3config.txt)
        with open(file_path, 'r') as f:
            full_text = f.read()

        # 3. Apply the regex logic
        pattern = re.compile(rf'{key_to_find}\s+"(.*?)"')
        match = pattern.search(full_text)

        if match:
            return match.group(1)
        else:
            # The key might not exist in the file, which is fine
            return None

    except FileNotFoundError as e:
        print(f"Error accessing file: {e}")
        # In the real app, this error would be shown to the user in the GUI
        return None