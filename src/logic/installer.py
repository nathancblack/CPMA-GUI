import os
import zipfile
import tempfile
import urllib.request
import shutil

def get_install_path():
    local_app_data = os.getenv('LOCALAPPDATA')
    if not local_app_data:
        local_app_data = os.path.expanduser("~\\AppData\\local")

    install_path = os.path.join(local_app_data, "CPMA_GUI")
    return install_path

def open_game_folder():
    # For open game folder button
    path = get_install_path()
    if os.path.exists(path):
        os.startfile(path)
    else:
        print("Folder does not exist yet.")

def install_assets():
    install_dir = get_install_path()
    download_url = f"https://github.com/nathancblack/CPMA-GUI/releases/latest/download/assets.zip"

    os.makedirs(install_dir, exist_ok=True)

    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".zip") as temp_file:
            temp_path = temp_file.name

            with urllib.request.urlopen(download_url) as response:
                shutil.copyfileobj(response, temp_file)

        with zipfile.ZipFile(temp_path, 'r') as zip_ref:
            zip_ref.extractall(install_dir)

    except Exception as e:
        print(f"Error installing assets: {e}")
        return False

    finally:
        if temp_path and os.path.exists(temp_path):
            os.remove(temp_path)
    return True
print(get_install_path())