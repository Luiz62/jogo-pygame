from pygame import image, transform
from app.constants import const_character as cst, const
from personagens.sprites.character import Character

class Necromancer(Character):
    def __init__(self):
        # call Character initializer
        Character.__init__(self)

        self.name = 'NECROMANCER'

        self.image = transform.scale(image.load(const.IMG_NECROMANCER_LEFT),
                                     (32 * cst.SCALE_CHAMPS, 32 * cst.SCALE_CHAMPS))

        self.rect = self.image.get_rect()

        self.rect.center = (0, 0)

        self.attack = cst.Statistics_character_computer[self.name]['ATTACK']

        self.defense = cst.Statistics_character_computer[self.name]['DEFENSE']

        self.speed = cst.Statistics_character_computer[self.name]['SPEED']

        self.hp = cst.Statistics_character_computer[self.name]['HP']

        self.hp_root = cst.Statistics_character_computer[self.name]['HP']

        self.skill_value = cst.Statistics_character_computer[self.name]['SKILL']

    # Adiciona vida a ele e seu aliado
    def skill(self, dic):
        self.hp += self.skill_value
        dic['enemy_2'].hp += self.skill_value

    def insight(self):
        return self.attack, self.defense, self.hp

