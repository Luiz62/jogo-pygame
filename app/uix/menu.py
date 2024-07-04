from typing import List
import pygame as pg
from pygame import transform
from app.uix.button import ButtonScreenStart as Bss
from app.uix.button import ButtonScreenGame as Bsg
from app.uix.text import Text
from app.uix.layout_menu import LayoutMenu
from operator import itemgetter
from app.constants import const
from random import choice

class Menu:
    """
    screen : Tela do jogo
    [button] : Lista de botões
    current  : Botão atual
    no_selected : Botões não selecionados
    """
    def __init__(self, screen, buttons: List[Bss], sounds):
        self.__screen = screen
        self.__buttons = buttons
        self.__sounds = sounds
        self.__current = 1
        self.current.toggle_highlight()
        self.no_selected = [0, 1, 2, 3, 4]

    @property
    def current(self) -> Bss:
        return self.__buttons[self.__current]

    def __render_arrow(self):
        img = transform.scale(pg.image.load(const.IMG_ARROW), (128 * 3, 128 * 3))
        rect = const.POS_MENU_ARROW[self.__current]
        self.__screen.blit(img, rect)

    def next(self, key, play_sound=False):
        if play_sound:
            self.__sounds['sound_next'].play()
        steps = {
            'right': 1,
            'left': -1,
            }
        self.current.toggle_highlight()
        self.__current += steps[key]

        if self.__current not in self.no_selected:

            for i in range(2):
                self.__current += steps[key]
                if self.__current in self.no_selected:
                    break

        if self.__current > max(self.no_selected):
            self.__current = min(self.no_selected)

        if self.__current < min(self.no_selected):
            self.__current = max(self.no_selected)

        self.current.toggle_highlight()

    def get_current(self):
        if self.__current in self.no_selected:
            self.no_selected.remove(self.__current)
        return self.__current

    def render(self, images):
        self.__render_arrow()
        for button in self.__buttons:
            button.render(self.__screen, images)

