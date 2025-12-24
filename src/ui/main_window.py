import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

from src.logic.paths import PathManager
from src.logic.settings import VIDEO_SETTINGS
paths = PathManager()

app = tk.Tk()
app.title('CPMA Config Editor')
app.geometry('800x600')

def select_folder_dialog():
    selected_folder = filedialog.askdirectory(
        title="Select your Quake III Arena folder",
        mustexist=True,
        initialdir="C:/Program Files (x86)"
    )
    paths.set_game_root(selected_folder)

    label1.config(text=f"Quake 3 Folder Path:  {paths.get_game_root()}")
    label2.config(text=f"cpma Folder Path:  {paths.get_path_cpma()}")
    label3.config(text=f"autoexec Location:  {paths.get_path_autoexec()}")


def save():
    # generate gui file
    # write to gui file
    label4.config(text=f"Generated gui.cfg Location:  {paths.get_path_guicfg()}")


# INFO BOX
info_box = ttk.LabelFrame(app, text="Info")
info_box.pack(anchor="n",fill="x", padx=10, pady=10)

label1 = ttk.Label(info_box, text="Quake 3 Folder Path:  ")
label1.pack(anchor="w", padx=10, pady=(10, 0))

label2 = ttk.Label(info_box, text="cpma Folder Path:  ")
label2.pack(anchor="w", padx=10, pady=(5, 5))

label3 = ttk.Label(info_box, text="autoexec Location:  ")
label3.pack(anchor="w", padx=10, pady=(10, 0))

label4 = ttk.Label(info_box, text="Generated gui.cfg Location:  ")
label4.pack(anchor="w", padx=10, pady=(5, 0))

select_q3_folder_button = ttk.Button(info_box, text='Select Quake III Arena Folder', command=select_folder_dialog)
select_q3_folder_button.pack(anchor="e", padx=10, pady=(5, 10))

# TABS
style = ttk.Style()
style.theme_use('clam')
style.configure('TNotebook.Tab', padding=[20, 2])
style.map('TCombobox', fieldbackground=[('readonly', 'white')], selectbackground=[('readonly', 'white'), ('!readonly', 'white')], selectforeground=[('readonly', 'black'), ('!readonly', 'black')])

tabControl = ttk.Notebook(app)
tabControl.pack(anchor="n",fill="both", expand=True, padx=10, pady=10)

#each frame holds that specific tab's widgets
tab1 = ttk.Frame(tabControl, padding=10)
tab2 = ttk.Frame(tabControl)
tab3 = ttk.Frame(tabControl)
tab4 = ttk.Frame(tabControl)
tab5 = ttk.Frame(tabControl)
tab6 = ttk.Frame(tabControl)
tab7 = ttk.Frame(tabControl)

tabControl.add(tab1, text ="Video")
tabControl.add(tab2, text ="Mouse")
tabControl.add(tab3, text ="Audio")
tabControl.add(tab4, text ="Hud")
tabControl.add(tab5, text ="Player")
tabControl.add(tab6, text ="Weapons")
tabControl.add(tab7, text ="Keybinds")

row_i = 0
for i in VIDEO_SETTINGS:
    ttk.Label(tab1, text=VIDEO_SETTINGS[i]["label"], font=('calibre',10, 'bold')).grid(row = 0+row_i, column = 0,  sticky='w', pady=(15,0), padx=(0,15))
    ttk.Label(tab1, text=VIDEO_SETTINGS[i]["description"], font=('calibre',10)).grid(row = 0+row_i, column = 1, sticky='w', pady=(15,0))

    if 'min' in VIDEO_SETTINGS[i]:
        ttk.Label(tab1, text=f"<{VIDEO_SETTINGS[i]['min']} to {VIDEO_SETTINGS[i]['max']}> (default: {VIDEO_SETTINGS[i].get('game_default','')})", font=('calibre',10, 'bold')).grid(row = 1+row_i, column=1, sticky='w')
    else:
        ttk.Label(tab1, text=f"(default: {VIDEO_SETTINGS[i]['game_default']})", font=('calibre',10, 'bold')).grid(row = 1+row_i, column=1, sticky='w')

    if VIDEO_SETTINGS[i]['type'] in ["float","int"] :
        ttk.Entry(tab1, width=8).grid(column = 0, row = 1+row_i, sticky='w')
    elif VIDEO_SETTINGS[i]['type'] == "bool" :
        ttk.Combobox(tab1, values=["", "0", "1"], state="readonly", width=6).grid(column = 0, row = 1+row_i, sticky='w')
    elif VIDEO_SETTINGS[i]['type'] == "discrete" :
        ttk.Combobox(tab1, values=["", "0", "1", "2"], state="readonly", width=6).grid(column = 0, row = 1+row_i, sticky='w')
    elif VIDEO_SETTINGS[i]['type'] == "string" :
        ttk.Label(tab1, text="STRING", font=('calibre',10, 'bold')).grid(column = 0, row = 1+row_i, sticky='w')
    else:
        pass
    row_i += 2

# SAVE BUTTON
save_config_button = ttk.Button(app, text='Save Config')
save_config_button.pack(anchor="se", padx=20, pady=(10,20))

# Make infinite loop for displaying app on the screen
app.mainloop()
