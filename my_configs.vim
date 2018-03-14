syntax on
filetype on


" Lightline setting
let g:lightline = {
    \ 'colorscheme': 'tender',
    \ 'separator': {'left':'', 'right': ''},
    \ 'subseparator': {'left':'', 'right': ''},
    \ }

" Set font according to system
if has("mac") || has("macunix")
    set gfn=Hack:h14,Source\ Code\ Pro:h15,Menlo:h15
elseif has("win16") || has("win32")
    set gfn=Hack:h14,Source\ Code\ Pro:h12,Bitstream\ Vera\ Sans\ Mono:h11
elseif has("gui_gtk2")
    set gfn=Hack\ 11,Source\ Code\ Pro\ 11,Bitstream\ Vera\ Sans\ Mono\ 10
elseif has("linux")
    set gfn=Hack\ 11,Source\ Code\ Pro\ 11,Bitstream\ Vera\ Sans\ Mono\ 10
elseif has("unix")
    set gfn=Monospace\ 11
endif

set number

" Colorscheme
let g:solarized_termtrans = 1
colorscheme solarized
set background=dark
call togglebg#map("<F5>")

" syntastic python checker
let g:syntastic_python_checkers = ['flake8']

" open-browser plugin binding key
let g:netrw_nogx = 1 " disable netrw's gx mapping
nmap gx <Plug>(openbrowser-smart-search)
vmap gx <Plug>(openbrowser-smart-search)

" vv to generate new vertical split
nnoremap <silent> vv <C-w>v

" Prompt for a command to run
map <Leader>vp :VimuxPromptCommand<CR>

" Close vimux runner
map <Leader>vc :VimuxCloseRunner<CR>

" set up easytags
set tags=./tags;
let g:easytags_dynamic_files = 1
" let g:easytags_events = ['BufWritePost']

" Tagbar setting
nmap <F8> :TagbarToggle<CR>

" config ack-vim
map <Leader>g :Ack! 

" Escape character remap exit mode insert
inoremap kj <Esc>

" taskwarrior.vim setting
let g:task_rc_override = 'rc.defaultheight=0'

" set new line caracter
set listchars=tab:ˉ\ ,eol:¬
set list
