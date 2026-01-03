# src/ui/dialogs.py
import tkinter as tk

def prompt_setup_choice(root, install_task):
    popup = tk.Toplevel(root)
    popup.title("First Time Setup")
    popup.geometry("350x150")
    popup.resizable(False, False)

    user_choice = tk.StringVar(value=None)

    def on_install():
        btn_frame.destroy()
        lbl.config(text="Installing assets...\nPlease wait, this may take a moment.")

        popup.update()

        success = install_task()

        if success:
            user_choice.set("install_success")
        else:
            user_choice.set("install_failed")

        popup.destroy()

    def on_locate():
        user_choice.set("locate")
        popup.destroy()

    lbl = tk.Label(popup, text="CPMA Assets not found.\nWhat would you like to do?", pady=10)
    lbl.pack()

    btn_frame = tk.Frame(popup)
    btn_frame.pack(pady=10)

    btn_install = tk.Button(btn_frame, text="Download & Install", width=15, command=on_install)
    btn_install.pack(side="left", padx=10)

    btn_locate = tk.Button(btn_frame, text="Locate Existing", width=15, command=on_locate)
    btn_locate.pack(side="left", padx=10)

    popup.transient(root)
    popup.grab_set()
    root.wait_window(popup)

    return user_choice.get()