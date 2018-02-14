#!/usr/bin/env python

import os
import subprocess
import sys
import os.path as p
import glob

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


    print(userPath)
    userConfigFolder = os.listdir(configPath)
    print(userConfigFolder)
