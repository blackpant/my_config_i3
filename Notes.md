```
                   -`                    aurera@Lenovo-sans-touches
                  .o+`                   --------------------------
                 `ooo/                   OS: Arch Linux x86_64
                `+oooo:                  Host: 20378 Lenovo Y50-70
               `+oooooo:                 Kernel: 4.15.8-1-ARCH
               -+oooooo+:                Uptime: 4 hours, 25 mins
             `/:-:++oooo+:               Packages: 845
            `/++++/+++++++:              Shell: zsh 5.4.2
           `/++++++++++++++:             Resolution: 1920x1080
          `/+++ooooooooooooo/`           WM: i3
         ./ooosssso++osssssso+`          Theme: Arc-Darker [GTK2/3]
        .oossssso-````/ossssss+`         Icons: Arc [GTK2/3]
       -osssssso.      :ssssssso.        CPU: Intel i7-4720HQ (8) @ 3.600GHz
      :osssssss/        osssso+++.       GPU: NVIDIA GeForce GTX 960M
     /ossssssss/        +ssssooo/-       GPU: Intel Integrated Graphics
   `/ossssso+/:-        -:/+osssso+-     Memory: 2314MiB / 7896MiB
  `+sso+:-`                 `.-/+oso:
 `++:.                           `-/+/
 .`                                 `/

```

# Applications principales
* Web browser           : Firefox
* File Manager          : Thunar + Ranger
* Desktop background    : Feh + Nitrogen
* Text and Code Editor  : Vim + Spacemacs
* Music Player          : Cmus + Spotify + ncmpcpp + mpd
* Launcher              : Rofi
* Email Client          : Thunderbird
* Bureautique           : LibreOffice
* Réseaux               :
    - Wireshark
    - Tshark
    - Ntop
    - Scapy
* Session Manager       : Slim
* Screen Recorder       : Byzanz
* Clipboard manager     : Xclip
* Bar de status         : I3blocks
* Windows manager       : I3-gaps
* Terminal              : Termite, Terminator, URxvt
* Notifications         : Dunst
* Process Monitoring    : Htop


# Fichier de config
- ~/.vim_runtime/my_config.vim
- .vimrc
- .vim_runtime/sources_non_forked/
- dossier .config
    + compton.conf  - ok
    + i3_scrop.conf - ok
    + i3/           - ok
    + terminator/   - ok
    + cava/         - ok
    + cmus/         - ok
    + htop/         - ok
    + polybar/      - ok
    + ranger/       - ok
    + rofi/         - ok
    + vlc/          - ok
    + nvim/
    + tmux/
- dossier conky !!
- fichier .conkyrc
- fichier .Xdefault
- dossier ~/Images/Wallpapers
- fichier ~/.zshrc
- fichier `~/.ssh/config`
- fichier `~/.tmux.conf`
- fichier `~/tmuxline`
- fichier `.task/`
- fichier `.taskrc`
- fichier `.xinitrc`
- rofi
- python-pip
- antigen
- i3-gaps
- ajout de gaps global
```
  set gaps
  gaps inner 15
  gaps outer 1
```
- ajout de l'option "smart_gaps":  `smart_gaps on`
- installation de feh: `yaourt -Sy feh`
- creation du dossier ~/Images/Wallpapers/
> `mkdir ~/Images/Wallpapers/`

- pour changement automatique du wallpaper avec l'image ninja.jpg dans `~/Images/Wallpapers/`
- Dans .zshrc
    + Ajout de plusieurs alias
    + A voir pour d'autre
- Set alias
```sh
  alias ls  = 'ls --color    = auto '
  alias la  = 'ls -a --color = auto'
  alias ll  = 'ls -l --color = auto'
  alias cls = 'clear'
```

- installation de polybar
```sh
  install -Dm644 /usr/share/doc/polybar/config \$HOME/.config/polybar/config
  polybar example
```

