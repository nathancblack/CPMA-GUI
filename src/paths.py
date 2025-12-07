import json
import tkinter as tk
from pathlib import Path
from tkinter import filedialog


def load_json_config():
    file = Path("Q3Arena_path.json")
    if file.exists():
        try:
            with open(file, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return {}
    return {}


def write_json_config(config):
    with open("Q3Arena_path.json", "w") as f:
        json.dump(config, f, indent=2)


def build_paths(Q3Arena_path):
    Q3Arena_path = Path(Q3Arena_path)
    cpma_path = Q3Arena_path / "cpma"
    autoexec_cfg_path = cpma_path / "autoexec.cfg"
    gui_cfg_path = cpma_path / "gui.cfg"

    # Validate required paths
    if not Q3Arena_path.exists():
        raise FileNotFoundError(f"Quake directory not found: {Q3Arena_path}")
    if not cpma_path.exists():
        raise FileNotFoundError(f"CPMA directory not found: {cpma_path}")
    if not autoexec_cfg_path.exists():
        raise FileNotFoundError(f"autoexec.cfg not found: {autoexec_cfg_path}")

    return {
        "Q3Arena_path": Q3Arena_path,
        "cpma_path": cpma_path,
        "autoexec_cfg_path": autoexec_cfg_path,
        "gui_cfg_path": gui_cfg_path,
    }


def init_paths():
    config = load_json_config()

    # Try to use existing Q3Arena_path
    if "Q3Arena_path" in config:
        try:
            return build_paths(config["Q3Arena_path"])
        except FileNotFoundError:
            pass  # Fall through to prompt user
    Q3Arena_path = filedialog.askdirectory(
        title="Select your Quake III Arena folder", initialdir="C:/Program Files (x86)"
    )

    if not Q3Arena_path:
        print("No folder selected")
        return None

    try:
        paths = build_paths(Q3Arena_path)
        write_json_config({"Q3Arena_path": str(Q3Arena_path)})
        print(f"Selected folder: {Q3Arena_path}")
        return paths
    except FileNotFoundError as error:
        print(f"Error: {error}")
        return None


# Usage
paths = init_paths()
