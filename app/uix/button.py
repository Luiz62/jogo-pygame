import pygame as pg
from app.uix.text import Text

class ButtonScreenGame:
    """
        text : Texto
        font : Fonte
        size  : Tamanho
        color : Cor
        offset : X, Y
    """
    def __init__(self, text, font, size, color, offset):
        self.__text = text
        self.__font = font
        self.__size = size
        self.__color = color
        self.__x, self.__y = offset
        self.__highlight = False

    @property
    def text(self):
        return self.__text

    @property
    def highlight(self):
        return self.__highlight

    def toggle_highlight(self):
        self.__highlight = not self.__highlight

    def __str__(self):
        return self.__text

    def __render_text(self, screen):
        text = Text(self.__text, screen)
        text.render_text_buttons_screen_game(self.__size, self.__color, (self.__x, self.__y))

    def render(self, screen: pg.Surface):
        self.__render_text(screen)

class ButtonScreenStart:
    """
    text            : texto a ser exibido no botão
    (    x,      y) : posição
    (width, height) : altura e largura
    highlight       : nosso botão está destacado?
    """

    def __init__(self, text, dim, offset, icon):
        self.__text = text
        self.__w, self.__h = dim
        self.__x, self.__y = offset
        self.__icon = icon
        self.__highlight = False

    @property
    def highlight(self):
        return self.__highlight

    def toggle_highlight(self):
        self.__highlight = not self.__highlight

    def __str__(self):
        return self.__text.text

    def __render_text(self, screen):
        self.__text.show_text(self.__highlight, screen)

    def __render_button(self, screen, images, icon_name):
        button = pg.transform.scale(images[icon_name], (384, 384))
        button_rect = button.get_rect()
        button_rect.center = (self.__x, self.__y)
        screen.blit(button, button_rect)

    def __render_icon(self, screen, images):
        icon, icon_rect = self.__icon.returnIcon(images[self.__text.text])
        screen.blit(icon, icon_rect)

    def render(self, screen: pg.Surface, images: dict):

        self.__render_text(screen)

        if self.__icon is not None:
            self.__render_button(screen, images, "menu")

        if self.__icon is not None:
            self.__render_icon(screen, images)
