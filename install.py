#!/usr/bin/env python

import os
import subprocess
# import shutil as sht


def CheckFolder():
    if "HOME" in os.environ:
        userPath = os.getenv('HOME')
        # configPath = userPath + "/.config"

        subprocess.run(['cp', '-ur', '.config', userPath])
        subprocess.run(['cp', '-ur', '.task', userPath])
        subprocess.run(['cp', '-u', '.taskrc', userPath])
        subprocess.run(['cp', '-u', '.tmux.conf', userPath])
        subprocess.run(['cp', '-u', '.zshrc', userPath])
        subprocess.run(['cp', '-u', 'my_config.vim',  userPath + '/.vim_runtime/'])
        subprocess.run(['cp', '-u', 'tmuxline', userPath])
        subprocess.run(['mkdir', userPath + '/Images/Wallpapers'])
        subprocess.run(['cp', 'leopard2.jpg', userPath + '/Images/Wallpapers'])


CheckFolder()
