#!/usr/bin/python
import termcolor as tm
# import subprocess
import pyperclip
import sys

# Variables
# Il ny en a pas mouahahahah
##################################################

if len(sys.argv) < 2:
    print(tm.colored("Entrez le texte a convertir".center(20, "="), 'blue'))
    text = input().encode('utf-8')
else:
    text = sys.argv[1].encode('utf-8')
# Convertion

convtext = text.hex()

print(tm.colored("text convertit:\t", 'green'), convtext)
# Resultat envoyer dans le clipboard !!
pyperclip.copy(convtext)
