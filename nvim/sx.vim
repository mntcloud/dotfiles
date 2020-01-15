" =============================================================================
" Filename: autoload/lightline/colorscheme/sx.vim
" Author: quant0x2
" License: MIT License
" Last Change: 2013/09/07 12:23:38.
" =============================================================================
let s:white = '#e4e4e4'
let s:base3 = '#c5c8c6'
let s:base2 = '#bababa'
let s:base1 = '#a0a0a0'
let s:base0 = '#909090'
let s:base00 = '#666666'
let s:base01 = '#121212'
let s:base02 = '#212121' " maybe set #262626
let s:base023 = '#303030'
let s:base03 = '#1d1f21'
let s:red = '#e98885'
let s:orange = '#de935f'
let s:yellow = '#ffc68d'
let s:green = '#a3c38b'
let s:cyan = '#00a69f'
let s:blue = '#a6cae2'
let s:magenta = '#e7cdfb'

let s:p = {'normal': {}, 'inactive': {}, 'insert': {}, 'replace': {}, 'visual': {}, 'tabline': {}}
let s:p.normal.left = [ [ s:white, s:base02 ], [ s:white , s:base02 ]]
let s:p.normal.right = [ [ s:white, s:base02 ], [ s:white, s:base02 ] ]
let s:p.inactive.right = [ [ s:base00, s:base01 ], [ s:base00, s:base01 ] ]
let s:p.inactive.left =  [ [ s:base00, s:base01 ], [ s:base00, s:base01 ] ]
let s:p.insert.left = [ [ s:base02, s:green ], [ s:base3, s:base01 ] ]
let s:p.insert.right = copy(s:p.insert.left)
let s:p.replace.left = [ [ s:base02, s:orange ], [ s:base3, s:base01 ] ]
let s:p.visual.left = [ [ s:base02, s:magenta ], [ s:base3, s:base01 ] ]
let s:p.normal.middle = [ [ s:base1, s:base01 ] ]
let s:p.inactive.middle = [ [ s:base0, s:base01 ] ]
let s:p.tabline.left = [ [ s:white, s:base02 ] ]
let s:p.tabline.tabsel = [ [ s:white, s:base02 ] ]
let s:p.tabline.middle = [ [ s:base02, s:base01 ] ]
let s:p.tabline.right = copy(s:p.normal.right)
let s:p.normal.error = [ [ s:red, s:base023 ] ]
let s:p.normal.warning = [ [ s:yellow, s:base02 ] ]

let g:lightline#colorscheme#sx#palette = lightline#colorscheme#fill(s:p)
