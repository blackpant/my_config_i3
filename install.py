#! /usr/bin/python






import os
import subprocess
import concurrent.futures as futures
# import threading
# import requests


# recup la variable HOME
user_home = os.getenv('HOME')

# verifie si les dossiers exits, si non les creer
os.makedirs(user_home + '/.vim_runtime', exist_ok=True)
os.makedirs(user_home + '/.vim_runtime/sources_non_forked', exist_ok=True)
os.makedirs(user_home + '/.vim_runtime/test', exist_ok=True)
os.makedirs(user_home + '/Images/Wallpapers', exist_ok=True)


def CheckFolder():
    if "HOME" in os.environ:
        userPath = os.getenv('HOME')
        subprocess.run(['cp', '-ur', '.config', userPath])
        subprocess.run(['cp', '-ur', '.task', userPath])
        subprocess.run(['cp', '-u', '.taskrc', userPath])
        subprocess.run(['cp', '-u', '.tmux.conf', userPath])
        subprocess.run(['cp', '-u', '.zshrc', userPath])
        subprocess.run(['cp', '-u', 'my_configs.vim',  userPath + '/.vim_runtime/'])
        subprocess.run(['cp', '-u', 'tmuxline', userPath])
        # subprocess.run(['mkdir', userPath + '/Images/Wallpapers'])
        subprocess.run(['cp', 'leopard2.jpg', userPath + '/Images/Wallpapers'])


def install_vim_ult():
    subprocess.run(['git', 'clone', '--depth=1', 'https://github.com/amix/vimrc.git', os.path.join(user_home, '.vim_runtime')])
    subprocess(['sh', os.path.join(user_home, '.vim_runtime') + '/install_awesome_vimrc.sh'])


# fonction pour installer les plugins supp pour vim
def install_git_plugin(url):
    subprocess.run(['git', 'clone', url])


CheckFolder()

# recup les liens plugin vim
with open('link', 'r') as f:
    url_list = ''.join(f.readlines()).splitlines()


# change de repertoire courant => vim_runtime/sources_non_forked
os.chdir(os.path.join(os.getenv('HOME'), '.vim_runtime', 'sources_non_forked'))
# dl les plugins vim de facon asynchrone
with futures.ThreadPoolExecutor(20) as executor:
    executor.map(install_git_plugin, url_list)


##################################################
# downloadThreads = []
# with open('link', 'r') as f:
#     for line in f:
#         # downloadThread = threading.Thread(target=install_git_plugin, args=[line])
#         # downloadThreads.append(downloadThread)
#         # downloadThread.start()


# for downloadThread in downloadThreads:
#     downloadThread.join()
##################################################

print('Done.')
