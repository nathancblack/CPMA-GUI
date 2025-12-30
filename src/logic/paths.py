import json
import subprocess
import os
from pathlib import Path


class PathManager:
    def __init__(self, config_folder_name="CPMA_Config_Editor", filename="paths.json"):
        # 1. Get the standard Windows AppData folder
        # e.g., C:\Users\Nathaniel\AppData\Roaming
        appdata = os.getenv('APPDATA')

        # 2. Define your specific folder
        self.config_dir = Path(appdata) / config_folder_name

        # 3. Create the folder if it doesn't exist yet
        self.config_dir.mkdir(parents=True, exist_ok=True)

        # 4. Set the full path to the json file
        self.paths_file = self.config_dir / filename

        print(f"Path Manager initialized. Storage: {self.paths_file}")
        self.paths = self._load_paths()
        self.missing = []

    def _load_paths(self):
        # Specifically loads the path mapping from the JSON file
        if self.paths_file.exists():
            with open(self.paths_file, "r") as f:
                return json.load(f)
        return {}

    def _save_paths(self):
        # Specifically writes the path mapping to the JSON file
        with open(self.paths_file, "w") as f:
            json.dump(self.paths, f, indent=4)

    def set_game_root(self, path_str):
        game_root = Path(path_str)

        cpma_dir = game_root / "cpma"
        autoexec = cpma_dir / "autoexec.cfg"

        found_cpma = cpma_dir.exists() and cpma_dir.is_dir()
        found_autoexec = autoexec.exists() and autoexec.is_file()

        self.paths["game_root"] = str(game_root)

        if found_cpma:
            self.paths["cpma_dir"] = str(cpma_dir)
        if found_autoexec:
            self.paths["autoexec"] = str(autoexec)

        self._save_paths()

        if not found_cpma:
            self.missing.append("cpma_dir")
        if not found_autoexec:
            self.missing.append("autoexec")

        return self.missing

    def set_game_exe(self, path_str):
        path = Path(path_str)
        if path.exists() and path.is_file():
            self.paths["game_exe"] = str(path)
            self._save_paths()
            return True
        return False

    def set_specific_path(self, key, path_str):
        self.paths[key] = str(Path(path_str))
        self._save_paths()

    def launch_exe(self):
        cmd = [self.get_path_gameexe(), "+set", "fs_game", "cpma"]
        subprocess.Popen(cmd, cwd=self.get_game_root())

    def get_game_root(self):
        return self.paths.get("game_root")

    def get_path_autoexec(self):
        return self.paths.get("autoexec")

    def get_path_cpma(self):
        return self.paths.get("cpma_dir")

    def get_path_guicfg(self):
        if "cpma_dir" in self.paths:
            return Path(self.paths["cpma_dir"]) / "gui.cfg"
        return None

    def get_path_gameexe(self):
        return self.paths.get("game_exe")