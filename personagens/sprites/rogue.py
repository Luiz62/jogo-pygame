from pygame import image, transform
from app.constants import const_character as cst, const
from personagens.sprites.character import Character


class Rogue(Character):
    def __init__(self):
        # call Character initializer
        Character.__init__(self)

        self.name = 'ROGUE'

        self.image = transform.scale(image.load(const.IMG_ROGUE), (32*cst.SCALE_CHAMPS, 32*cst.SCALE_CHAMPS))

        self.rect = self.image.get_rect()

        self.rect.center = (0, 0)

        self.attack = cst.Statistics_character_player[self.name]['ATTACK']

        self.defense = cst.Statistics_character_player[self.name]['DEFENSE']

        self.speed = cst.Statistics_character_player[self.name]['SPEED']

        self.hp = cst.Statistics_character_player[self.name]['HP']

        self.hp_root = cst.Statistics_character_player[self.name]['HP']

        self.skill_value = cst.Statistics_character_player[self.name]['SKILL']

    # Aumenta o seu ataque
    def skill(self):
        self.attack += self.skill_value
