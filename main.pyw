import os
import sys
from app.game import Game
import pygame as pg
import ctypes

dirpath = os.getcwd()
sys.path.append(dirpath)

if getattr(sys, 'frozen', False):
    os.chdir(sys._MEIPASS)

# function 'main'
def main():

    if not pg.font:
        print("Warning, fonts disabled")
    if not pg.mixer:
        print("Warning, sound disabled")

    jogo = Game()

    jogo.view_screen_start()

    while jogo.running:
        jogo.new_game()


# this calls the 'main' function when this script is executed
if __name__ == '__main__':
    ctypes.windll.kernel32.FreeConsole()
    main()
