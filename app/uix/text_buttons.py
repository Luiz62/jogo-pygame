import pygame as pg
from app.constants import const

class TextButtons:
    def __init__(self, text, size, color, offset):
        self.__text = text
        self.__size = size
        self.__color = color
        self.__x, self.__y = offset
        self.__bold = False

    @property
    def text(self):
        return self.__text

    def __text_highlight(self):
        self.__size = 25
        self.__bold = True

    def __text_not_highlight(self):
        self.__size = 20
        self.__bold = False

    def __render_text(self, screen):
        font = pg.font.SysFont(const.FONT[2], self.__size, self.__bold)
        text = font.render(self.__text, True, self.__color)
        rect = text.get_rect()
        rect.center = (self.__x, self.__y)
        screen.blit(text, rect)

    def show_text(self, highlight, screen):
        if highlight:
            self.__text_highlight()
        else:
            self.__text_not_highlight()

        self.__render_text(screen)