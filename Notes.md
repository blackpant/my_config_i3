---
author: Ianis HAMMAM
title: Notes
...

# fichier de config 
- ~/.vim_runtime/my_config.vim
- .vimrc
- .vim_runtime/sources_non_forked/
- dossier .config
    + compton.conf
    + i3-scrop.conf
    + i3/
    + terminator/
    + cava/
    + cmus/
    + htop/
    + polybar/
    + ranger/
    + rofi/
    + vlc/
    + nvim/
    + tmux/
    
- dossier conky !!
- fichier .conkyrc
- fichier .Xdefault
- dossier ~/Images/Wallpapers
- fichier ~/.zshrc
- fichier `~/.ssh/config`  
- `~/.tmux.conf`
- `~/tmuxline`


- install rofi
- install python-pip
- yaourt -Syua
- yaourt -Sy antigen-git
- ajout de quelque ligne dans .zshrc pour utiliser oh-my-zsh et pour choisir bundle et theme
- source /usr/share/zsh/share/antigen.zsh
- antigen use oh-my-zsh
- antigen bundle git
- antigen bundle pip
- antigen theme agnoster
- antigen apply
- installation de i3-gaps
```sh
yaourt -Sy i3
git clone https://github.com/blackpant/my_config_i3
cd my_config_i3
cd i3
cp config ~/.config/i3/
cp i3status.conf ~/.config/i3/
```

- ajout de gaps global
```
set gaps
gaps inner 15
gaps outer 1
```

- ajout de l'option "smart_gaps"
`smart_gaps on`

- installation de feh
`yaourt -Sy feh`

- creation du dossier ~/Images/Wallpapers/
`mkdir ~/Images/Wallpapers/`

- pour changement automatique du wallpaper avec l'image ninja.jpg dans `~/Images/Wallpapers/`

- Dans .zshrc
    + Ajout de plusieurs alias 
    + A voir pour d'autre


- Set alias
```sh
alias ls='ls --color=auto '
alias la='ls -a --color=auto'
alias ll='ls -l --color=auto'
alias cls='clear'
```

- installation de polybar
```sh
$ install -Dm644 /usr/share/doc/polybar/config \$HOME/.config/polybar/config
$ polybar example
```

- Launching polybar routine

