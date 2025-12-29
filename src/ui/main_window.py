import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from src.logic.paths import PathManager
from src.logic.config_io import load_existing_config, save_current_config
from src.logic.settings import (
    VIDEO_SETTINGS, MOUSE_SETTINGS, AUDIO_SETTINGS,
    HUD_SETTINGS, PLAYER_SETTINGS, WEAPON_SETTINGS, KEYBIND_SETTINGS
)

VALID_KEYS_TEXT = (
    "VALID KEYS REFERENCE:\n"
    "Standard: a-z, 0-9, SPACE, TAB, ENTER, ESCAPE, BACKSPACE\n"
    "Modifiers: SHIFT, CTRL, ALT, CAPSLOCK, COMMAND, PAUSE\n"
    "Symbols: SEMICOLON, BACKSLASH\n"
    "Navigation: INS, DEL, HOME, END, PGUP, PGDN\n"
    "Arrows: UPARROW, DOWNARROW, LEFTARROW, RIGHTARROW\n"
    "Function: F1-F24\n"
    "Mouse: MOUSE1-MOUSE9, MWHEELUP, MWHEELDOWN\n"
    "Keypad: KP_HOME, KP_END, KP_PGUP, KP_PGDN, KP_DEL, KP_INS\n"
    "KP_UPARROW, KP_DOWNARROW, KP_LEFTARROW, KP_RIGHTARROW\n"
    "KP_5, KP_ENTER, KP_PLUS, KP_MINUS, KP_STAR, KP_SLASH\n"
    "KP_EQUALS, KP_NUMLOCK\n"
    "Joystick: JOY1-JOY32"
)

CROSSHAIR_INFO_TEXT = (
    "CROSSHAIR STYLES (0-20):\n"
    "0 = No crosshair\n"
    "1 = Cross\n"
    "2 = Exploded cross\n"
    "3 = Disk + dot\n"
    "4 = Circle + dot\n"
    "5 = Big dot\n"
    "6 = Circle + cross\n"
    "7 = Big exploded cross\n"
    "8 = Big exploded cross + dot\n"
    "9 = Side curves + dot\n"
    "10 = Circle + dot\n"
    "11 = Cross w/ black outline\n"
    "12 = Exploded cross w/ black outline\n"
    "13 = Disk + dot w/ black outline\n"
    "14 = Circle + dot w/ black outline\n"
    "15 = Dot w/ black outline\n"
    "16 = Circle + cross w/ black outline\n"
    "17 = Mirrored L w/ black outline\n"
    "18 = Cross + dot w/ black outlines\n"
    "19 = Side curves + dot w/ black outline\n"
    "20 = Circle + exploded cross + dot"
)
paths = PathManager()

class ScrollableFrame(ttk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.canvas = tk.Canvas(self, highlightthickness=0)
        self.scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.scrollable_content = ttk.Frame(self.canvas)
        self.window_id = self.canvas.create_window((0, 0), window=self.scrollable_content, anchor="nw")

        self.scrollable_content.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )
        self.canvas.bind('<Configure>', self._on_canvas_configure)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")
        self.bind('<Enter>', self._bound_to_mousewheel)
        self.bind('<Leave>', self._unbound_to_mousewheel)

    def _on_canvas_configure(self, event):
        self.canvas.itemconfig(self.window_id, width=event.width)

    def _bound_to_mousewheel(self, event):
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)

    def _unbound_to_mousewheel(self, event):
        self.canvas.unbind_all("<MouseWheel>")

    def _on_mousewheel(self, event):
        if event.num == 5 or event.delta == -120:
            self.canvas.yview_scroll(1, "units")
        elif event.num == 4 or event.delta == 120:
            self.canvas.yview_scroll(-1, "units")



app = tk.Tk()
app.title('CPMA Config Editor')
app.geometry('800x600')

# Format: { 'setting_key': (widget_instance, settings_dictionary_reference) }
widget_map = {}

