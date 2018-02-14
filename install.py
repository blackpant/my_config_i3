#!/usr/bin/env python

import os
import subprocess
import sys
import os.path as p
import glob

def CheckFolder() :
    if "HOME" in os.environ:
        userPath = os.getenv('HOME')
        configPath = userPath + "/.config"

        if ".config" in os.listdir(userPath):
            folderConfFile = ["i3","rofi","compton"]
            for conf in folderConfFile:
                if conf in os.listdir(configPath):
                    print("OK")
                else:
                    print("Création du dossier %s",conf)
                    print("###################################################")
                    try:
                        subprocess.call(["mkdir", configPath + "/" + conf])
                    except subprocess.CalledProcessError as error:
                        print("Erreur : \r")
                        sys.exit(error.returncode)

        else :
            print("NO")


def CheckFolderBis():
    # change current directory
    # get environnement variable $HOME
    # copy .config from repositery to user home folder
    # install antigen + dependencies
    # copy .zshrc from repositery to $HOME
    # install vim ultimate config
    # copy from repositerie vim_runtime/source_non_forked/ to ~/.vim_runtine/
    pass

def Main():
    pass
