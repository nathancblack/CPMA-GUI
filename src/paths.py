import tkinter as tk
from tkinter import filedialog
from pathlib import Path

# Prompt user to select Quake 3 folder
quake_dir = filedialog.askdirectory(
    title="Select your Quake III Arena folder",
    initialdir="C:/Program Files (x86)"
)

if quake_dir:
    # Convert string to Path object
    quake_dir = Path(quake_dir)
    print(f"Selected folder: {quake_dir}")
    
    # Define paths (now this will work)
    cpma_dir = quake_dir / "cpma"
    autoexec_path = cpma_dir / "autoexec.cfg"
    gui_path = cpma_dir / "gui.cfg"
else:
    print("No folder selected")