- Launching polybar routine
  + [Lien](https://github.com/jaagr/polybar/wiki)
- add line to always launch the script in config of i3 like :
```sh
  exec_always --no-startup-id $HOME/.config/polybar/launch.sh
```

- installation de librairies python pour le bon fonctionnement de py3status
```sh
  yaourt -S python-pip
  sudo pip install py3status
  sudo pip install pytz
  sudo pip install tzlocal
```

- installation de dmenu si pas installé
```sh
  yaourt -S dmenu
```

- ROFI **install**
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
  > Modification du lancement de urxvt
  > maintenant à chaque chargemnt de i3 lancement de urxvtd - daemon server de urxvt
  $mod+Return exec urxvtc => ouvre des terminaux lié au daemon => plus rapide prends moins de memoire apparemment
```


# Plein de choses !!

> mise a jours du git
> suppression de dossier de config inutile
> ajout du dossier de config rofi pour avoir deux themes differents les deux sont pas mal.
> roficlip peut marcher dans un terminal directement.
> ou dans rofi en faisant => rofi -show run => tapez roficlip => entrer pour le lancer.
- installation de docker :
```sh
yaourt -S docker
```

- installation client ssh.
> openssh installé !

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

- `bindkey` pour voir tous les keybindings de zsh.
- suppression des profils inutile dans la config de terminator
- ajout de quelque ligne pour faciliter la creation de 'pane' dans tmux.

- installation de the_silver_search
```sh
yaourt -S the_silver_search
```

- ajout du plugin `tmux` + `wd` dans le fichier de config `.zshrc`.
> `tmux` ajoute des alias à zsh, et avec la ligne ci-dessous d'ajouter démarre tmux lorsqu'une session zsh est démarré.
> `wd` [Lien](https://github.com/robbyrussel/oh-my-zsh/wiki/Plugins#tmux)


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

Ensuite ajouter des keybinding pour:
- appeler TagbarToggle

Modif de ~/.vim_runtime/my_config.vim :
- `g:easytags_dynamic_files` like:
> :set tags=./tags;
> :let g:easytags_dynamic_files = 1


# TaskWarrior

Installation :
```sh
sudo pacman -S task
```

Ajout du plugin `taskwarrior` dans la config `.zshrc`.

Installation de task-dashboard.
Installation de tasksh.
Inthe.am : site taskwarrior server.
Ajout de ligne dans `.taskrc`.
```conf
    # Files
    data.location=~/.task
    
    # Color theme (uncomment one to use)
    #include /usr/share/doc/task/rc/light-16.theme
    #include /usr/share/doc/task/rc/light-256.theme
    #include /usr/share/doc/task/rc/dark-16.theme
    #include /usr/share/doc/task/rc/dark-256.theme
    #include /usr/share/doc/task/rc/dark-red-256.theme
    #include /usr/share/doc/task/rc/dark-green-256.theme
    #include /usr/share/doc/task/rc/dark-blue-256.theme
    #include /usr/share/doc/task/rc/dark-violets-256.theme
    #include /usr/share/doc/task/rc/dark-yellow-green.theme
    #include /usr/share/doc/task/rc/dark-gray-256.theme
    #include /usr/share/doc/task/rc/dark-gray-blue-256.theme
    include /usr/share/doc/task/rc/solarized-dark-256.theme
    #include /usr/share/doc/task/rc/solarized-light-256.theme
    #include /usr/share/doc/task/rc/no-color.theme
    
    taskd.certificate=~/.task/intheam_config/private.certificate.pem
    taskd.key=~/.task/intheam_config/private.key.pem
    taskd.ca=~/.task/intheam_config/ca.cert.pem
    taskd.server=taskwarrior.inthe.am:53589
    taskd.credentials=inthe_am/ianishammam/832e2186-f4ce-463d-9aa0-b5e610239087
    taskd.trust=ignore hostname
```

- Modification du contenu du dossier `~/.task/`.
```
    .task
    ├── backlog.data
    ├── completed.data
    ├── dashboard.json
    ├── hooks
    │   └── on-exit_dashboard -> /home/blackpant/Documents/task-dashboard/task-dashboard
    ├── intheam_config
    │   ├── ca.cert.pem
    │   ├── private.certificate.pem
    │   └── private.key.pem
    ├── pending.data
    ├── undo.data
    └── .vim_tw.history
```


## Best Practices

[Lien](https://taskwarrior.org/docs/best-practices.html)


# Vim

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
>
> INSTALLATION DE YOUCOMPLETEME VIA LE GIT ET COMPILATION POUR TOUS OU CERTAIN LANGAGES
>
> vraiment se pencher sur neovim !!! ou pas -_- !!

- installation du plugin vim `vim-tmux-navigator`
- ajout dans `~/.vim_runtime/my_config.vim` :

```vim
    " vv to generate new vertical split
    nnoremap <silent> vv <C-w>v
```
    > A enlever, surcharge Leader+vv, qui fait la meme chose.
    > ou attendre un peut pour voir celle que j'utilise le plus.

- suppresstion de `~/.vim_runtime/source_non_forked.save`.
- installation du plugin vim `vimux` pour envoyer des commandes à tmux.
- tagbar plugin pour vim!!
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
- installation de plugin vim
    + open-browser
    + previm
- mapping vim pour plugin vim open-browser.vim:
```vim
    let g:netrw_nogx = 1 " disable netrw's gx mapping
    nmap gx <Plug>(openbrowser-smart-search)
    vmap gx <Plug>(openbrowser-smart-search)
```

- Installation du plugin `fzf.vim`
    > super de la mort qui tue
    > `:Maps` très utile liste tous mes binds
    > [FZF VIM](https://github.com/junegunn/fzf.vim)
    > `vim $(fzf --height 40%)` ou `vim $(fzf)`

- Lire et se familiariser avec les differentes facon de copier/coller
    + [Vim Wiki Copy Cut Paste](http://vim.wikia.com/wiki/Copy,_cut_and_paste)
    + [Vim Wiki System Clipboard](http://vim.wikia.com/wiki/Accessing_the_system_clipboard)
- Documentation pour modifier `lightline.vim`, statusline de vim:
- Changement de la combinaison pour sortir du `mode insertion` dans le fichier de coonfiguration `my_config.vim`:
```vim
    :inoremap kj <Esc>
```

- Modification de mon fichier de config vim `.vimrc` pour modifier légèrement l'apparence de la `statusline` de vim.
- nouveau theme d'installer pour vim, airline, et lightline : **`tender.vim`**
```vim
    let g:lightline = {
        \ 'colorscheme': 'tender',
        \ 'separator': {'left':'', 'right': ''},
        \ 'subseparator': {'left':'', 'right': ''},
        \ }
```


## Profiler vim plugins

```sh
    ====================================
    Top 10 plugins slowing vim's startup
    ====================================
    1        32.962   vim-virtualenv
    2        19.958   vim-easytags
    3        15.199   nerdtree
    4         7.161   syntastic
    5         5.085   vim-colors-solarized
    6         4.114   vim-fugitive
    7         1.965   tabular
    8         1.889   tagbar
    9         1.687   vim-gitgutter
    10        1.506   YouCompleteMe
    ====================================
```

## VIM client-server
```vim
    vim --servername FOO
```

```vim
    vim --servername foo --remote-silent bar.hs


    +-----------------------+
    |           |~$         |
    |           |           |
    |           |-----------+
    |    Vim    |~$         |
    |   Server  |           |
    |           |-----------+
    |           |~$         |
    |           |           |
    +-----------------------+
```
- Ajout d'un alias pour `vim --servername` ?!.
- Lancement de gvim dans le fichier i3 config comme `gvim --servername NAME_SERVEUR` ?!
- `vim --servername FOO --remote-silent $(fzf)` :lance fuzzyf(fzf) et ouvre le fichier trouvé dans le serveur vim FOO.
- ou `vim --servername boring --remote-tab-silent $(fzf)` : lance fzf et ouvre le fichier choisi après la recherche fzf dans un nouvel onglet vim dans le serveur vim BORING.


# Tmux

Fichier de config de tmux `.tmux.conf`:
```conf
    # tmuxline
    if-shell "test -f ~/tmuxline" "source ~/tmuxline"
    
    is_vim="ps -o state= -o comm= -t '#{pane_tty}' | grep -iqE '^[^TXZ ]+ +(\\S+\\/)?g?(view|n?vim?x?)(diff)?$'"
    
    bind-key -n C-h if-shell "$is_vim" "send-keys C-h"  "select-pane -L"
    bind-key -n C-j if-shell "$is_vim" "send-keys C-j"  "select-pane -D"
    bind-key -n C-k if-shell "$is_vim" "send-keys C-k"  "select-pane -U"
    bind-key -n C-l if-shell "$is_vim" "send-keys C-l"  "select-pane -R"
    bind-key -n C-\ if-shell "$is_vim" "send-keys C-\\" "select-pane -l"
    
    # binding vertical split
    bind | split-window -h -c "#{pane_current_path}"
    bind - split-window -v -c "#{pane_current_path}"
    
    # copy from tmux to sytem clipboard
    bind -T copy-mode-vi y send-keys -X copy-pipe-and-cancel 'xclip -in -selection clipboard'
```
- Ajout du mode mouse, pour pouvoir scroller dans l'historique du terminal. De base l'option mouse est sur off.
- Ajout de la possibilité de resize les panes avec la souris.


## Tmuxinator
[Lien explication tmuxinator](https://collectiveidea.com/blog/archives/2017/03/27/using-tmuxinator-to-automate-your-environment)
[Lien explication tmuxinator un peu plus détaillé](https://fabianfranke.de/2013/11/19/use-tmuxinator-to-recreate-tmux-panes-and-windows/)
> Ne pas ajouter les options `set -g base-index 1` et `set -g pane-base-index 1`. Sinon task-dashboard ne fonctionne plus apparemment!!.


# ZSH

- Configuration de `zsh` avec `antigen`.
- liste de bundles/plugins:
```zsh
    ### Source plugins
    ##################
    source /usr/share/zsh/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
    source /usr/share/zsh/share/antigen.zsh
    
    # load the oh-my-zsh library
    antigen use oh-my-zsh
    
    # Bundles from the default repo oh-my-zsh repo
    #
    antigen bundle git
    antigen bundle pip
    antigen bundle colored-man-pages
    antigen bundle colorize
    antigen bundle vim-plugin
    antigen bundle vi-mode
    # antigen bundle zsh-vimto
    # antigen bundle hacker-quotes
    antigen bundle tmux
    antigen bundle wd
    antigen bundle taskwarrior
    # antigen bundle docker
    
    # Use theme agnoster from oh-my-zsh
    antigen theme robbyrussell
    # antigen theme avit
    # antigen theme agnoster
    
    # Apply the settings and it's done
    antigen apply
```
- `vi-mode` keybindings :
[git lien](https://github.com/robbyrussell/oh-my-zsh/tree/master/plugins/vi-mode)


# Tree command

Installation :
```sh
    yaourt -S tree
```

Utilisation :
```sh
    cd ~/Documents
    tree -d MarkdownProj/
```

```
        ➜  Documents tree -d MarkdownProj
        MarkdownProj
    ├── pandoc-bootstrap-template
    ├── pandoc-latex-template
    │   └── examples
    │       ├── basic-example
    │       ├── book
    │       ├── custom-titlepage
    │       ├── default-titlepage
    │       ├── german
    │       ├── green-titlepage
    │       ├── images-and-tables
    │       ├── japanese
    │       ├── listings
    │       └── without-listings
    └── screen
```

# Tips

tree like command with installing any additionnal packages:
```sh
    ls -R | grep ":$" | sed -e 's/:$//' -e 's/[^-][^\/]*\//--/g' -e 's/^/   /' -e 's/-/|/'
```

# i3

Installation:  
```sh
    yaourt -Sy i3
    git clone https://github.com/blackpant/my_config_i3
    cd my_config_i3
    cd i3
    cp config ~/.config/i3/
    cp i3status.conf ~/.config/i3/
```


# Developpement

pip install virtualenv
pip install virtualenvwrapper
ligne dans `.zshrc` :
```sh
    export WORKON_HOME=$HOME/Documents/.virtualenvs
    export PROJECT_HOME=$HOME/Documents/Devel
    export VIRTUALENVWRAPPER_SCRIPT=/usr/bin/virtualenvwrapper.sh
    source /usr/bin/virtualenvwrapper_lazy.sh
```


## Dossier de developpemnt qui contiendra tous les projets virtualenv

`mkdir ~/Documents/Devel/`  

## Sauvegarde des libraries python avec pip freeze

- sauvegarde librairies :  
```sh
    pip freeze > requirements.txt
```

- reinstallation des librairies sur un autre systeme :
```sh
    pip install -r requirements.txt
```


# Link
[TaskWarrior Command Reference](https://wiki.archlinux.org/index.php/Apache_HTTP_Server#Installation)


# Cheat sheet
[Site pour créer des fiches de rappels](https://www.cheatography.com/create/)
```py
subprocess.run(['vlc', '--play-and-exit', '/home/blackpant/Musique/ringtones/Slap-SoundMaster13-49669815.wav'])
```
[Lien python à lire](https://null-byte.wonderhowto.com/how-to/hack-like-pro-python-scripting-for-aspiring-hacker-part-1-0159118/)
[Languages for Hackers](https://www.tech2hack.com/programming-languages-hackers/)


# IDEAS Python Script

- script d'envoie d'une documentation (docx + html ou l'un ou l'autre) à une liste de mail ou à mail en particulier !! A voir !
- [mini exercices pour pratique python](https://projecteuler.net/archives)
- installation de dunst: pour desktop notification
- utilise `notify-send`.
- configuration de l'appararence des notification de dunst.
- suppression de i3lock-fancy
- suppression de i3lock
- installation de i3lock-color(git)
- installation de i3lock-next(git)
- changement de l'apparence de rofi.

changement de la configuration de `compton`:
lancement avec 
```
   exec --no-startup-id compton -fb --config ~/.config/compton.conf -i 0.8 --inactive-opacity-override --inactive-dim 0.1 -G --sw-opti
```

A ajuster quand meme.
` compton -fb --config /home/blackpant/.config/compton.conf -i 0.8 --inactive-opacity-override --inactive-dim 0.1 -G --sw-opti`

Installation de Termite
yaourt -S termite

Installation colorscheme solarized pour termite
[colors solarized termite](https://github.com/alpha-omega/termite-colors-solarized)

Changement du rofi clipboard manager  
Greenclip vers roficlip  
Roficlip integre les notification !!  
pas sur !!?
Pourquoi scrot + xclip fonctionne une fois sur deux ?
fonctionne avec la fenetre selectionné 
ne fonctionne pas avec tout l'écran !!

pour les screenshots maim !!? 
maim + xclip ?!!

bon alors en mono screen scrot + xclip fonctionne bien !!
sinon maim + xclip fonctionne aussi. maim est apparemment une version amelioré de scrot !! Donc à voir mais tant qu'a faire autant utiliser maim. A confirmer.
Est-ce que maim + xclip fonctionnent en dual screen ?
>[Lien screenshot de l'ecran actif](https://github.com/naelstrof/maim/issues/103)

outil a prendre en compte *xdotool*

envoyer une notification quand un screenshot est pris.
`basename 2018-04-07-103834_1366x768_scrot.png | while read OUTPUT; do notify-send "$OUTPUT";done`
S'inspirer de cette commande !!

`maim | xclip -selecetion clipboard -t image/png | notify-send "Screenshot !!" "$filename"`

Une ligne mis en commentaire pour invoquer rofi et tout de suite apres faire un screen, pour pouvoir faire un screen de rofi.
Maim + xclip + notify-send => permet de faire un screenshot, le mettre dans le clipboard, envoyer une notification comme quoi un screenshot a été fait !!(la notification precise si c'est un screenshot d'une fenetre active ou de tout l'écran).

xdotool
installer xdotool.  
utile pour faire une capture d'écran de la fenetre active avec maim !!
Mais pour servir à plein d'autres choses.

history des commandes pour voir comment il serait possible de sélectionner juste l'écran actif pour faire une capture !!!
les deux écrans sont considérés comme un seul écran sur la machine virtuelle.
> peut etre different sur une machine physique !!!  

```sh
    maim | feh - -x & maim -s cropped.png
    maim | feh - -x & maim -s cropped.png
    maim -x 0.0 | xclip -selection clipboard -t image/png
    maim -x .0.0 | xclip -selection clipboard -t image/png
    maim -x :0.0 | xclip -selection clipboard -t image/png
    maim -x $DISPLAY.1 | xclip -selection clipboard -t image/png
    maim -x :0.1 | xclip -selection clipboard -t image/png
    xrandr --listmonitors
    maim -s | xclip -selection clipboard -t image/png | notify-send "$f Screen shot taken"
    maim -s | xclip -selection clipboard -t image/png
    maim -x :0.1 | xclip -selection clipboard -t image/png
    maim -x :.1 | xclip -selection clipboard -t image/png
    maim -x :O.1 | xclip -selection clipboard -t image/png
    maim -x :O.0 | xclip -selection clipboard -t image/png
    maim -x :0.1 | xclip -selection clipboard -t image/png
    maim -x :0.0 | xclip -selection clipboard -t image/png
    maim -x :0.1 | xclip -selection clipboard -t image/png
    man convert
    man maim
    maim -g 1366x768
    maim -g 1366x768 | xclip -selection clipboard -t image/png
    man xdotool
    xdotool getmouselocation --shell
    xdotool get_num_desktops
    xdotool get_desktop_viewport --shell
    xdotool get_desktop_viewport
    xdotool get_desktop
    xdotool get_desktop_for_window $(xdotool getacwindow)
    xdotool get_desktop_for_window $(xdotool getactivewindow)
    man maim
    xdotool getactivewindow get_desktop_for_window
    xdotool getactivewindow
    xdotool getactivewindow --shell
    xdotool getactivewindow
    man slop
    man maim
    xwininfo
    xwininfo -children
    xwininfo -children -tree
    xwininfo -tree
    xwininfo -root
    echo $DISPLAY
```

python + xdotool
pip install python-libxdo -> pour utiliser xdotool avec python 
https://rshk.github.io/python-libxdo/library.html

vim plugin multi-cursor 
ajout d'un ligne dans zshrc pour désactiver une ancienne fonction des terminaux et pour que multi-cursor plugin de vim fonctionne.  
```sh
  # pour permettre à vim-multi-cursor de fonctionner
  # avec la touche <C-s>
  stty -ixon
```

outils pour aider a la configuration de i3 avec les fenetres.  
- xwinfo
- xdotool
- xprop

# CMUS - Console Music PLayer CLI
fichier de configuration dans $HOME/.config/cmus/.  

pour enregistrer la capture d'écran dans un fichier.  
clippaste > toto.png

vlc config
demarrage en mode minimaliste
skin minimaliste
choisir meilleur skin !!!
voir vlc notification avec dunst ??

playerctl - cli tool pour controller les media player. Spotify, Vlc etc.

[vim bootstrap](http://5.vim-bootstrap.appspot.com/)
pour générer un .vimrc personnalisé !!! 
A tester de facon urgente !!!


installation de calendar.vim
un calendrier dans vim + clock, peux synchro avec compte google.

il existe un outil CLI pour google keep ?! A VOIR
[CLI Google Keep](https://github.com/Nekmo/gkeep)

installation d'un colorscheme papercolor.

mise a jour du fichier de config i3.
Ajout d'un workspace 10.
Gaps personnalisé pour le workspace 7 - Musics / Media.
Ajout de for_window pour termite et terminator, pour les focus à l'ouverture. Comme en générale on les ouvrent pour faire quelque chose de ponctuel ou pas mais dans tout les cas c'est pour les utiliser directement.
Ajout d'un for_window pour les fenetres de dialogs de GVIM, qu'elles s'afichent dans le mem workspace que le GVIM focus, et qu'elles soient focus.
Assign VLC au workspace 7 - Musics / Media.
urxvt n'est plus assigné au workpsace 3 - Term.

Changement de la config de vim.
theme solarized_visibility mis à "normal".

erreurs yahourt
Quand il y a une erreur yaourt lors de l'installation d'un package :
- Editer le PKGBUILD, pour avoir la clé pgp.
- Ensuite l'ajouter à l'aide de :
  - `gpg --recv-keys <KEYID - See 'validpgpkeys' array in PKGBUILD>`.
- Ensuite reessayer d'installer le package.!

clipboard vim
[vim clipboard](https://wiki.archlinux.org/index.php/Vim#Clipboard)
mettre dans my_config.vim :
```
   set clipboard=unnamedplus
```

clipboard linux explication
[linux archlinux clipboard](https://wiki.archlinux.org/index.php/Clipboard)

pour vlc il doit y avoir un systeme de serveur-client un peu comme vim.

SPACEMACS
a voir !! 
[spacemacs](http://spacemacs.org/#)
Assez sympa va surement plair à un mickatronic xD

Music Player Daemon (MPD)
installation




Mise en forme en clair du fichier de config i3. Avec indentations et tout.

BLACKARCH DISTRIB
distribution archlinux pour pentesting.
installation : [Lien install](https://blackarch.org/downloads.html#install-repo)

installation de bmenu
dmenu like dans le terminal. Sorte de couteau suisse du menu xD.

installation de maia theme
install vibrancy theme
install adapta theme

utilisation de alsamixer
install volumeicon
pacmixer equivalent pour pulseaudio apparemment !!
A ajout dans le fichier de config de rofi :
```
    configuration {
        show-icons: true;
        drun-icon-theme: "MY_ICON_THEME";
    }
```
ou 
`rofi -show drun -show-icons -drun-icon-theme MY_ICON_THEME`.
juste :
`rofi -show drun -show-icons`

renommer `.Xdefaults` par `.Xresources`.

tasknc - ncurses wrapper for taskwarrior. Installation.

[collection de theme termite](https://github.com/khamer/base16-termite/tree/master/themes)
[using rofi with compton](https://github.com/DaveDavenport/rofi/wiki/Using-rofi-with-compton)

HDMI Manjaro solution
quand je connecte un ecran rien ne se passait.
la commande `xrandr --output HDMI1 --auto`, résouds en partie mon problème en dupliquant mon écran sur le second écran.

#Gestion du son sur manjaro 
[Lien à suivre](https://wiki.manjaro.org/index.php?title=Setting_the_Default_Sound_Device)
```
 0 [HDMI           ]: HDA-Intel - HDA Intel HDMI
                      HDA Intel HDMI at 0xd1710000 irq 34
 1 [PCH            ]: HDA-Intel - HDA Intel PCH
                      HDA Intel PCH at 0xd1714000 irq 31
```

#Rclone Browser
permet d'acceder à different service de stockage cloud comme dropbox ou drive.k

#NCMPCPP
NCMPCPP ( MPD Client)
installer mpd avant.
configurer le fichier `/etc/mpd.conf`.
`cd ~ && mkdir .ncmpcpp`.
`cp /usr/share/doc/ncmpcpp/config ~/.ncmpcpp/`.
quand nouveau fichier de music ajouté dans le dossier de musique, base de données mpd n'est pas bien mis à jour !!?
problem a voir.
plus tard c'est chiant !!! Peut etre sur Arch juste !!! A voir sur debian ?!

#MPD and MOPIDY
(Lien article blog)[http://ellengummesson.com/blog/2014/08/31/mopidy-and-ncmpcpp/]
- Mopidy remplace mpd ?
- Est-ce que mopidy est mieux que mpd du coup ?

#MOPIDY
installer mopidy
installer mopidy-spotify

Mopidy permet avec ses pligins de lire des musics sur le cloud comme spotify ou soudclound par exemple.
Mais apparemment le maintient n'est pas très actif !!


#Simple Terminal
>Un terminal qui a l'air pas mal à voir !!

#NETTOYER LE CACHE DES PACKAGES SUR ARCHLINUX
(Lien à lire)[https://www.ostechnix.com/recommended-way-clean-package-cache-arch-linux/]


#VIM AND PYTHON 
(lien de l'article)[https://realpython.com/vim-and-python-a-match-made-in-heaven/#auto-complete]

