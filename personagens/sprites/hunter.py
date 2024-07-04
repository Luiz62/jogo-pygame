from pygame import image, transform
from app.constants import const_character as cst, const
from personagens.sprites.character import Character

class Hunter(Character):
    def __init__(self):
        # call Character initializer
        Character.__init__(self)

        self.name = 'HUNTER'

        self.image = transform.scale(image.load(const.IMG_HUNTER),
                                     (32*cst.SCALE_CHAMPS, 32*cst.SCALE_CHAMPS))

        self.rect = self.image.get_rect()

        self.rect.center = (0, 0)

        self.attack = cst.Statistics_character_player[self.name]['ATTACK']

        self.defense = cst.Statistics_character_player[self.name]['DEFENSE']

        self.speed = cst.Statistics_character_player[self.name]['SPEED']

        self.hp = cst.Statistics_character_player[self.name]['HP']

        self.hp_root = cst.Statistics_character_player[self.name]['HP']

        self.skill_value = cst.Statistics_character_player[self.name]['SKILL']

    # O Hunter usa seu arco prefurante, diminuindo a defesa dos inimigos
    def skill(self, dic):
        enemy_1 = dic['enemy_1']
        enemy_2 = dic['enemy_2']
        enemy_1.defense -= self.skill_value
        enemy_2.defense -= self.skill_value
