import pygame as pg

from app.constants import const


class Text:
    def __init__(self, text, screen):
        self.__text = text
        self.__screen = screen
        self.__font = None

    @property
    def text(self):
        return self.__text

    def render_text_font_firacode(self, size, bold, color):
        font = pg.font.SysFont(const.FONT[1], size, bold)
        text = font.render(self.__text, True, color)
        return text

    @staticmethod
    def render_text_font_firacode_with_text(text, size, bold, color):
        font = pg.font.SysFont(const.FONT[1], size, bold)
        text = font.render(text, True, color)
        return text

    def render_text_font_arial(self, size, bold, color):
        font = pg.font.SysFont(const.FONT[2], size, bold)
        text = font.render(self.__text, True, color)
        return text

    def render_text_font_gabriola(self, size, bold, color):
        font = pg.font.SysFont(const.FONT[3], size, bold)
        text = font.render(self.__text, True, color)
        return text

    def __render_text_topleft(self, text, offset):
        x, y = offset
        rect = text.get_rect()
        rect.topleft = (x, y)
        self.__screen.blit(text, rect)

    def __render_text_center(self, text, offset):
        x, y = offset
        rect = text.get_rect()
        rect.center = (x, y)
        self.__screen.blit(text, rect)

    def render_text_turn(self):
        self.__text += "'S TURN!"
        text = self.render_text_font_firacode(const.TEXT_TURN_SIZE, True, const.TEXT_TURN_COLOR)
        self.__render_text_topleft(text, const.TEXT_TURN_OFFSET)

    def render_text_enemy_statistics_name(self, s1, s2, s3, s4):
        self.__text += " STATISTICS!"
        text = self.render_text_font_firacode(18, True, const.TEXT_TURN_COLOR)
        self.__render_text_topleft(text, const.TEXT_TURN_OFFSET)

        text_1, offset_1 = 'ATTACK: {:.0f}'.format(s1), [70, 465]
        text_2, offset_2 = 'DEFENSE: {:.0f}'.format(s2), [240, 465]
        text_3, offset_3 = 'HP: {:.0f}'.format(s3), [70, 510]
        text_4, offset_4 = 'DAMAGE: {:.0f}'.format(s4), [240, 510]

        list_statistics = [[text_1, offset_1], [text_2, offset_2], [text_3, offset_3], [text_4, offset_4]]
        self.__render_enemy_statistics(list_statistics)

    def __render_enemy_statistics(self, lst):
        for element in lst:
            text = self.render_text_font_firacode_with_text(element[0], 18, True, const.TEXT_TURN_COLOR)
            self.__render_text_topleft(text, element[1])

    def render_text_hp(self, x, y):
        text = self.render_text_font_firacode(20, True, (248, 248, 248))
        self.__render_text_topleft(text, (x, y))

    def render_text_end_game(self, size, color, offset):
        text = self.render_text_font_firacode(size, True, color)
        self.__render_text_topleft(text, offset)

    def render_text_target(self, size, color, offset):
        text = self.render_text_font_firacode(size, True, color)
        self.__render_text_topleft(text, offset)

    def render_text_action(self, size, color, offset):
        text = self.render_text_font_firacode(size, True, color)
        self.__render_text_topleft(text, offset)

    def render_text_defeated(self, size, color, offset):
        text = self.render_text_font_firacode(size, True, color)
        self.__render_text_topleft(text, offset)

    def render_text_introbattle(self, size, color, offset):
        text = self.render_text_font_arial(size, False, color)
        self.__render_text_center(text, offset)

    def render_text_screen_end_game(self, size, color, offset):
        text = self.render_text_font_gabriola(size, False, color)
        self.__render_text_center(text, offset)

    def render_text_buttons_screen_game(self, size, color, offset):
        text = self.render_text_font_firacode(size, True, color)
        self.__render_text_topleft(text, offset)