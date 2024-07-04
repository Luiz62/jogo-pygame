from pygame import image, transform
from app.constants import const_character as cst, const
from personagens.sprites.character import Character


class Wizard(Character):
    def __init__(self):
        # call Character initializer
        Character.__init__(self)

        self.name = 'WIZARD'

        self.image = transform.scale(image.load(const.IMG_WIZARD_RIGHT),
                                     (32*cst.SCALE_CHAMPS, 32*cst.SCALE_CHAMPS))

        self.rect = self.image.get_rect()

        self.rect.center = (0, 0)

        self.attack = cst.Statistics_character_player[self.name]['ATTACK']

        self.defense = cst.Statistics_character_player[self.name]['DEFENSE']

        self.speed = cst.Statistics_character_player[self.name]['SPEED']

        self.hp = cst.Statistics_character_player[self.name]['HP']

        self.hp_root = cst.Statistics_character_player[self.name]['HP']

        self.skill_value = cst.Statistics_character_player[self.name]['SKILL']

    def attacks_all(self, enemy_defense):
        damage = self.skill_value * (50 / (50 + enemy_defense))
        return damage

    # Usa uma magia que causa dano a todos os inimigos
    def skill(self, dic):
        enemy_1 = dic['enemy_1']
        enemy_2 = dic['enemy_2']
        damage_1 = self.attacks_all(enemy_1.defense)
        damage_2 = self.attacks_all(enemy_2.defense)
        enemy_1.receive_attack(damage_1)
        enemy_2.receive_attack(damage_2)
