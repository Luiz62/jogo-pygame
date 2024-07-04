from app.constants import const
from pygame import transform
class LayoutMenu:
    def __init__(self, img, offset, screen):
        self.__img = img
        self.__w, self.__h = const.LAYOUT_DIM
        self.__x, self.__y = offset
        self.__screen = screen

    def render_layout(self):
        self.__img = transform.scale(self.__img, (self.__w, self.__h))
        rect = self.__img.get_rect()
        rect.x, rect.y = self.__x, self.__y
        self.__screen.blit(self.__img, rect)

    def render_layout_center(self):
        self.__img = transform.scale(self.__img, (self.__w, self.__h))
        rect = self.__img.get_rect()
        rect.center = (self.__x, self.__y)
        self.__screen.blit(self.__img, rect)