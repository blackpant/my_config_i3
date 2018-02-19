syntax on
filetype on

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

" Colorscheme
colorscheme solarized
" set background=dark
set number
"let g:lightline = {
      "\ 'colorscheme': 'solarized',
      "\ }