class MenuGame:
    def __init__(self, screen, buttons: List[Bsg], imgs, img_bg, sounds, selected, sprites):
        self.__screen = screen
        self.__buttons = buttons
        self.__imgs = imgs
        self.__img_bg = img_bg
        self.__sounds = sounds
        self.__selected = selected
        self.__sprites = sprites
        self.__current = 0
        self.__current_2 = 0
        self.__current_3 = 0
        self.__list_characters = ['character_1', 'character_2', 'character_3', 'enemy_1', 'enemy_2']
        self.__dict_sprites = {}
        self.__list_order_turn = []
        self.__load_sprites()
        self.finish = False
        self.close_game = False
        self.__turn = 0
        self.__list_order_turn = sorted(self.__list_order_turn, key=itemgetter(1), reverse=True)
        self.__turn_name = self.__list_order_turn[0][0]
        self.__round = 0
        # verifica se o jogador quer desfazer a escolha
        self.__press_x = False

    # carrega as sprites
    def __load_sprites(self):
        for key, sprite in enumerate(self.__sprites):
            self.__dict_sprites[self.__list_characters[key]] = sprite

        for key, sprite in enumerate(self.__sprites):
            self.__list_order_turn.append([sprite.name, sprite.speed])

    def __next_resert(self):
        self.__layout_left()

        # texto mostrando de quem é a vez
        self.__draw_text_turn()

        # desenha os botões de ações disponíveis
        self.__draw_buttons()

    # muda a seta de posição
    def next(self, key, play_sound=False):
        if play_sound:
            self.__sounds['sound_next'].play()
        steps = {
            'right': 1,
            'left': -1,
            'up': -2,
            'down': 2
            }
        self.__next_resert()
        self.__current += steps[key]
        self.__current = abs(self.__current % len(self.__buttons))
        self.__draw_arrow()

    # muda a seta de posição
    def __next_attack(self, key, play_sound=False):
        if play_sound:
            self.__sounds['sound_next'].play()
        steps = {
            'right': 1,
            'left': -1,
            'up': 1,
            'down': -1
        }
        self.__current_2 += steps[key]
        self.__current_2 = abs(self.__current_2 % 2)

    # muda a seta de posição
    def __next__heal(self, key, play_sound=False):
        if play_sound:
            self.__sounds['sound_next'].play()
        steps = {
            'left': 1,
            'up': -1,
            'down': 1
        }
        self.__current_3 += steps[key]
        self.__current_3 = abs(self.__current_3 % 3)

    # menu da esquerda
    def __layout_left(self):

        img_1 = transform.scale(self.__imgs['menu_1'], (128 * 4, 128 * 4))
        rect_1 = img_1.get_rect()
        rect_1.x, rect_1.y = 0, 280
        self.__screen.blit(img_1, rect_1)

    # menu do hp do personagens
    def __layout_right(self):
        lm = LayoutMenu(self.__imgs['menu_2'], (376, 240), self.__screen)
        lm.render_layout()

    # menu da mensagem de fim de jogo
    def __layout_center(self):
        lm = LayoutMenu(self.__imgs['menu_3'], (410, 533), self.__screen)
        lm.render_layout_center()

    # mostra o menu com a barra de vida do jogadores aliados
    def __render_hps(self):
        list_info = []

        for pos, sprite in enumerate(self.__sprites):
            list_info.append({
                'name': sprite.name,
                'hp': sprite.hp,
                'hp_root': sprite.hp_root
            })
        for pos, item in enumerate(self.__selected):
            text_hp = list_info[pos]['name']
            new_text = Text(text_hp, self.__screen)
            new_text.render_text_hp(const.POS_HP_NAME[pos][0], const.POS_HP_NAME[pos][1])

            info_hp = '{:3.0f}  /  {:3.0f}'.format(list_info[pos]['hp'], list_info[pos]['hp_root'])
            new_text = Text(info_hp, self.__screen)
            new_text.render_text_hp(const.POS_HP_HUD[pos][0], const.POS_HP_HUD[pos][1])

    # mostra de quem é a vez
    def __render_turn(self, name):
        new_text = Text(name, self.__screen)
        new_text.render_text_turn()

    # seta para escolher qual ação executar
    def __render_arrow(self):
        img = transform.scale(self.__imgs['arrow_right'], (128 * 2, 128 * 2))
        img_rect = img.get_rect()
        img_rect.topleft = const.ARROW_OFFSET[self.__current]
        self.__screen.blit(img, img_rect)

    # seta para escolher qual inimigo atacar
    def __render_arrow_attack(self):
        img = transform.scale(self.__imgs['arrow_down'], (128 * 2, 128 * 2))
        img_rect = img.get_rect()
        self.__to_check_enemy_in_game()
        img_rect.topleft = const.ARROW_OFFSET_ATTACK[self.__current_2]
        self.__screen.blit(img, img_rect)

    def __to_check_enemy_in_game(self):
        if self.__current_2 == 0:
            if not self.__dict_sprites['enemy_1'].in_game:
                self.__current_2 = 1
        elif self.__current_2 == 1:
            if not self.__dict_sprites['enemy_2'].in_game:
                self.__current_2 = 0

    # seta para escolher quem curar
    def __render_arrow_heal(self):
        img = transform.scale(self.__imgs['arrow_down'], (128 * 2, 128 * 2))
        img_rect = img.get_rect()
        self.__to_check_ally_in_game()
        img_rect.topleft = const.ARROW_OFFSET_HEAL[self.__current_3]
        self.__screen.blit(img, img_rect)

    # verifica se o aliado onde a seta vai aparecer está vivo
    def __to_check_ally_in_game(self):
        if self.__current_2 == 0:
            if not self.__dict_sprites['character_1'].in_game:
                self.__current_2 = 1
        elif self.__current_3 == 1:
            if not self.__dict_sprites['character_2'].in_game:
                self.__current_3 = 2
        elif self.__current_3 == 3:
            if not self.__dict_sprites['character_3'].in_game:
                self.__current_3 = 0

    def __next_turn_resert(self):

        # resertando a posição da seta
        self.__current = 0
        self.__current_2 = 0

        # atualiza todas as sprites
        self.__update_sprites()

        # resertar tela
        self.__resert_screen()

        # desenha o menu com a barra de vida
        self.__draw_menu_game()

        # desenhar sprites
        self.__draw_sprites()

        # verificar a vitória
        self.__to_check_victory()

    # verifica a vitória
    def __to_check_victory(self):
        not_in_game_ally, not_in_game_enemy = 0, 0

        for i in range(0, 5):

            sprite = self.__dict_sprites[self.__list_characters[i]]
            if not sprite.in_game:
                if i < 3:
                    not_in_game_ally += 1
                if i > 2:
                    not_in_game_enemy += 1

        # verifica se você derrotou os inimigos
        if not_in_game_enemy == 2:
            self.__victory()

        # verifica se você foi derrotado
        elif not_in_game_ally == 3:
            self.__defeat()

    # limpa a tela no final do jogo
    def __resert_screen_end_game(self):
        self.__resert_screen()

        self.__draw_sprites()

        self.__layout_center()

    def __victory(self):
        self.__text_end_game('YOU WON THE BATTLE! :)')

    def __defeat(self):
        self.__text_end_game('YOU LOST THE BATTLE! :/')

    def __text_end_game(self, text_in):
        self.__resert_screen_end_game()

        text = Text(text_in, self.__screen)
        text.render_text_end_game(const.TEXT_END_SIZE, const.TEXT_END_COLOR, const.TEXT_END_OFFSET)
        self.__update_display()

        pg.time.delay(2000)

        self.finish = True

    def __next_turn_values(self):
        self.__turn += 1

        if self.__turn > len(self.__list_order_turn) - 1:
            self.__turn = 0

        self.__turn_name = self.__list_order_turn[self.__turn][0]

    # vai para proxima rodada
    def __next_turn(self):

        self.__next_turn_resert()

        if not self.finish:
            self.__round += 1

            self.__next_turn_values()

            waiting = True
            while waiting:
                value = self.__character_in_game()

                if not value:
                    self.__next_turn_values()
                else:
                    waiting = False

            if self.__turn_name == 'SKELETON' or self.__turn_name == 'NECROMANCER':
                self.__action_enemy()
            else:
                self.render()
                self.__draw_arrow()

    # adiciona defesa ao personagem no começo da rodada e no final remove
    def __next_turn_defend(self, sprite):
        sprite.receive_defense()
        self.__next_turn_resert()

        if not self.finish:
            self.__round += 1

            self.__next_turn_values()

            waiting = True
            while waiting:
                if not self.__character_in_game():
                    self.__next_turn_values()
                else:
                    waiting = False

            if self.__turn_name == 'SKELETON' or self.__turn_name == 'NECROMANCER':
                self.__action_enemy()
            else:
                self.render()
                self.__draw_arrow()

        sprite.back_defense()

    def __character_in_game(self):
        if self.__sprite_turn().in_game:
            return True
        else:
            return False

    def __text_select_your_target(self):
        text = Text('SELECT YOUR TARGET!', self.__screen)
        text.render_text_target(const.TEXT_ACTION_SIZE, const.TEXT_ACTION_COLOR, [70, 470])
        self.__update_display()

    def __show_action(self, text):
        text.render_text_action(const.TEXT_ACTION_SIZE, const.TEXT_ACTION_COLOR, const.TEXT_ACTION_OFFSET)
        self.__draw_text_turn()
        self.__update_display()

    def __render_action(self, x, y, name):
        text = Text(x.name + name + y.name + '...', self.__screen)
        self.__show_action(text)

    def __render_action_2(self, x, action):
        text = Text(x.name + action + '...', self.__screen)
        self.__show_action(text)

    def __render_action_3(self, action):
        text = Text(action + '...', self.__screen)
        self.__show_action(text)

    def __render_statistics_enemy(self, enemy, s1, s2, s3, s4):
        text = Text(enemy.name, self.__screen)
        text.render_text_enemy_statistics_name(s1, s2, s3, s4)
        self.__update_display()

    def __render_defeated(self, name):
        text = Text(name, self.__screen)
        text.render_text_defeated(const.TEXT_TURN_SIZE, const.TEXT_TURN_COLOR, const.TEXT_TURN_OFFSET)

        text = Text('WAS DEFEATED!', self.__screen)
        text.render_text_defeated(const.TEXT_ACTION_SIZE, const.TEXT_ACTION_COLOR, const.TEXT_ACTION_OFFSET)
        self.__update_display()

    def __action_enemy_resert(self):
        # resertar tela
        self.__resert_screen()

        # desenhar sprites
        self.__draw_sprites()

        # desenha o menu com a barra de vida
        self.__draw_menu_game()

    def __action_enemy(self):
        self.__action_enemy_resert()

        # verificando seu o nome da rodada é de um dos inimigos
        if self.__turn_name == 'SKELETON' or self.__turn_name == 'NECROMANCER':
            # sorteando a opção que o inimigo vai escolher
            op_action = choice([0, 1, 2])

            enemy = self.__sprite_turn()

            # opção de atacar
            if op_action == 0:

                # escolhendo quem vai ser atacado
                op_enemy = choice([0, 1, 2])

                # nome da sprite que receberá o ataque
                op_enemy = self.__list_characters[op_enemy]

                # sprite que receberá o ataque
                character = self.__dict_sprites[op_enemy]

                # dano que a sprite receberar
                damage = enemy.attacks(character.defense)

                # verificando se a sprite não será derrotada após o dano
                if character.hp - damage <= 0:
                    # texto que a sprite foi derrotada
                    self.__was_defeated(character.name)

                # atualizando o hp da sprite que recebeu o ataque
                character.receive_attack(damage)

                # texto mostrando a ação
                self.__render_action(enemy, character, ' ATTACKS ')

            # opção defender
            elif op_action == 1:
                # texto mostrando a ação
                self.__render_action_2(enemy, ' SELECTED DEFEND')

                self.__next_turn_defend(enemy)

            # opção de skill
            elif op_action == 2:
                # O Necromancer adiciona vida a ele e seu aliado
                if enemy.name == 'NECROMANCER':
                    enemy.skill(self.__dict_sprites)
                    self.__render_action_3('HEALED HIM AND HIS ALLY')

                # Se sua vida estiver abaixo de 13% da vida total, seu poder de ataque é triplicado
                # Do contrário são adicionados mais quatro pontos ao seu ataque
                elif enemy.name == 'SKELETON':
                    op = enemy.skill()
                    if op == 0:
                        self.__render_action_2(enemy, ' ATTACK INCREASES 3X')
                    elif op == 1:
                        self.__render_action_2(enemy, ' ATTACK INCREASES 4')

        # delay de 2.5 segundos
        pg.time.delay(2500)

        # indo para próxima rodada
        self.__next_turn()

    # exibe texto mostrando o nome da sprite que foi derrotada
    def __was_defeated(self, name):
        self.__layout_left()
        self.__render_defeated(name)
        self.__update_display()
        pg.time.delay(1500)

    def __screen_resert_all(self):
        # resertar tela
        self.__resert_screen()

        # desenha o menu com a barra de vida
        self.__draw_menu_game()

        # desenhar sprites
        self.__draw_sprites()

    def __attack(self):
        self.__screen_resert_all()

        # texto mostrando de quem é a vez
        self.__draw_text_turn()

        # texto falando para escolher um dos alvos
        self.__text_select_your_target()

        timer, framerate = pg.time.Clock(), const.FRAMERATE

        waiting_player = True
        self.__press_x = False

        while waiting_player:
            timer.tick(framerate)

            self.__draw_arrow_attack()

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    waiting_player = False
                    self.finish = True

                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_a or event.key == pg.K_LEFT:
                        self.__next_attack('left', True)

                    elif event.key == pg.K_d or event.key == pg.K_RIGHT:
                        self.__next_attack('right', True)

                    elif event.key == pg.K_w or event.key == pg.K_UP:
                        self.__next_attack('up', True)

                    elif event.key == pg.K_s or event.key == pg.K_DOWN:
                        self.__next_attack('down', True)

                    elif event.key == pg.K_x:
                        self.__sounds['sound_selected'].play()
                        waiting_player = False
                        self.__press_x = True

                    elif event.key == pg.K_z or event.key == pg.K_SPACE:
                        self.__sounds['sound_selected'].play()
                        waiting_player = False

                    self.__screen_resert_all()

                    # texto mostrando de quem é a vez
                    self.__draw_text_turn()
                    if waiting_player:
                        self.__text_select_your_target()

            self.__update_display()
        if not self.__press_x:
            # personagem do jogador
            character = None

            # personagem inimigo
            enemy = None

            if self.__current_2 == 0:
                character = self.__sprite_turn()
                enemy = self.__dict_sprites['enemy_1']

            elif self.__current_2 == 1:
                character = self.__sprite_turn()
                enemy = self.__dict_sprites['enemy_2']

            damage = character.attacks(enemy.defense)

            enemy.receive_attack(damage)

            self.__screen_resert_all()

            self.__render_action(character, enemy, ' ATTACKS ')

            # sleep para conseguir ler o texto de ataque
            pg.time.delay(1500)

            if enemy.hp - damage <= 0:
                self.__was_defeated(enemy.name)

            enemy.receive_attack(damage)

            self.__next_turn()
        else:
            self.render()

    def __defend_resert(self):
        self.__layout_left()

    def __defend(self):
        self.__defend_resert()

        character = self.__sprite_turn()

        self.__render_action_2(character, ' SELECTED DEFEND')
        pg.time.delay(1500)
        self.__next_turn_defend(character)

    def __insight_resert(self):
        self.__layout_left()

    def __insight(self):
        self.__screen_resert_all()

        # texto mostrando de quem é a vez
        self.__draw_text_turn()

        # texto falando para escolher um dos alvos
        self.__text_select_your_target()

        timer, framerate = pg.time.Clock(), const.FRAMERATE

        waiting_player = True
        self.__press_x = False

        while waiting_player:
            timer.tick(framerate)

            self.__draw_arrow_attack()

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    waiting_player = False
                    self.finish = True

                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_a or event.key == pg.K_LEFT:
                        self.__next_attack('left', True)

                    elif event.key == pg.K_d or event.key == pg.K_RIGHT:
                        self.__next_attack('right', True)

                    elif event.key == pg.K_w or event.key == pg.K_UP:
                        self.__next_attack('up', True)

                    elif event.key == pg.K_s or event.key == pg.K_DOWN:
                        self.__next_attack('down', True)

                    elif event.key == pg.K_x:
                        self.__sounds['sound_selected'].play()
                        waiting_player = False
                        self.__press_x = True

                    elif event.key == pg.K_z or event.key == pg.K_SPACE:
                        self.__sounds['sound_selected'].play()
                        waiting_player = False

                    self.__screen_resert_all()

                    if waiting_player:
                        # texto mostrando de quem é a vez
                        self.__draw_text_turn()
                        self.__text_select_your_target()

            self.__update_display()
        if not self.__press_x:
            # personagem do jogador
            character = None

            # personagem inimigo
            enemy = None

            if self.__current_2 == 0:
                character = self.__sprite_turn()
                enemy = self.__dict_sprites['enemy_1']

            elif self.__current_2 == 1:
                character = self.__sprite_turn()
                enemy = self.__dict_sprites['enemy_2']

            # verificar o dano que o inimigo vai causar em você
            damage = character.attacks(enemy.defense)

            attack, defend, hp = enemy.insight()

            self.__render_statistics_enemy(enemy, attack, defend, hp, damage)

            # sleep para conseguir ler o texto de ataque
            pg.time.delay(4000)

            self.__next_turn()
        else:
            self.render()

    def __skill_resert(self):
        self.__layout_left()

    def __skill(self):
        self.__skill_resert()

        character, enemy_1, enemy_2 = None, None, None
        for sprite in self.__sprites:
            if sprite.name == self.__turn_name:
                character = sprite

        # O mago usa uma magia que causa dano a todos os inimigos
        if character.name == 'WIZARD':
            character.skill(self.__dict_sprites)
            self.__render_action_2(character, ' ATTACKS ALL')

        # O guerreiro protege seus aliados, aumentando a defesa deles
        elif character.name == 'PALADIN':
            character.skill(self.__dict_sprites)
            self.__render_action_2(character, ' ALLY RECEIVE DEFENSE')

        # O clérigo cura ele ou um aliado;
        elif character.name == 'PRIEST':
            self.__heal()

        # O Rogue pode aumenta o seu poder de ataque
        elif character.name == 'ROGUE':
            character.skill()
            self.__render_action_2(character, ' INCREASES YOUR ATTACK')

        # O Hunter usa seu arco prefurante, diminuindo a defesa dos inimigos
        elif character.name == 'HUNTER':
            character.skill(self.__dict_sprites)
            self.__render_action_2(character, ' ENEMY DEFENSE REDUCE')

        if not self.__press_x:
            pg.time.delay(1500)
            self.__next_turn()

    def __heal(self):
        self.__screen_resert_all()

        self.__draw_text_turn()

        self.__text_select_your_target()

        timer, framerate = pg.time.Clock(), const.FRAMERATE

        waiting_player = True
        self.__press_x = False

        self.__draw_arrow_heal()

        while waiting_player:
            timer.tick(framerate)

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    waiting_player = False
                    self.finish = True
                    self.close_game = True

                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_a or event.key == pg.K_LEFT:
                        self.__next__heal('left', True)

                    elif event.key == pg.K_w or event.key == pg.K_UP:
                        self.__next__heal('up', True)

                    elif event.key == pg.K_s or event.key == pg.K_DOWN:
                        self.__next__heal('down', True)

                    elif event.key == pg.K_z or event.key == pg.K_SPACE:
                        self.__sounds['sound_selected'].play()
                        waiting_player = False

                    elif event.key == pg.K_x:
                        self.__sounds['sound_selected'].play()
                        waiting_player = False
                        self.__press_x = True

                    if not self.close_game:
                        self.__screen_resert_all()

                        # desenhando seta
                        self.__draw_arrow_heal()

                        # texto mostrando de quem é a vez
                        self.__draw_text_turn()

                        if waiting_player:
                            self.__text_select_your_target()

            self.__update_display()
        if not self.__press_x:
            if not self.close_game:
                character, character_ally = None, None

                for sprite in self.__sprites:
                    if sprite.name == 'PRIEST':
                        character = sprite

                if self.__current_3 == 0:
                   character_ally = self.__dict_sprites['character_1']

                elif self.__current_3 == 1:
                    character_ally = self.__dict_sprites['character_2']

                elif self.__current_3 == 2:
                    character_ally = self.__dict_sprites['character_3']

                if character_ally is not None:
                    character.skill(character_ally)
                    self.__screen_resert_all()
                    self.__render_action(character, character_ally, ' HEALED ')
                    pg.time.delay(1500)

                self.__next_turn()

        else:
            self.__resert_screen()
            self.__draw_sprites()
            self.render()

    # reserta o layout da esquerda
    def __select_action_resert(self):
        self.__layout_left()

    # personagem escolha
    def select_action(self):
        self.__select_action_resert()

        # função de ataque
        if self.__buttons[self.__current].text == 'ATTACK':
            self.__attack()

        # função de defesa
        elif self.__buttons[self.__current].text == 'DEFEND':
            self.__defend()

        # função de análise
        elif self.__buttons[self.__current].text == 'INSIGHT':
            self.__insight()

        # função de habilidade
        elif self.__buttons[self.__current].text == 'SKILL':
            self.__skill()

    # texto mostrando de quem é a vez
    def __draw_text_turn(self):
        self.__render_turn(self.__turn_name)

    # desenha botões
    def __draw_buttons(self):
        for button in self.__buttons:
            button.render(self.__screen)

    # desenha a seta
    def __draw_arrow(self):
        self.__render_arrow()

    # desenha a seta para escolher o alvo
    def __draw_arrow_attack(self):
        self.__render_arrow_attack()

    # desenha a seta para escolher qual aliado curar
    def __draw_arrow_heal(self):
        self.__render_arrow_heal()

    # desenha o menu com a barra de vida
    def __draw_menu_game(self):
        self.__layout_left()
        self.__layout_right()
        self.__render_hps()

    # desenhar sprites
    def __draw_sprites(self):
        self.__sprites.draw(self.__screen)

    # atualiza todas as sprites
    def __update_sprites(self):
        self.__sprites.update()

    # retorna a sprite da rodada atual
    def __sprite_turn(self):
        for sprite in self.__sprites:
            if sprite.name == self.__turn_name:
                return sprite

    @staticmethod
    def __update_display():
        pg.display.flip()

    # resertar tela
    def __resert_screen(self):
        # tela com cor preta
        self.__screen.fill(const.COLOR['BLACK'])

        # adicionando um fundo a tela
        self.__screen.blit(self.__img_bg, (0, 0))

    def render(self):

        # desenha o menu com a barra de vida
        self.__draw_menu_game()

        # texto mostrando de quem é a vez
        self.__draw_text_turn()

        # verifica se o round é do computador
        if self.__turn_name == 'SKELETON' or self.__turn_name == 'NECROMANCER':
            self.__action_enemy()

        # se o round for do jogador
        else:
            # desenha os botões de ações disponíveis
            self.__draw_buttons()

            # coloca a seta na posição inicial
            self.__current = 0

            # desenha a seta para escolher uma das ações
            self.__draw_arrow()
