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

def get_key_for_action(action_to_find):
    """
    Finds which key is bound to a specific action.
    Example: get_key_for_action("weapon 2") would return "f"
    """
    try:
        file_path = get_config_file_path() # Assumes this function exists
        with open(file_path, 'r') as f:
            full_text = f.read()

        action_re = re.escape(action_to_find)

        # Regex:
        # bind\s+    -> Find "bind" plus one or more spaces
        # (\S+)      -> Capture (group 1) one or more non-space chars (this is the key)
        # \s+        -> Find one or more spaces
        # "{action}" -> Find the action string (e.g., "weapon 2") in quotes
        pattern = re.compile(rf'bind\s+(\S+)\s+"{action_re}"')
        match = pattern.search(full_text)

        if match:
            return match.group(1) # This returns the captured key, e.g., "f"
        else:
            return "" # No key is bound

    except FileNotFoundError:
        return ""