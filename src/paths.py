import json
import tkinter as tk
from pathlib import Path
from tkinter import filedialog


def load_paths_json():
    paths_file = Path("Q3Arena_path.json")
    if paths_file.exists():
        try:
            with open(paths_file, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return {}
    return {}


def save_paths_json(config):
    with open("Q3Arena_path.json", "w") as f:
        json.dump(config, f, indent=2)


def calculate_paths(Q3Arena_path):
    Q3Arena_path = Path(Q3Arena_path)
    cpma_dir = Q3Arena_path / "cpma"
    autoexec_cfg_file = cpma_dir / "autoexec.cfg"
    gui_cfg_file = cpma_dir / "gui.cfg"

    # Validate required paths
    if not Q3Arena_path.exists():
        raise FileNotFoundError(f"Quake directory not found: {Q3Arena_path}")
    if not cpma_dir.exists():
        raise FileNotFoundError(f"CPMA directory not found: {cpma_dir}")
    if not autoexec_cfg_file.exists():
        raise FileNotFoundError(f"autoexec.cfg not found: {autoexec_cfg_file}")

    return {
        "Q3Arena_path": Q3Arena_path,
        "cpma_dir": cpma_dir,
        "autoexec_cfg_file": autoexec_cfg_file,
        "gui_cfg_file": gui_cfg_file,
    }


def load_or_prompt_paths():
    config = load_paths_json()

    # Try to use existing Q3Arena_path
    if "Q3Arena_path" in config:
        try:
            return calculate_paths(config["Q3Arena_path"])
        except FileNotFoundError:
            pass  # Fall through to prompt user
    Q3Arena_path = filedialog.askdirectory(
        title="Select your Quake III Arena folder", initialdir="C:/Program Files (x86)"
    )

    if not Q3Arena_path:
        print("No folder selected")
        return None

    try:
        paths = calculate_paths(Q3Arena_path)
        save_paths_json({"Q3Arena_path": str(Q3Arena_path)})
        print(f"Selected folder: {Q3Arena_path}")
        return paths
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return None


# Usage
paths = load_or_prompt_paths()
