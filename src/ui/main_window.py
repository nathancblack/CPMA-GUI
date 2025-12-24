import customtkinter as ctk
import tkinter as tk  # We still need this for BooleanVar/StringVar
from tkinter import messagebox
from src.logic import config_io, paths
from src.logic.settings import (
    VIDEO_SETTINGS,
    MOUSE_SETTINGS,
    AUDIO_SETTINGS,
    HUD_SETTINGS,
    PLAYER_SETTINGS,
    WEAPON_SETTINGS
)

# Initialize CustomTkinter settings
ctk.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

TABS_MAPPING = [
    ("Video", VIDEO_SETTINGS),
    ("Mouse", MOUSE_SETTINGS),
    ("Audio", AUDIO_SETTINGS),
    ("HUD", HUD_SETTINGS),
    ("Player", PLAYER_SETTINGS),
    ("Weapons", WEAPON_SETTINGS)
]


class ConfigApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("CPMA Config Editor")
        self.geometry("800x750")

        self.gui_vars = {}
        self.enabled_vars = {}
        self.widgets = {}

        self._create_layout()

    def _create_layout(self):
        # 1. Main TabView (Replaces Notebook)
        self.tabview = ctk.CTkTabview(self)
        self.tabview.pack(expand=True, fill="both", padx=20, pady=20)

        # 2. Generate Tabs
        for tab_name, settings_dict in TABS_MAPPING:
            self._build_tab(tab_name, settings_dict)

        # 3. Save Button Area
        btn_frame = ctk.CTkFrame(self, fg_color="transparent")
        btn_frame.pack(fill="x", padx=20, pady=20)

        save_btn = ctk.CTkButton(btn_frame, text="Save Configuration", command=self.save_config, width=200)
        save_btn.pack(side="right")

        cancel_btn = ctk.CTkButton(btn_frame, text="Exit", command=self.destroy, fg_color="transparent", border_width=2,
                                   text_color=("gray10", "#DCE4EE"))
        cancel_btn.pack(side="right", padx=10)

    def _build_tab(self, name, settings_dict):
        """Creates a new tab and populates it."""
        # Create the tab
        self.tabview.add(name)
        tab_root = self.tabview.tab(name)

        # Create a scrollable frame inside the tab
        scroll_frame = ctk.CTkScrollableFrame(tab_root, fg_color="transparent")
        scroll_frame.pack(fill="both", expand=True)

        # --- WIDGET GENERATION LOOP ---
        row = 0
        for command, data in settings_dict.items():
            label_text = data.get("label", command)
            desc_text = data.get("description", "")

            # 1. Decide if active
            current_val = data.get("value")
            is_active = current_val is not None

            # 2. "Enable" Checkbox
            # Note: CustomTkinter CheckBox uses 1/0 for on/off by default when using IntVar,
            # but for BooleanVar it works natively.
            enable_var = tk.BooleanVar(value=is_active)
            self.enabled_vars[command] = enable_var

            enable_chk = ctk.CTkCheckBox(
                scroll_frame,
                text="",
                variable=enable_var,
                width=24,
                height=24
            )
            enable_chk.grid(row=row, column=0, padx=(10, 5), pady=(10, 0), sticky="nw")

            # 3. Label
            lbl = ctk.CTkLabel(scroll_frame, text=label_text, font=ctk.CTkFont(size=13, weight="bold"))
            lbl.grid(row=row, column=1, sticky="w", padx=5, pady=(10, 0))

            # 4. Widget
            widget = self._create_widget_for_type(scroll_frame, command, data, current_val)
            widget.grid(row=row, column=2, sticky="ew", padx=10, pady=(10, 0))

            self.widgets[command] = widget

            # 5. Toggle Logic
            def toggle_state(w=widget, v=enable_var):
                state = "normal" if v.get() else "disabled"
                try:
                    w.configure(state=state)
                except:
                    # Some complex widgets (like frames) might need recursive disabling
                    pass

            enable_chk.configure(command=toggle_state)
            toggle_state()  # Set initial

            # 6. Description
            if desc_text:
                desc_lbl = ctk.CTkLabel(
                    scroll_frame,
                    text=desc_text,
                    font=ctk.CTkFont(size=11),
                    text_color="gray"
                )
                desc_lbl.grid(row=row + 1, column=1, columnspan=2, sticky="w", padx=5, pady=(0, 5))
                row += 2
            else:
                row += 1

        # Configure grid weight so widgets expand
        scroll_frame.grid_columnconfigure(2, weight=1)

    def _create_widget_for_type(self, parent, command, data, loaded_value):
        data_type = data.get("type")
        display_value = loaded_value if loaded_value is not None else data.get("game_default", "")

        # --- CHECKBOX (Boolean) ---
        if data_type == "bool":
            # CTkCheckBox needs specific string values if we use StringVar
            var = tk.StringVar(value=display_value)
            self.gui_vars[command] = var
            return ctk.CTkCheckBox(parent, text="Enabled", variable=var, onvalue="1", offvalue="0")

        # --- DROPDOWN (Discrete) ---
        elif data_type == "discrete":
            var = tk.StringVar(value=display_value)
            self.gui_vars[command] = var

            options = data.get("options", [])
            values = list(options.values()) if isinstance(options, dict) else options

            # Convert all to strings to be safe
            values = [str(v) for v in values]

            return ctk.CTkComboBox(parent, variable=var, values=values, state="readonly")

        # --- SLIDER (Float/Int) ---
        elif data_type in ["float", "int"]:
            try:
                numeric_val = float(display_value)
            except ValueError:
                numeric_val = float(data.get("min", 0))

            var = tk.DoubleVar(value=numeric_val)
            self.gui_vars[command] = var

            min_val = float(data.get("min", 0))
            max_val = float(data.get("max", 10))

            # Frame to hold slider + value label
            frame = ctk.CTkFrame(parent, fg_color="transparent")

            val_lbl = ctk.CTkLabel(frame, text=f"{numeric_val:.2f}", width=40)
            val_lbl.pack(side="right", padx=5)

            slider = ctk.CTkSlider(
                frame,
                from_=min_val,
                to=max_val,
                variable=var,
                command=lambda v: val_lbl.configure(text=f"{float(v):.2f}")
            )
            slider.pack(side="left", fill="x", expand=True)

            return frame

        # --- ENTRY (Default) ---
        else:
            var = tk.StringVar(value=display_value)
            self.gui_vars[command] = var
            return ctk.CTkEntry(parent, textvariable=var)

    def save_config(self):
        for tab_name, settings_dict in TABS_MAPPING:
            for command, data in settings_dict.items():
                is_enabled = self.enabled_vars[command].get()
                if is_enabled:
                    new_val = self.gui_vars[command].get()
                    data["value"] = str(new_val)
                else:
                    data["value"] = None

        cfg_path = paths.get_gui_cfg_path()
        if cfg_path:
            config_io.save_current_config(cfg_path)
            messagebox.showinfo("Success", "Configuration saved successfully!")
        else:
            messagebox.showerror("Error", "Could not find config path.")


if __name__ == "__main__":
    paths.init_paths()
    config_io.load_existing_config(paths.get_gui_cfg_path())
    app = ConfigApp()
    app.mainloop()