def select_folder_dialog():
    selected_folder = filedialog.askdirectory(
        title="Select your Quake III Arena folder",
        mustexist=True,
        initialdir="C:/Program Files (x86)"
    )
    if selected_folder:
        paths.set_game_root(selected_folder)
        refresh_path_display()

def select_paths_dialog():

    select_folder_dialog()

    if paths.missing:
        for missing_path in paths.missing:
            if missing_path == "autoexec":
                update_autoexec_path()

            elif missing_path == "cpma_dir":
                update_cpma_path()

    update_gameexe_path()


def refresh_path_display():
    if paths.get_game_root():
        val_label1.config(text=paths.get_game_root())
        val_label2.config(text=paths.get_path_cpma())
        val_label3.config(text=paths.get_path_autoexec())
        val_label4.config(text=paths.get_path_guicfg())

        if paths.get_path_gameexe():
            val_label5.config(text=paths.get_path_gameexe())

        load_to_ui()

def update_q3_path(event=None):
    new_path = filedialog.askdirectory(title="Select Quake 3 Root Folder", mustexist=True)
    if new_path:
        paths.set_game_root(new_path)
        refresh_path_display()

def update_cpma_path(event=None):
    new_path = filedialog.askdirectory(title="Select CPMA Folder", mustexist=True)
    if new_path:
        paths.set_specific_path("cpma_dir", new_path)
        refresh_path_display()


def update_autoexec_path(event=None):
    new_path = filedialog.askopenfilename(
        title="Select Autoexec File",
        initialdir=f"{paths.get_game_root()}"
    )
    if new_path:
        paths.set_specific_path("autoexec", new_path)
        refresh_path_display()

def update_gameexe_path(event=None):
    new_path = filedialog.askopenfilename(
        title="Select Game Executable File",
        initialdir=f"{paths.get_game_root()}"
    )
    if new_path:
        paths.set_game_exe(new_path)
        refresh_path_display()


def export_config_dialog():
    export_path = filedialog.asksaveasfilename(
        title="Export Configuration",
        defaultextension=".cfg",
        filetypes=[("Quake 3 Config", "*.cfg"), ("All Files", "*.*")],
        initialdir=paths.get_game_root(),
        initialfile="my_custom_settings.cfg"
    )

    if export_path:
        sync_widgets_to_logic()

        save_current_config(export_path, None, True)

        print(f"Exported configuration to: {export_path}")

def make_clickable(widget, callback):
    widget.bind("<Button-1>", callback)

    widget.bind("<Enter>", lambda e: widget.config(font=('calibre', 10, 'underline'), cursor="hand2", foreground="blue"))
    widget.bind("<Leave>", lambda e: widget.config(font=('calibre', 10), foreground="black"))



def show_help(event, text):
    tooltip = tk.Toplevel()
    tooltip.wm_overrideredirect(True)
    tooltip.wm_geometry(f"+{event.x_root + 15}+{event.y_root + 10}")

    label = tk.Label(tooltip, text=text, background="#ffffe0", relief="solid", borderwidth=1, justify="left")
    label.pack()

    event.widget.tooltip_window = tooltip


def hide_help(event):
    if hasattr(event.widget, 'tooltip_window'):
        event.widget.tooltip_window.destroy()
        del event.widget.tooltip_window

def load_to_ui():
    cfg_path = paths.get_path_guicfg()
    if not cfg_path:
        print("No config path available yet.")
        return

    print(f"Loading config from: {cfg_path}")

    load_existing_config(cfg_path)

    count = 0
    for key, (widget, settings_dict) in widget_map.items():
        val = settings_dict[key].get('value')

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


def sync_widgets_to_logic():
    for key, (widget, settings_dict) in widget_map.items():
        raw_val = widget.get().strip()

        if raw_val == "":
            settings_dict[key]['value'] = None
        else:
            settings_dict[key]['value'] = raw_val


def save_from_ui():
    sync_widgets_to_logic()

    save_current_config(paths.get_path_guicfg(), paths.get_path_autoexec(), False)

    val_label4.config(text=f"{paths.get_path_guicfg()}")
    print("Config saved.")

