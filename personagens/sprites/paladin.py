import pygame as pg
from pygame import transform
from app.constants import const_character as cst, const
from personagens.sprites.character import Character


class Paladin(Character):
    def __init__(self):
        # call Character initializer
        Character.__init__(self)

        self.name = 'PALADIN'

        self.image = transform.scale(pg.image.load(const.IMG_PALADIN),
                                     (32*cst.SCALE_CHAMPS, 32*cst.SCALE_CHAMPS))

        self.rect = self.image.get_rect()

        self.rect.center = (0, 0)

        self.attack = cst.Statistics_character_player[self.name]['ATTACK']

        self.defense = cst.Statistics_character_player[self.name]['DEFENSE']

        self.speed = cst.Statistics_character_player[self.name]['SPEED']

        self.hp = cst.Statistics_character_player[self.name]['HP']

        self.hp_root = cst.Statistics_character_player[self.name]['HP']

        self.skill_value = cst.Statistics_character_player[self.name]['SKILL']

    # O protege seus aliados, aumentando a defesa deles
    def skill(self, dic):
        dic['character_1'].defense += self.skill_value
        dic['character_2'].defense += self.skill_value
        dic['character_3'].defense += self.skill_value
