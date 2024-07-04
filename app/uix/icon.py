from pygame import transform

class Icon:
    """
    (x, y): posição
    (width, height): altura e largura
    """
    def __init__(self, dim, offset):
        self.__width, self.__height = dim
        self.__x, self.__y = offset

    def returnIcon(self, img):
        icon = img
        icon = transform.scale(icon, (self.__width * 3, self.__height * 3))
        icon_rect = icon.get_rect()
        icon_rect.center = (self.__x, self.__y)

        return icon, icon_rect