def clear_all_inputs():
    count = 0
    for widget, _ in widget_map.values():
        if isinstance(widget, ttk.Entry):
            widget.delete(0, tk.END)
            count += 1

        elif isinstance(widget, ttk.Combobox):
            widget.set("")
            count += 1

# INFO BOX
info_box = ttk.LabelFrame(app, text="Info")
info_box.pack(anchor="n", fill="x", padx=10, pady=10)

info_box.columnconfigure(1, weight=1)

lbl_title1 = ttk.Label(info_box, text="Quake 3 Folder:", font=('calibre', 10, 'bold'))
lbl_title1.grid(row=0, column=0, sticky="w", padx=10, pady=5)
val_label1 = ttk.Label(info_box, text="<Click to set path>", font=('calibre', 10))
val_label1.grid(row=0, column=1, sticky="w", padx=5, pady=5)
make_clickable(val_label1, update_q3_path)

lbl_title2 = ttk.Label(info_box, text="cpma Folder:", font=('calibre', 10, 'bold'))
lbl_title2.grid(row=1, column=0, sticky="w", padx=10, pady=5)
val_label2 = ttk.Label(info_box, text="<Click to set path>", font=('calibre', 10))
val_label2.grid(row=1, column=1, sticky="w", padx=5, pady=5)
make_clickable(val_label2, update_cpma_path)

lbl_title3 = ttk.Label(info_box, text="autoexec:", font=('calibre', 10, 'bold'))
lbl_title3.grid(row=2, column=0, sticky="w", padx=10, pady=5)
val_label3 = ttk.Label(info_box, text="<Click to set path>", font=('calibre', 10))
val_label3.grid(row=2, column=1, sticky="w", padx=5, pady=5)
make_clickable(val_label3, update_autoexec_path)

lbl_title4 = ttk.Label(info_box, text="Generated gui.cfg:", font=('calibre', 10, 'bold'))
lbl_title4.grid(row=4, column=0, sticky="w", padx=10, pady=5)
val_label4 = ttk.Label(info_box, text="...", font=('calibre', 10))
val_label4.grid(row=4, column=1, sticky="w", padx=5, pady=5)

lbl_title5 = ttk.Label(info_box, text="Game Executable:", font=('calibre', 10, 'bold'))
lbl_title5.grid(row=3, column=0, sticky="w", padx=10, pady=5)
val_label5 = ttk.Label(info_box, text="<Click to set path>", font=('calibre', 10))
val_label5.grid(row=3, column=1, sticky="w", padx=5, pady=5)
make_clickable(val_label5, update_gameexe_path)

select_q3_folder_button = ttk.Button(info_box, text='Select Quake III Arena Folder', command=select_paths_dialog)
select_q3_folder_button.grid(row=5, column=0, columnspan=2, sticky="e", padx=10, pady=(5, 10))

# TABS
style = ttk.Style()
style.theme_use('clam')
style.configure('TNotebook.Tab', padding=[20, 2])

tabControl = ttk.Notebook(app)
tabControl.pack(anchor="n", fill="both", expand=True, padx=10, pady=10)

tab1 = ScrollableFrame(tabControl)
tab2 = ScrollableFrame(tabControl)
tab3 = ScrollableFrame(tabControl)
tab4 = ScrollableFrame(tabControl)
tab5 = ScrollableFrame(tabControl)
tab6 = ScrollableFrame(tabControl)
tab7 = ScrollableFrame(tabControl)

tabControl.add(tab1, text="Video")
tabControl.add(tab2, text="Mouse")
tabControl.add(tab3, text="Audio")
tabControl.add(tab4, text="Hud")
tabControl.add(tab5, text="Player")
tabControl.add(tab6, text="Weapons")
tabControl.add(tab7, text="Keybinds")

tabs_data = [
    (tab1, VIDEO_SETTINGS),
    (tab2, MOUSE_SETTINGS),
    (tab3, AUDIO_SETTINGS),
    (tab4, HUD_SETTINGS),
    (tab5, PLAYER_SETTINGS),
    (tab6, WEAPON_SETTINGS),
    (tab7, KEYBIND_SETTINGS)
]

