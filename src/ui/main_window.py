import os
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

from src.logic.config_io import load_existing_config, save_current_config
from src.logic.installer import get_install_path, install_assets
from src.logic.paths import PathManager
from src.logic.settings import (
    AUDIO_SETTINGS,
    HUD_SETTINGS,
    KEYBIND_SETTINGS,
    MOUSE_SETTINGS,
    PLAYER_SETTINGS,
    VIDEO_SETTINGS,
    WEAPON_SETTINGS,
)
from src.ui.components import ScrollableFrame, hide_help, make_clickable, show_help
from src.ui.constants import CROSSHAIR_INFO_TEXT, VALID_KEYS_TEXT
from src.ui.dialogs import prompt_setup_choice


class CPMAApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("CPMA Config Editor")
        self.geometry("800x600")

        self.paths = PathManager()
        self.widget_map = {}

        self._build_info_box()
        self._build_buttons()
        self._build_tabs()

        self._check_startup()

    def _check_startup(self):
        if self.paths.get_game_root():
            self.refresh_path_display()
        else:
            choice = prompt_setup_choice(self, install_assets)

            if choice == "install_success":
                print("Installation finished successfully.")
                root_path = os.path.join(
                    get_install_path(), "assets", "QUAKE3_CPMA_ASSETS"
                )
                exe_path = os.path.join(root_path, "cnq3-x64.exe")

                self.paths.set_game_root(root_path)
                self.paths.set_game_exe(exe_path)

                self.refresh_path_display()
                self.deiconify()

            elif choice == "locate":
                self.select_paths_dialog()
                self.deiconify()

            elif choice == "install_failed":
                self.destroy()

            else:
                self.destroy()

    def _build_info_box(self):
        info_box = ttk.Frame(self, borderwidth=2, relief="groove")
        info_box.pack(anchor="n", fill="both", padx=10, pady=15)
        info_box.columnconfigure(1, weight=1)

        _, self.val_q3_path = self._create_info_row(
            info_box, 0, "Quake 3 Folder:", self.update_q3_path
        )
        _, self.val_cpma_path = self._create_info_row(
            info_box, 1, "cpma Folder:", self.update_cpma_path
        )
        _, self.val_autoexec_path = self._create_info_row(
            info_box, 2, "autoexec Config:", self.update_autoexec_path
        )
        _, self.val_exe_path = self._create_info_row(
            info_box, 3, "Game Executable:", self.update_gameexe_path
        )

        select_btn = ttk.Button(
            info_box,
            text="Select Quake III Arena Folder",
            command=self.select_paths_dialog,
        )
        select_btn.grid(
            row=4, column=0, columnspan=2, sticky="e", padx=10, pady=(5, 10)
        )

    def _create_info_row(self, parent, row, title, command):
        lbl = ttk.Label(parent, text=title, font=("calibre", 10, "bold"))
        lbl.grid(row=row, column=0, sticky="w", padx=10, pady=5)

        val = ttk.Label(parent, text="<Click to set path>", font=("calibre", 10))
        val.grid(row=row, column=1, sticky="w", padx=5, pady=5)
        make_clickable(val, command)
        return lbl, val

    def _build_tabs(self):
        self.style = ttk.Style()
        self.style.theme_use("clam")

        self.style.configure("TNotebook.Tab", padding=[36, 2], focuscolor="")
        self.style.map("TNotebook.Tab", padding=[("selected", [36, 2])])

        self.style.map(
            "TCombobox",
            fieldbackground=[("readonly", "#ffffff")],
            selectbackground=[("readonly", "#ffffff")],
            selectforeground=[("readonly", "#000000")],
        )

        self.bg_color = self.style.lookup("TFrame", "background")

        self.tabControl = ttk.Notebook(self)
        self.tabControl.pack(
            anchor="n", fill="both", expand=True, padx=10, pady=(0, 10)
        )

        tabs_data = [
            ("Video", VIDEO_SETTINGS),
            ("Mouse", MOUSE_SETTINGS),
            ("Audio", AUDIO_SETTINGS),
            ("Hud", HUD_SETTINGS),
            ("Player", PLAYER_SETTINGS),
            ("Weapons", WEAPON_SETTINGS),
            ("Keybinds", KEYBIND_SETTINGS),
        ]

        self.tab_names = [name for name, _ in tabs_data]

        for tab_name, settings_data in tabs_data:
            frame = ScrollableFrame(self.tabControl)
            self.tabControl.add(frame, text=tab_name)

            self._populate_tab(frame.scrollable_content, settings_data)

        self.tabControl.bind("<Configure>", self._on_tab_configure)

    def _on_tab_configure(self, event):
        num_tabs = len(self.tab_names)
        if num_tabs == 0:
            return

        notebook_width = event.width
        tab_width = max(1, notebook_width // num_tabs)

        self.style.configure(
            "TNotebook.Tab", width=tab_width, padding=[5, 2], anchor="center"
        )
        self.style.map("TNotebook.Tab", padding=[("selected", [5, 2])])

    def _forward_scroll(self, event, canvas):
        canvas.event_generate("<MouseWheel>", delta=event.delta)
        return "break"

    def _populate_tab(self, parent_frame, current_settings):
        row_i = 0
        parent_frame.columnconfigure(1, weight=1)

        # SPECIAL HANDLING FOR KEYBINDS
        if current_settings is KEYBIND_SETTINGS:
            for i in current_settings:
                ttk.Label(
                    parent_frame,
                    text=current_settings[i]["label"],
                    font=("calibre", 10, "bold"),
                ).grid(row=row_i, column=0, sticky="w", pady=5, padx=10)
                w = ttk.Entry(parent_frame, width=15)
                w.grid(row=row_i, column=1, sticky="w", pady=5)

                if row_i == 1:
                    help_icon = ttk.Label(
                        parent_frame, text="[?]", foreground="blue", cursor="hand2"
                    )
                    help_icon.grid(row=row_i, column=2, sticky="w", padx=5)
                    help_icon.bind("<Enter>", lambda e: show_help(e, VALID_KEYS_TEXT))
                    help_icon.bind("<Leave>", hide_help)

                self.widget_map[i] = (w, current_settings)
                row_i += 1

        # STANDARD SETTINGS
        else:
            parent_frame.columnconfigure(0, weight=0)
            for i in current_settings:
                # Left column: fixed-width frame containing title + entry/combobox
                top_pady = 20 if row_i == 0 else 10
                left_frame = tk.Frame(
                    parent_frame, width=140, height=44, bg=self.bg_color
                )
                left_frame.grid(
                    row=row_i,
                    column=0,
                    sticky="nw",
                    padx=(10, 15),
                    pady=(top_pady, 10),
                )
                left_frame.grid_propagate(False)

                title_label = ttk.Label(
                    left_frame,
                    text=current_settings[i]["label"],
                    font=("calibre", 10, "bold"),
                )
                title_label.place(x=0, y=0)

                widget_frame = tk.Frame(left_frame, width=120, height=24)
                widget_frame.pack_propagate(False)
                widget_frame.place(x=0, y=20)

                setting_type = current_settings[i]["type"]
                canvas = parent_frame.master.master

                if setting_type in ["float", "int", "bitmask", "string"]:
                    w = ttk.Entry(widget_frame)
                elif setting_type == "bool":
                    w = ttk.Combobox(
                        widget_frame, values=["", "0", "1"], state="readonly"
                    )
                    w.bind(
                        "<MouseWheel>", lambda e, c=canvas: self._forward_scroll(e, c)
                    )
                elif setting_type == "discrete":
                    w = ttk.Combobox(
                        widget_frame, values=["", "0", "1", "2"], state="readonly"
                    )
                    w.bind(
                        "<MouseWheel>", lambda e, c=canvas: self._forward_scroll(e, c)
                    )

                w.pack(fill="both", expand=True)

                # Right column: frame containing description + default value
                right_frame = ttk.Frame(parent_frame)
                right_frame.grid(
                    row=row_i,
                    column=1,
                    sticky="new",
                    padx=(0, 10),
                    pady=(top_pady, 10),
                )

                desc_label = ttk.Label(
                    right_frame,
                    text=current_settings[i]["description"],
                    font=("calibre", 10),
                    justify="left",
                )
                desc_label.pack(anchor="w", fill="x")
                desc_label.bind(
                    "<Configure>", lambda e: e.widget.config(wraplength=e.width)
                )

                if i == "cg_drawCrosshair":
                    help_icon = ttk.Label(
                        right_frame, text="[?]", foreground="blue", cursor="hand2"
                    )
                    help_icon.place(relx=1.0, x=-20, y=0)
                    help_icon.bind(
                        "<Enter>", lambda e: show_help(e, CROSSHAIR_INFO_TEXT)
                    )
                    help_icon.bind("<Leave>", hide_help)

                if "min" in current_settings[i]:
                    ttk.Label(
                        right_frame,
                        text=f"<{current_settings[i]['min']} to {current_settings[i]['max']}> (default: {current_settings[i].get('game_default', '')})",
                        font=("calibre", 10, "bold"),
                    ).pack(anchor="w")
                else:
                    ttk.Label(
                        right_frame,
                        text=f"(default: {current_settings[i].get('game_default', 'N/A')})",
                        font=("calibre", 10, "bold"),
                    ).pack(anchor="w")

                self.widget_map[i] = (w, current_settings)

                row_i += 1

    def _build_buttons(self):
        button_frame = tk.Frame(self, bg=self.cget("bg"))
        button_frame.pack(side="bottom", fill="x", padx=10, pady=(0, 10))

        # Left side - Clear Inputs
        ttk.Button(
            button_frame, text="Clear Inputs", command=self.confirm_clear_inputs
        ).pack(side="left")

        # Right side - other buttons
        ttk.Button(button_frame, text="Save Config", command=self.save_from_ui).pack(
            side="right"
        )
        ttk.Button(
            button_frame, text="Launch Game", command=self.paths.launch_exe
        ).pack(side="right", padx=5)
        ttk.Button(
            button_frame, text="Export Config", command=self.export_config_dialog
        ).pack(side="right", padx=5)

    def confirm_clear_inputs(self):
        if messagebox.askyesno(
            "Clear Inputs", "Are you sure you want to clear all the input boxes?"
        ):
            self.clear_all_inputs()

    # --- FUNCTIONALITY METHODS ---

    def select_folder_dialog(self):
        selected_folder = filedialog.askdirectory(
            title="Select your Quake III Arena folder",
            mustexist=True,
            initialdir="C:/Program Files (x86)",
        )
        if selected_folder:
            self.paths.set_game_root(selected_folder)
            self.refresh_path_display()

    def select_paths_dialog(self):
        self.select_folder_dialog()
        if self.paths.missing:
            for missing_path in self.paths.missing:
                if missing_path == "autoexec":
                    self.update_autoexec_path()
                elif missing_path == "cpma_dir":
                    self.update_cpma_path()
        self.update_gameexe_path()

    def refresh_path_display(self):
        if self.paths.get_game_root():
            self.val_q3_path.config(text=self.paths.get_game_root())
            self.val_cpma_path.config(text=self.paths.get_path_cpma())
            self.val_autoexec_path.config(text=self.paths.get_path_autoexec())
            if self.paths.get_path_gameexe():
                self.val_exe_path.config(text=self.paths.get_path_gameexe())
            self.load_to_ui()

    def update_q3_path(self, event=None):
        new_path = filedialog.askdirectory(
            title="Select Quake 3 Root Folder", mustexist=True
        )
        if new_path:
            self.paths.set_game_root(new_path)
            self.refresh_path_display()

    def update_cpma_path(self, event=None):
        new_path = filedialog.askdirectory(title="Select CPMA Folder", mustexist=True)
        if new_path:
            self.paths.set_specific_path("cpma_dir", new_path)
            self.refresh_path_display()

    def update_autoexec_path(self, event=None):
        new_path = filedialog.askopenfilename(
            title="Select Autoexec File", initialdir=f"{self.paths.get_game_root()}"
        )
        if new_path:
            self.paths.set_specific_path("autoexec", new_path)
            self.refresh_path_display()

    def update_gameexe_path(self, event=None):
        new_path = filedialog.askopenfilename(
            title="Select Game Executable File",
            initialdir=f"{self.paths.get_game_root()}",
        )
        if new_path:
            self.paths.set_game_exe(new_path)
            self.refresh_path_display()

    def export_config_dialog(self):
        export_path = filedialog.asksaveasfilename(
            title="Export Configuration",
            defaultextension=".cfg",
            filetypes=[("Quake 3 Config", "*.cfg"), ("All Files", "*.*")],
            initialdir=self.paths.get_game_root(),
            initialfile="my_custom_settings.cfg",
        )
        if export_path:
            self.sync_widgets_to_logic()
            save_current_config(export_path, None, True)
            print(f"Exported configuration to: {export_path}")

    def load_to_ui(self):
        cfg_path = self.paths.get_path_guicfg()
        if not cfg_path:
            print("No config path available yet.")
            return

        print(f"Loading config from: {cfg_path}")
        load_existing_config(cfg_path)

        count = 0
        for key, (widget, settings_dict) in self.widget_map.items():
            val = settings_dict[key].get("value")

            if isinstance(widget, ttk.Entry):
                widget.delete(0, tk.END)
            elif isinstance(widget, ttk.Combobox):
                widget.set("")

            if val is not None:
                str_val = str(val)
                if isinstance(widget, ttk.Entry):
                    widget.insert(0, str_val)
                elif isinstance(widget, ttk.Combobox):
                    widget.set(str_val)
                count += 1
        print(f"UI populated. {count} fields updated.")

    def sync_widgets_to_logic(self):
        for key, (widget, settings_dict) in self.widget_map.items():
            raw_val = widget.get().strip()
            if raw_val == "":
                settings_dict[key]["value"] = None
            else:
                settings_dict[key]["value"] = raw_val

    def save_from_ui(self):
        self.sync_widgets_to_logic()
        save_current_config(
            self.paths.get_path_guicfg(), self.paths.get_path_autoexec(), False
        )
        print("Config saved.")

    def clear_all_inputs(self):
        for widget, _ in self.widget_map.values():
            if isinstance(widget, ttk.Combobox):
                if widget["values"]:
                    widget.current(0)
            elif isinstance(widget, ttk.Entry):
                widget.delete(0, tk.END)


if __name__ == "__main__":
    app = CPMAApp()
    app.mainloop()
