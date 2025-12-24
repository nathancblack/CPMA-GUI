import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from pathlib import Path

from src.logic.paths import PathManager
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

# VIDEO TAB
ttk.Label(tab1, text="r_gamma", font=('calibre',10, 'bold')).grid(column = 0, row = 0, sticky='w', padx=(0,40))
ttk.Label(tab1, text="Gamma correction factor", font=('calibre',10)).grid(column = 1, row = 0, sticky='w')
ttk.Entry(tab1, width=8).grid(column = 0, row = 1, sticky='w')
ttk.Label(tab1, text="<0.5 to 3.0> (default 1.2)", font=('calibre',10, 'bold')).grid(column = 1, row = 1, sticky='w')


ttk.Label(tab1, text="r_intensity", font=('calibre',10, 'bold')).grid(column = 0, row = 2, sticky='w', pady=(15, 0))
ttk.Label(tab1, text="Brightness of non-lightmap map textures", font=('calibre',10)).grid(column = 1, row = 2, sticky='w', pady=(15, 0))
ttk.Entry(tab1, width=8).grid(column = 0, row = 3, sticky='w')
ttk.Label(tab1, text="<1.0 to +inf> (default: 1)", font=('calibre',10, 'bold')).grid(column = 1, row = 3, sticky='w')


ttk.Label(tab1, text="r_greyscale", font=('calibre',10, 'bold')).grid(column = 0, row = 4, sticky='w', pady=(15, 0))
ttk.Label(tab1, text="How desaturated the final image looks", font=('calibre',10)).grid(column = 1, row = 4, sticky='w', pady=(15, 0))
ttk.Entry(tab1, width=8).grid(column = 0, row = 5, sticky='w')
ttk.Label(tab1, text="<0.0 to 1.0> (default: 0)", font=('calibre',10, 'bold')).grid(column = 1, row = 5, sticky='w')


ttk.Label(tab1, text="r_fullscreen", font=('calibre',10, 'bold')).grid(column = 0, row = 6, sticky='w', pady=(15, 0))
ttk.Label(tab1, text="Full-screen mode", font=('calibre',10)).grid(column = 1, row = 6, sticky='w', pady=(15, 0))
ttk.Combobox(tab1, values=["", "0", "1"], state="readonly", width=6).grid(column = 0, row = 7, sticky='w')
ttk.Label(tab1, text="<0:1> (default: 1)", font=('calibre',10, 'bold')).grid(column = 1, row = 7, sticky='w')


# SAVE BUTTON
save_config_button = ttk.Button(app, text='Save Config')
save_config_button.pack(anchor="se", padx=20, pady=(10,20))

# Make infinite loop for displaying app on the screen
app.mainloop()
