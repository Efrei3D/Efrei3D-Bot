import wget, os, zipfile, shutil, filecmp
from os import getcwd
from packaging import version
import subprocess


download_url = "https://github.com/Efrei3D/Efrei3D-Bot/archive/refs/heads/main.zip"


directory = getcwd()
download_folder = os.path.join(directory, 'TEMP')

if not os.path.exists(download_folder): os.mkdir(download_folder)

download_file = os.path.join(download_folder, 'temp_download.zip')

def download():
    if not os.path.exists(download_file):
        wget.download(download_url, download_file)

def check_version():
    versions = []
    with open(os.path.join(directory, "version"), "r") as f: cr_version = f.read()
    versions.append(cr_version)
    # try:
    with zipfile.ZipFile(download_file) as archive:
        with archive.open("Efrei3D-Bot-main/version", 'r') as f: zip_version = f.read().decode()
        # zip_version.strip('\n')
        versions.append(zip_version)
    return versions


def unzip():
    if os.path.exists(download_file):
        archive = zipfile.ZipFile(download_file)
        for file in archive.namelist():
            if file.startswith('Efrei3D-Bot-main/'):
                archive.extract(file, download_folder)   


def wipe():
    active_listdir = os.listdir(directory)
    active_listdir.remove("update.sh")
    active_listdir.remove("update_restart.sh")
    active_listdir.remove("restart.sh")
    active_listdir.remove("updater.py")
    active_listdir.remove("TEMP")
    active_listdir.remove("version")
    active_listdir.remove("api_secrets.json")
    for element in active_listdir:
        target = os.path.join(directory, element)
        try:
            os.remove(target)
        except Exception as e:
            shutil.rmtree(target)

def move():
    active_listdir_move = os.listdir(os.path.join(download_folder, 'Efrei3D-Bot-main'))
    for element in active_listdir_move:
        original = os.path.join(os.path.join(download_folder, 'Efrei3D-Bot-main'), element)
        target = os.path.join(directory, element)
        try:
            shutil.move(original, target)
        except Exception as e:
            print(e)

    try:
        os.remove(download_folder)
    except Exception as e:
        shutil.rmtree(download_folder)

def restart():
    # os.execl(f"{os.path.join(directory, 'update_restart.sh')}", ' ')
    # os.execl("update_restart.sh","")
    subprocess.run(f"{os.path.join(directory, 'update_restart.sh')}", shell=True)
    quit()


if __name__=="__main__":
    download()
    versions = check_version()
    if version.parse(versions[0]) > version.parse(versions[1]) or version.parse(versions[0]) == version.parse(versions[1]):
        print("No update needed")
        try:
            os.remove(download_file)
        except Exception as e:
            shutil.rmtree(download_file)
        try:
            os.remove(download_folder)
        except Exception as e:
            shutil.rmtree(download_folder)
    else:
        print("Update needed")
        unzip()
        wipe()
        move()
        print("Update done")
    restart()