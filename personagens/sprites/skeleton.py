from pygame import image, transform
from app.constants import const_character as cst, const
from personagens.sprites.character import Character

class Skeleton(Character):
    def __init__(self):
        # call Character initializer
        Character.__init__(self)

        self.name = 'SKELETON'

        self.image = transform.scale(image.load(const.IMG_SKELETON_LEFT),
                                     (32 * cst.SCALE_CHAMPS, 32 * cst.SCALE_CHAMPS))

        self.rect = self.image.get_rect()

        self.rect.center = (0, 0)

        self.attack = cst.Statistics_character_computer[self.name]['ATTACK']

        self.defense = cst.Statistics_character_computer[self.name]['DEFENSE']

        self.speed = cst.Statistics_character_computer[self.name]['SPEED']

        self.hp = cst.Statistics_character_computer[self.name]['HP']

        self.hp_root = cst.Statistics_character_computer[self.name]['HP']

        self.skill_value = cst.Statistics_character_computer[self.name]['SKILL']

    # Se sua vida estiver abaixo de 13% da vida total, seu poder de ataque é triplicado
    # Do contrário são adicionados mais quatro pontos ao seu ataque
    def skill(self):
        if self.hp <= self.hp_root * 13/100:
            self.attack *= self.skill_value
            return 0
        else:
            self.attack += self.skill_value + 1
            return 1

    def insight(self):
        return self.attack, self.defense, self.hp