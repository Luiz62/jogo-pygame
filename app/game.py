from app.constants import const
import pygame as pg
from pygame import transform
from personagens.sprites import paladin, rogue, wizard, hunter, priest, skeleton, necromancer
from app.uix.button import ButtonScreenStart as Bt1
from app.uix.button import ButtonScreenGame as Bt2
from app.uix.menu import Menu, MenuGame
from app.uix.text import Text
from app.uix.icon import Icon
from app.uix.text_buttons import TextButtons

class Screen:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def screen_size(self):
        return self.__width, self.__height

class Game:
    def __init__(self):

        pg.init()

        # iniciar mixer
        pg.mixer.init()

        # tela
        self.__s = Screen(const.WIDTH, const.HEIGHT)
        self.__screen = pg.display.set_mode(self.__s.screen_size())

        # nome da tela
        pg.display.set_caption(const.TITLE_GAME)

        # imagens
        self.__img_bg = transform.scale(pg.image.load(const.DIR_IMG_MENU_BG), (1536/2, 1152/2))
        self.__images = None
        self.__img_menu_game = None

        # relogio
        self.__timer = pg.time.Clock()

        # character selected
        self.__selected = []

        self.__playing = True

        # menu
        self.__menu = None
        self.__icon = []
        self.__text = []
        self.__list_buttons = []

        self.__introbattle = Text(const.TEXT_INTRO[0], self.__screen)

        # game
        self.__menu_game = None
        self.__list_buttons_game = []
        self.__running = True

        # sprites
        self.__start_sprites = None

        # sounds
        self.__sounds = None

        # sprites group
        self.__allsprites = pg.sprite.Group()

        self.__waiting_player = False

        # carregando items
        self.__load_items()
        self.__load_imgs()
        self.__load_sounds()
        self.__load_buttons()
        self.__load_start_sprites()

    @property
    def running(self):
        return self.__running

    def new_game(self):
        self.__load_sprites()
        self.__screen.fill(const.COLOR['BLACK'])
        self.run()

    def __load_start_sprites(self):
        self.__start_sprites = [
            paladin.Paladin(),
            rogue.Rogue(),
            wizard.Wizard(),
            hunter.Hunter(),
            priest.Priest(),
            skeleton.Skeleton(),
            necromancer.Necromancer()
        ]

    # carregar sprites
    def __load_sprites(self):

        # add characters
        for k, item in enumerate(self.__selected):
            self.__start_sprites[item].rect.x = const.POS_CHAMPS_GAME[k][0]
            self.__start_sprites[item].rect.y = const.POS_CHAMPS_GAME[k][1]
            self.__allsprites.add(self.__start_sprites[item])

        # add enemys
        for k, i in enumerate(range(-1, -3, -1)):
            self.__start_sprites[i].rect.x = const.POS_ENEMY_GAME[k][0]
            self.__start_sprites[i].rect.y = const.POS_ENEMY_GAME[k][1]
            self.__allsprites.add(self.__start_sprites[i])

    # carregar tela
    def __load_screen(self):
        self.__screen.fill(const.COLOR['BLACK'])

        self.__screen.blit(self.__img_bg, (0, 0))

        if self.__menu_game is None:
            self.__view_screen_game()

        self.__menu_game.render()

        self.__allsprites.draw(self.__screen)

    def __load_items(self):
        for i in range(5):
            self.__icon.append(Icon((32, 32), const.POS_MENU_CHAMPS[i]))
        for i in range(5):
            self.__text.append(TextButtons(const.CHAMPS_MENU[i], 20, const.COLOR['WHITE'], const.POS_MENU_NAMES[i]))

    # carregar botões
    def __load_buttons(self):
        for i in range(5):
            self.__list_buttons.append(Bt1(self.__text[i], (128 * 3, 128 * 3), const.POS_MENU[i], self.__icon[i]))
        for i in range(4):
            self.__list_buttons_game.append(Bt2(
                const.BUTTONS_GAME_NAME[i],
                const.BUTTONS_GAME_FONT,
                const.BUTTONS_GAME_SIZE,
                const.BUTTONS_GAME_COLOR,
                const.BUTTONS_GAME_OFFSET[i],
            ))

    # carregar imagens
    def __load_imgs(self):
        self.__images = {
            'menu': pg.image.load(const.IMG_MENU)
        }
        self.__img_menu_game = {
            'menu_1': pg.image.load(const.IMG_GAME_1),
            'menu_2': pg.image.load(const.IMG_GAME_2),
            'menu_3': pg.image.load(const.IMG_GAME_3),
            'arrow_right': pg.image.load(const.IMG_ARROW_RIGHT),
            'arrow_down': pg.image.load(const.IMG_ARROW)
        }
        for i in range(5):
            self.__images[const.CHAMPS_MENU[i]] = pg.image.load(const.LIST_CHAMPS[i])

    def __load_sounds(self):

        sound_next = pg.mixer.Sound(const.DIR_SOUND_NEXT_BUTTON)
        sound_next.set_volume(0.1)

        sound_selected = pg.mixer.Sound(const.DIR_SOUND_SELECTED)
        sound_selected.set_volume(0.1)

        self.__sounds = {
            'sound_next': sound_next,
            'sound_selected': sound_selected
        }
        self.__sounds['sound_next'].set_volume(0.5)

    # function run
    def run(self):

        self.__load_screen()

        # loop main
        while self.__playing:

            self.__timer.tick(const.FRAMERATE)

            self.__events()

            if self.__menu_game.finish:
                self.__playing = False

            if self.__menu_game.close_game:
                self.__playing = False
                self.__running = False

            pg.display.flip()

        if self.running:
            self.__view_screen_game_over()

    def __events(self):

        for event in pg.event.get():

            if event.type == pg.QUIT:
                self.__playing = False
                self.__running = False

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_a or event.key == pg.K_LEFT:
                    self.__menu_game.next('left', True)

                if event.key == pg.K_d or event.key == pg.K_RIGHT:
                    self.__menu_game.next('right', True)

                if event.key == pg.K_w or event.key == pg.K_UP:
                    self.__menu_game.next('up', True)

                if event.key == pg.K_s or event.key == pg.K_DOWN:
                    self.__menu_game.next('down', True)

                if event.key == pg.K_z or event.key == pg.K_SPACE:
                    self.__sounds['sound_selected'].play()
                    self.__menu_game.select_action()

    def view_screen_start(self):

        self.__menu = Menu(self.__screen, self.__list_buttons, self.__sounds)

        self.__waiting_player = True
        self.__wait_player()

    def __wait_player(self):
        while self.__waiting_player:

            self.__timer.tick(const.FRAMERATE)

            self.__screen.fill(const.COLOR['BLACK'])

            self.__screen.blit(self.__img_bg, (0, 0))

            # retângulo preto
            pg.draw.rect(self.__screen, const.COLOR['BLACK'], ((const.WIDTH / 2 - 150, 25), (300, 60)), 0)

            # linha horizontal de cima
            pg.draw.line(self.__screen, const.COLOR['WHITE'], [234, 25], [534, 25], 3)

            # linha horizontal de baixo
            pg.draw.line(self.__screen, const.COLOR['WHITE'], [234, 83], [534, 83], 3)

            # linha vertical da esquerda
            pg.draw.line(self.__screen, const.COLOR['WHITE'], [234, 25], [234, 83], 3)

            # linha vertical da direita
            pg.draw.line(self.__screen, const.COLOR['WHITE'], [534, 25], [534, 83], 3)

            self.__introbattle.render_text_introbattle(const.TEXT_INTRO[1], const.TEXT_INTRO[2], const.TEXT_INTRO[3])

            self.__menu.render(self.__images)

            if len(self.__selected) >= 3:
                self.__waiting_player = False
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.__waiting_player = False
                    self.__running = False

                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_a or event.key == pg.K_LEFT:
                        self.__menu.next('left', True)

                    elif event.key == pg.K_d or event.key == pg.K_RIGHT:
                        self.__menu.next('right', True)

                    elif event.key == pg.K_z:
                        self.__sounds['sound_selected'].play()
                        if len(self.__selected) == 0:
                            self.__selected.append(self.__menu.get_current())
                            self.__menu.next('right')
                        else:
                            valor = self.__menu.get_current()
                            if valor not in self.__selected:
                                self.__selected.append(valor)
                                self.__menu.next('right')

            if len(self.__selected) > 2:
                self.__waiting_player = False

            pg.display.flip()

    def __view_screen_game(self):

        self.__menu_game = MenuGame(
            self.__screen,
            self.__list_buttons_game,
            self.__img_menu_game,
            self.__img_bg,
            self.__sounds,
            self.__selected,
            self.__allsprites
        )

        pg.display.update()

    # tela fim de jogo
    def __view_screen_game_over(self):
        # desativada
        self.__waiting_player = False

        self.__screen.fill(const.COLOR['BLACK'])

        self.__screen.blit(self.__img_bg, (0, 0))

        pg.draw.rect(
            self.__screen, const.COLOR['BLACK'], ((const.WIDTH / 2 - 100, const.HEIGHT / 2 - 20), (200, 40)), 0)

        text_end_game = Text('END GAME', self.__screen)
        text_end_game.render_text_end_game(25, const.COLOR['WHITE'], [const.WIDTH/2, const.HEIGHT/2])

        font = pg.font.SysFont('freesansbold.txt', 30)
        display_restart = font.render('Press R to Restart', True, const.COLOR['WHITE'], const.COLOR['BLACK'])
        display_rect = display_restart.get_rect()
        display_rect.center = (const.WIDTH/2, 450)
        self.__screen.blit(display_restart, display_rect)

        text_by = Text('By ElNickholas', self.__screen)
        text_by.render_text_screen_end_game(19, const.COLOR['WHITE'], [const.WIDTH / 2, 563])

        # linha horizontal de cima
        pg.draw.line(self.__screen, const.COLOR['WHITE'], [284, 288-20], [484, 288-20], 3)

        # linha horizontal de baixo
        pg.draw.line(self.__screen, const.COLOR['WHITE'], [284, 288+20], [484, 288+20], 3)

        # linha vertical da esquerda
        pg.draw.line(self.__screen, const.COLOR['WHITE'], [284, 288+20], [284, 288-20], 3)

        # linha vertical da direita
        pg.draw.line(self.__screen, const.COLOR['WHITE'], [484, 288+20], [484, 288-20], 3)

        while self.__waiting_player:

            self.__timer.tick(const.FRAMERATE)

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.__waiting_player = False
                    self.__running = False

                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_r:
                        self.__waiting_player = False

            pg.display.flip()

        if self.running:
            self.__restart_game()

    def __restart_game(self):
        self.__selected = []
        self.__menu = None
        self.__list_buttons = []
        self.__load_buttons()
        self.__menu_game = None
        self.__waiting_player = True
        self.__playing = True
        self.__resert_sprites()
        self.view_screen_start()

    def __resert_sprites(self):
        for sprite in self.__allsprites:
            sprite.resert = True
        self.__allsprites.update()
        self.__allsprites = None
        self.__allsprites = pg.sprite.Group()