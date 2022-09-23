call plug#begin('~/.local/share/nvim/site/autolad/plug.vim')
Plug 'sheerun/vim-polyglot'
Plug 'jiangmiao/auto-pairs'
Plug 'neoclide/coc.nvim' , { 'branch' : 'release' }
Plug 'dense-analysis/ale'
call plug#end()

" Remap de botões.
" Salva e compila arquivos python no botão <END> (se quiser mudar, é só trocar
" o "END" outro botão. Pode ser F5, F10, etc.
autocmd FileType python map <buffer> <END> :w<CR>:exec '!python3' shellescape(@%, 1)<CR>
autocmd FileType python imap <buffer> <END> <esc>:w<CR>:exec '!python3' shellescape(@%, 1)<CR>

" Adicionando Control + C, Control + V e Control + X para que seja possível
" copiar comandos do VIM para programas externos. Ps.: nativo do VIM, não
" precisa de plug-ins.

vmap <C-c> "+yi
vmap <C-x> "+c
vmap <C-v> c<ESC>"+p
imap <C-v> <ESC>"+pa
" Fim remap de botões

" PlugIn ALE """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" Coloque embaixo os linters desejados para o ALE. Deixarei apenas o pylint
" se precisar de mais algum, como o autopep8, é só adicionar na lista abaixo.
" A síntaxe é apenas uma normal de lista de Python, apenas coloque ",
" NomeDoPrograma".
let g:ale_linters = {
\    'python': ['pylint']
\}

" Fixers são os que fazem modificações no programa para você, exemplo: já
" colocar no formato pep8 quando sai. Nesse caso, apenas está habilitado o que
" apaga os espaços vazios de linhas vazias, para que o código não fique cheio
" de caracteres desnecessário, para o interpretador perder tempo ignorando, ao compilar.
let g:ale_fixers = {
\   '*': ['trim_whitespace'],
\}

" Permite que o fixer acima haja ao salvar o arquivo.
let g:ale_fix_on_save = 1

" Aqui ficam os plug-ins do coc.Formas de utilizar a auto-completação: Curso para baixo/cima, mais Control + Y para auto-completar
" Ou Control + N/ Control + P para se mover entre as opções completando automaticamente. 
" N de Next e P de Preview. Y de Yank, essa é a lógica da auto-completação.
" Utilize SHIFT + k (k maiúsculo) para abrir a documentação da função.
let g:coc_global_extensions = [ 'coc-snippets', ]

" Configurações nativas do VIM. Eu pensei em deixar perto do copiar e colar,
" que também é nativo, mas ali é um remap, aqui não.
" Global Sets """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
syntax on            " Enable syntax highlight
set nu               " Enable line numbers
set tabstop=4        " Show existing tab with 4 spaces width
set softtabstop=4    " Show existing tab with 4 spaces width
set shiftwidth=4     " When indenting with '>', use 4 spaces width
set expandtab        " On pressing tab, insert 4 spaces
set smarttab         " insert tabs on the start of a line according to shiftwidth
set smartindent      " Automatically inserts one extra level of indentation in some cases
set hidden           " Hides the current buffer when a new file is openned
set incsearch        " Incremental search
set ignorecase       " Ingore case in search
set smartcase        " Consider case if there is a upper case character
set scrolloff=8      " Minimum number of lines to keep above and below the cursor
set colorcolumn=79  " Draws a line at the given line to keep aware of the line size
set signcolumn=yes   " Add a column on the left. Useful for linting
set cmdheight=2      " Give more space for displaying messages
set updatetime=100   " Time in miliseconds to consider the changes
set encoding=utf-8   " The encoding should be utf-8 to activate the font icons
set nobackup         " No backup files
set nowritebackup    " No backup files
set splitright       " Create the vertical splits to the right
set splitbelow       " Create the horizontal splits below
set autoread         " Update vim after file update from outside
set mouse=a          " Enable mouse support
filetype on          " Detect and set the filetype option and trigger the FileType Event
filetype plugin on   " Load the plugin file for the file type, if any
filetype indent on   " Load the indent file for the file type, if any


