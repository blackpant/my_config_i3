
import os
import subprocess
# import sys
# import os.path as p
# import glob

def updateFilesGit() :
    if "HOME" in os.environ:
        userPath = os.getenv('HOME')

    subprocess.call(["cp", userPath + "/.zshrc", userPath + "/Documents/my_config_i3"])
    subprocess.call(["cp", userPath + "/.vimrc", userPath + "/Documents/my_config_i3"])
    subprocess.call(["cp", userPath + "/.conkyrc", userPath + "/Documents/my_config_i3"])
    subprocess.call(["cp", userPath + "/.Xdefaults", userPath + "/Documents/my_config_i3"])
    subprocess.call(["cp", "-R", userPath + "/.config/i3", userPath + "/Documents/my_config_i3/.config"])
    subprocess.call(["cp", "-R", userPath + "/.config/terminator", userPath + "/Documents/my_config_i3/.config"])
    subprocess.call(["cp", userPath + "/.config/compton.conf", userPath + "/Documents/my_config_i3/.config"])
    subprocess.call(["cp", "-R", userPath + "/.config/cava", userPath + "/Documents/my_config_i3/.config"])
    subprocess.call(["cp", "-R", userPath + "/.config/cmus", userPath + "/Documents/my_config_i3/.config"])
    subprocess.call(["cp", "-R", userPath + "/.config/htop", userPath + "/Documents/my_config_i3/.config"])
    subprocess.call(["cp", "-R", userPath + "/.config/polybar", userPath + "/Documents/my_config_i3/.config"])
    subprocess.call(["cp", "-R", userPath + "/.config/ranger", userPath + "/Documents/my_config_i3/.config"])
    subprocess.call(["cp", "-R", userPath + "/.config/rofi", userPath + "/Documents/my_config_i3/.config"])
    subprocess.call(["cp", "-R", userPath + "/.config/vlc", userPath + "/Documents/my_config_i3/.config"])
    subprocess.call(["cp", userPath + "/.config/i3-scrot.conf", userPath + "/Documents/my_config_i3/.config"])

def Main():
    try:
        updateFilesGit()
    except:
        print("Erreur Survenant")

Main()
