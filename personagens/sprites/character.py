from pygame.sprite import Sprite

class Character(Sprite):
    def __init__(self):
        # call Sprite initializer
        Sprite.__init__(self)

        self.name = ''

        self.image = None

        self.attack = 0

        self.defense = 0

        self.speed = 0

        self.hp = 0

        self.hp_root = 0

        self.in_game = True

        self.resert = False

    def attacks(self, enemy_defense):
        damage = self.attack * (50 / (50 + enemy_defense))
        return damage

    def receive_attack(self, damage):
        self.hp -= damage

    def receive_defense(self):
        self.defense *= 2

    def back_defense(self):
        self.defense /= 2

    def update(self):
        if self.hp <= 0 and self.in_game:
            self.rect.x = 800
            self.in_game = False

        if self.resert:
            self.hp = self.hp_root
            self.rect.center = (0, 0)
            self.in_game = True
            self.resert = not self.resert

