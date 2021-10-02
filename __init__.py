"""
This code will only work on Linux and Mac OS X systems,
and only in terminal emulators with true color available,

How to check if your terminal has true color, write down this 
command in your terminal:
    
printf "\x1b[38;2;255;100;0mTRUECOLOR\x1b[0m\n"

If the terminal does NOT print "TRUECOLOR" in red, your terminal 
does not support it. 

What terminal emulator support true color? 
    Check this gist:
        https://gist.github.com/XVilka/8346728#terminals--true-color
"""
from themify.colormate import *