[Lien](https://github.com/jaagr/polybar/wiki)
- add line to always launch the script in config of i3 like :
```sh
exec_always --no-startup-id $HOME/.config/polybar/launch.sh
```

- **Wallpapers**
```
blackpant@anarchy  ~/Images/Wallpapers  cp * ~/Images/Wallpapers   (02-12 15:59) 
```

- installation de librairies python pour le bon fonctionnement de py3status
```sh
yaourt -S python-pip
sudo pip install py3status
sudo pip install pytz
sudo pip install tzlocal
```

- vim config

```sh
git clone --depth=1 https://github.com/amix/vimrc.git ~/.vim_runtime
sh ~/.vim_runtime/install_awesome_vimrc.sh
yaourt -S neovim
```

copy de mon dossier source_non_fork dans celui courant `~/.vim_runtime/sources_non_forked/`

> dans sources_non_forked 
> mkdir archives
> mv youcompleteme archives/  


> INSTALLATION DE YOUCOMPLETEME VIA LE GIT ET COMPILATION POUR TOUS OU CERTAIN LANGAGES  


> vraiment se pencher sur neovim !!! ou pas -_- !!  
>



- installation de dmenu si pas installé
```sh
yaourt -S dmenu
```

- ROFI install

```sh
install de compton
yaourt -S compton
```

- déplacer le compton.conf dans $HOME/.config/


- installation de flake pour que l'installation de youcompleteme fonctionne bien
```
sudo pip install flake8
```

- bon alors j'ai binder $mod+d sur un mode
    + si touche d => lance dmenu
    + si touche r => lance le mode Rofi
    + si touche r => lance rofi -show run
    + si touche w => lance rofi -show window
    + si touche s => lance rofi -show ssh


- run rofi-theme-selector  
    pour previsualiser les themes de disponible


- installation de roficlip clipboard manager rofi  
pour afficer dans rofi l'historique du presspapier/ clipboard

```sh
yaourt -S roficlip
# Modification du lancement de urxvt
# maintenant à chaque chargemnt de i3 lancement de urxvtd - daemon server de urxvt
$mod+Return exec urxvtc => ouvre des terminaux lié au daemon => plus rapide prends moins de memoire apparemment
```

# Plein de choses !!

---------
mise a jours du git   
suppression de dossier de config inutile  
ajout du dossier de config rofi pour avoir deux themes differents les deux sont pas mal.  
roficlip peut marcher dans un terminal directement.  
ou dans rofi en faisant => rofi -show run => tapez roficlip => entrer pour le lancer.  

---------


- installation de docker :  
```sh
yaourt -S docker
```


- installation client ssh.  
> openssh installé !
>

- installation clé privé + clé public !!
    + converti clé privé avec putty vers clé openssh
    + ajout de la clé dans le répertoire ~/.ssh/
    + rename de la clé en ...

- installation de polybar + config
    > config d'exemple de polybar pas vraiment de modification et d'utilisation pour l'instant.

- installation de slim
```sh
yaourt -S slim
# installation de vulscan + nmap !!!
yaourt -a vulscan
```
  
> est-ce que ca sert !!! aucune idée xD


- installation de cmus (console music player) +  cava (console light visualizer) :  
```sh
# installation de cmus
yaourt -S cmus

# installation de cava !!
yaourt -S cava
```

- installation de i3lock 
- installation de i3lock-fancy
> Juste i3lock-fancy suffit je crois !!

- Changement de keybinding 
    + ajout d'un mode terminal
pour ensuite choisir le terminal à lancer
urxvtc ou terminator ou peut etre guake


- Ajout du workspace "Music" => $tag7 => "Alt+è" pour y accèder


- Update config i3
> lancement de cmus directement dans le workspace "Music" soit Alt+7
> fait avec for_window
> partie "for_window config" du fichier i3 config

-----
> ajout dans le mode "focused"
> d'une touche pour focus "CMUS"
> en mode "Focused" 
> => touche "m" => focus sur cmus

-----

- ajout d'un for_window pour Htop ? ou un autre system de monitoring !!
- Htop est déplacé automatiquement dans le workspace 6

installation de deepin !!
Avoir ?? pour l'instant ne ma pas l'air tres personnalisable !!
- Htop et mieux je trouve.
    > Donc désinstallation de deepin
    >

- installation et test de termite terminal ?  

- installation et test de escrotum => screenshot tool 
possibilité de mettre le screenshot pris dans le pressepapier
la selection de fenetre pour un screenshot focus se fait via la souris !!
> Du coup désinstallation de escrotum !!

- installation et configuration de scrot + i3-scrot + ajout d'un mode screenshot avec keybinding + ajout dans la barre i3status d'un icone screen avec click event( voir dans la config de `i3status.conf`.  
Avec scrot cest bon
Lexemple ci-dessous fait un screenshot
i3-scrot => script scrot i3


- installation de xclip => Command line interface to the X11 clipboard

> *combinaison xclip + scrot => pas besoin de escrotum tant mieux*
>  
> screenshot de la fenetre courante vers le pressepapier ensuite

```sh
scrot -u -e 'xclip $f -selection clipboard -t image/png'
```

va dans le dossier `$Home/Images/` prend un screenshot qui s'enregistre à cette location et mets l'image dans le clipboard
```sh
cd ~/Images/ && scrot -u -e 'xclip $f -selection clipboard -t image/png'
```
***!!ne fonctionne pas ^^***


- Update du fichier de config i3
    + Regroupement des configs
    + Ajout du lancement de cava lors du lancement de cmus
    + Floating enable pour cmus et cava
    + Definir la taille et l'emplacement ?!
    + Ajout d'un mode "Power" => comme ca augmentation des keybindings dispo en en libérant un.


- installation de nitrogen pour les fonds d'ecran !!
> il y a deja feh mais cest un en plus léger aussi.
> feh est tres bien laisser Nitrogen de coté !!!

- regarde les differntes possibilités avec rofi , plugins et tout
rofi-top-git

- réarrangement du script d'import de fichier de configuration `import.py`

- modification du dossier par defaut ou sont enregistrés les screenshots => `~/.config/i3-scrot.conf` , dossier par default `~/Images/Screen/`

- move a floating window to the top right corner
```
move absolute position 0 0
```


- script python `my_config_i3`  
> si je change de definition d'écran, ne s'adapte pas automatique
> xrandr -q => recupere la configuration actuelle de l'ecran

```
for_window [title="cmus*" class="Terminator"] move container to workspace $tag7, floating enable, move absolute position 0 0, resize set 800 900
```
- *script ?! variable dans i3 ??!*

- Dans le fichier pour importer mes fichiers de configs `import.py` dans mon git faire un :  
```sh
cp -u [liste des fichiers] -t [dossier de destination]
```

- installation de cheat / python-cheat
    + configurer et mettre dotfile in the git
    + Utilité ?!

- installation de plugin vim
    + open-browser
    + previm

- mapping vim pour plugin vim open-browser.vim:  
```vim
let g:netrw_nogx = 1 " disable netrw's gx mapping
nmap gx <Plug>(openbrowser-smart-search)
vmap gx <Plug>(openbrowser-smart-search)
```


**CHANGEMENT DE GESTIONNAIRE DE CONNEXION**
- modifier le fichier utilisateur .xinitrc avec la ligne suivante :  
```sh
exec $1
```

- modifier le fichier /etc/slim.conf :  
```sh
```

- disable lightdm ou le précédent gestionnaire de connexion :  
```sh
systemctl disable lightdm.service
```

- enable slim :  
```sh
systemctl enable slim.service
```

- changement de clipboard display dans rofi. "greenclip"
    + ajout du lancement du daemon greenclip dans le fichier de config de i3
    + modification du fichier de config de rofi dans $HOME/.config/rofi/
    + roficlip est toujours la et utilisable mais je n'arrive pas a la lancer directement comme mode de rofi.
    + [link du github](https://github.com/erebe/greenclip)


- ajout et modification du fichier de configuration config de ssh.  
    + ajout des hosts  
    + bien comprendre le `~/.ssh/config`  

- a voir pour screenshot dans rofi
    + [link github](https://github.com/carnager/teiler)

- ajout d'un indicateur du nombre de fenetre dans le scratch i3, dans la barre i3status
    + a faire avec py3status
    + scratchpad_counter

- modification dans config i3status.conf:  
    + ajout de `screenshot` module
        * screenshot_command = scrot or i3-scrot
        * save_path = ~/Images/Screen/
        * push = False
    + Ajout de `keyboard_locks` module  
        * ...  



- enable ntop  
```sh
sudo systemctl enable ntop.service
```

- start ntop  
```sh
sudo systemctl start ntop.service
```

- lancement de ntop
```sh
sudo ntop
```

le premier lancement demandera un nouveau mot de passe root.  

- y accéder via cette URL:  

```
http://127.0.0.1:3000
```

- ajout de plugin zsh simple mais puissant ?!!
    + ssh-connect
    + solarized-man !!Nop
    + pretty-time-zsh !!
    + zsh-completion-generator
    + simple-agnoster theme à voir !!Nop
    + sysadmin-util !! Nop
    + plugin tmux si tmux installé !! Oui ?!
    + zsh-pandoc-completion !! Nop

- installer tmux + keybinding vim !!
    + [tuto](https://blog.bugsnag.com/tmux-and-vim/)

- installation de tmux :
```zsh
yaourt -a tmux
```

- installation de fzf :

    ```zsh
    yaourt -S fzf
    ```

- fichier de config tmux :
```
```

- installation de pylint :
```zsh
yaourt -S pylint
```

- rofi + tmux ?
- changer zsh mode emacs pour les keybinding

- redemarrer le serveur tmux pour bien prendre en compte le fichier de config.
- pour l'instant le ficheir de configuration tmux est ~/.tmux.conf
- installation du plugin vim `vim-tmux-navigator`
- ajout dans `~/.vim_runtime/my_config.vim` :  

    ```vim
    " vv to generate new vertical split
    nnoremap <silent> vv <C-w>v
    ```
    > A enlever, surcharge Leader+vv, qui fait la meme chose.
    > ou attendre un peut pour voir celle que j'utilise le plus.


- suppresstion de `~/.vim_runtime/source_non_forked.save`.  
-

- installation du plugin vim `vimux`
    pour envoyer des commandes à tmux.

- tagbar plugin pour vim!!
-

- ajout des lignes suivantes pour le binding vim du plugin vimux:
```vim
" Prompt for a command to run
map <Leader>vp :VimuxPromptCommand<CR>
```

```vim
" Close vimux runner
map <Leader>vc :VimuxCloseRunner<CR>
```

- ajout de quelques ligne dans mon fichier de configuration `vim`. Pour principalement rester en solarized et que ce soit bien affiché dans n'importe quel terminal.
- config vim : bien configurer le copier/coller dans vim !!
- ajout d'une status line dans tmux utilisant celle de vim : [Lien](https://github.com/edkolev/tmuxline.vim)
    + modification du fichier de configuration ~/.tmux.conf
    + Ajout du plugin tmuxline.vim
    + Helptags pour tout prendre en compte.

- `bindkey` pour voir tous les keybindings de zsh.
- suppression des profils inutile dans la config de terminator
- ajout de quelque ligne pour faciliter la creation de 'pane' dans tmux.
-

- installation de the_silver_search
```sh
yaourt -S the_silver_search
```

- ajout du plugin `tmux` + `wd` dans le fichier de config `.zshrc`.
> `tmux` ajoute des alias à zsh, et avec la ligne ci-dessous d'ajouter démarre tmux lorsqu'une session zsh est démarré.
> `wd` [Lien](https://github.com/robbyrussel/oh-my-zsh/wiki/Plugins#tmux)


- darkstat

# Exuberant ctag !!

## Universal-ctags

Installation de universal-ctags:  
```sh
yaourt -a universal-ctags
```

Installation du plugin `Tagbar` dans vim:  
```sh
cd ~/.vim_runtime/sources_non_forked/
git clone https://github.com/...
```

Installation du plugin `easytag` dans vim:  
```sh
cd ~/.vim_runtime/sources_non_forked/
git clone https://github.com/xolox/vim-easytags
```

Installer `ctags` + désinstaller `universal-ctags`:  
```sh
yaourt -S ctags
```
> universale-ctags sera en conflit avec `ctags` et sera donc désinstallé.

Donc garder:  
- ctags
- tagbar
- easytags
-

Ensuite ajouter des keybinding pour:  
- appeler TagbarToggle
- 

Modif de ~/.vim_runtime/my_config.vim :  
- `g:easytags_dynamic_files` like:  
> :set tags=./tags;
> :let g:easytags_dynamic_files = 1


