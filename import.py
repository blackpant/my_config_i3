#!/usr/bin/python
import os
import subprocess
# import shutil


def updateFilesGit():
    if "HOME" in os.environ:
        userPath = os.getenv('HOME')

    subprocess.call(["cp", "-u", userPath + "/.zshrc", "."])
    # subprocess.call(["cp", "-u", userPath + "/.vimrc", "."])
    subprocess.call(["cp", "-u", userPath + "/.vim_runtime/my_configs.vim", "."])
    subprocess.call(["cp", "-u", userPath + "/.conkyrc", "."])
    subprocess.call(["cp", "-u", userPath + "/.Xdefaults", "."])
    subprocess.call(["cp", "-u", userPath + "/tmuxline", "."])
    subprocess.call(["cp", "-u", userPath + "/.xinitrc", "."])
    subprocess.call(["cp", "-u", userPath + "/.tmux.conf", "."])
    subprocess.call(["cp", "-u", userPath + "/.taskrc", "."])
    subprocess.call(["cp", "-uR", userPath + "/.task", "."])
    subprocess.call(["cp", "-u", userPath + "/.config/compton.conf","./.config"])
    subprocess.call(["cp", "-u", userPath + "/.config/i3-scrot.conf", "./.config"])
    subprocess.call(["cp", "-u", userPath + "/.config/i3-scrot.conf", "./.config"])
    subprocess.call(["cp", "-uR", userPath + "/.config/i3", "./.config"])
    subprocess.call(["cp", "-uR", userPath + "/.config/i3blocks", "./.config"])
    subprocess.call(["cp", "-uR", userPath + "/.config/terminator", "./.config"])
    subprocess.call(["cp", "-uR", userPath + "/.config/termite", "./.config"])
    subprocess.call(["cp", "-uR", userPath + "/.config/cava", "./.config"])
    subprocess.call(["cp", "-uR", userPath + "/.config/cmus", "./.config"])
    subprocess.call(["cp", "-uR", userPath + "/.config/htop", "./.config"])
    subprocess.call(["cp", "-uR", userPath + "/.config/polybar", "./.config"])
    subprocess.call(["cp", "-uR", userPath + "/.config/ranger", "./.config"])
    subprocess.call(["cp", "-uR", userPath + "/.config/rofi", "./.config"])
    subprocess.call(["cp", "-uR", userPath + "/.config/vlc", "./.config"])
    subprocess.call(["cp", "-uR", userPath + "/.config/tmux", "./.config"])
    subprocess.call(["cp", "-uR", userPath + "/.config/tmuxinator", "./.config"])
    subprocess.call(["cp", "-uR", userPath + "/.config/dunst", "./.config"])



def Main():
    try:
        updateFilesGit()
    except:
        print("Erreur Survenant")


Main()