for current_tab, current_settings in tabs_data:
    parent_frame = current_tab.scrollable_content
    row_i = 0

    parent_frame.columnconfigure(1, weight=1)

    if current_settings is KEYBIND_SETTINGS:
        for i in current_settings:
            ttk.Label(parent_frame, text=current_settings[i]["label"], font=('calibre', 10, 'bold')).grid(row=row_i, column=0, sticky='w', pady=5, padx=(0, 10))

            w = ttk.Entry(parent_frame, width=15)
            w.grid(row=row_i, column=1, sticky='w', pady=5)

            if row_i == 1:
                help_icon = ttk.Label(parent_frame, text="[?]", foreground="blue", cursor="hand2")
                help_icon.grid(row=row_i, column=2, sticky='w', padx=5)

                help_icon.bind("<Enter>", lambda e: show_help(e, VALID_KEYS_TEXT))
                help_icon.bind("<Leave>", hide_help)

            widget_map[i] = (w, current_settings)

            row_i += 1
    else:
        for i in current_settings:
            ttk.Label(parent_frame, text=current_settings[i]["label"], font=('calibre', 10, 'bold')) \
                .grid(row=0 + row_i, column=0, sticky='nw', pady=(15, 0),
                      padx=(0, 15))

            desc_label = ttk.Label(
                parent_frame,
                text=current_settings[i]["description"],
                font=('calibre', 10),
                justify="left"
            )

            desc_label.grid(row=0 + row_i, column=1, sticky='ew', pady=(15, 0))

            desc_label.bind('<Configure>', lambda e: e.widget.config(wraplength=e.width))
            if 'min' in current_settings[i]:
                ttk.Label(parent_frame,
                          text=f"<{current_settings[i]['min']} to {current_settings[i]['max']}> (default: {current_settings[i].get('game_default', '')})",
                          font=('calibre', 10, 'bold')).grid(row=1 + row_i, column=1, sticky='w')
            else:
                ttk.Label(parent_frame, text=f"(default: {current_settings[i].get('game_default', 'N/A')})",
                          font=('calibre', 10, 'bold')).grid(row=1 + row_i, column=1, sticky='w')

            w = None
            if current_settings[i]['type'] in ["float", "int"]:
                w = ttk.Entry(parent_frame, width=8)
            elif current_settings[i]['type'] == "bool":
                w = ttk.Combobox(parent_frame, values=["", "0", "1"], state="readonly", width=6)
            elif current_settings[i]['type'] == "discrete":
                w = ttk.Combobox(parent_frame, values=["", "0", "1", "2"], state="readonly", width=7)
            elif current_settings[i]['type'] == "string":
                w = ttk.Entry(parent_frame, width=20)

            if w:
                w.grid(column=0, row=1 + row_i, sticky='w')
                if i == "cg_drawCrosshair":
                    help_icon = ttk.Label(parent_frame, text="[?]", foreground="blue", cursor="hand2")
                    help_icon.grid(row=1 + row_i, column=1, sticky='e', padx=5)

                    help_icon.bind("<Enter>", lambda e: show_help(e, CROSSHAIR_INFO_TEXT))
                    help_icon.bind("<Leave>", hide_help)
                widget_map[i] = (w, current_settings)

            row_i += 2

button_frame = ttk.Frame(app)
button_frame.pack(anchor="se", padx=20, pady=(0, 10))
export_button = ttk.Button(button_frame, text='Export Config', command=export_config_dialog)
export_button.pack(side="left", padx=5)

clear_button = ttk.Button(button_frame, text='Clear Inputs', command=clear_all_inputs)
clear_button.pack(side="left", padx=5)

launch_game_button = ttk.Button(button_frame, text='Launch Game', command=paths.launch_exe)
launch_game_button.pack(side="left", padx=5)

save_config_button = ttk.Button(button_frame, text='Save Config', command=save_from_ui)
save_config_button.pack(side="left", padx=5)


if paths.get_game_root():
    refresh_path_display()

app.mainloop()