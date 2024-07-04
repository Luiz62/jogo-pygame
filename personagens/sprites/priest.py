from pygame import image, transform
from app.constants import const_character as cst, const
from personagens.sprites.character import Character


class Priest(Character):
    def __init__(self):
        # call Character initializer
        Character.__init__(self)

        self.name = 'PRIEST'

        self.image = transform.scale(image.load(const.IMG_PRIEST_SHADOW),
                                     (32*cst.SCALE_CHAMPS, 32*cst.SCALE_CHAMPS))

        self.rect = self.image.get_rect()

        self.rect.center = (0, 0)

        self.attack = cst.Statistics_character_player[self.name]['ATTACK']

        self.defense = cst.Statistics_character_player[self.name]['DEFENSE']

        self.speed = cst.Statistics_character_player[self.name]['SPEED']

        self.hp = cst.Statistics_character_player[self.name]['HP']

        self.hp_root = cst.Statistics_character_player[self.name]['HP']

        self.skill_value = cst.Statistics_character_player[self.name]['SKILL']

    # O cura ele ou um aliado;
    def skill(self, ally):
        ally.hp += self.skill_value