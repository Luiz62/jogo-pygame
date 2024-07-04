
# Tela, largura e altura
WIDTH = 768
HEIGHT = 576

# titulo do jogo
TITLE_GAME = 'The IntroBattle Project'

# fontes
FONT = ['verdana', 'firacode', 'arial', 'gabriola']

# FRAMERATE
FRAMERATE = 30

# cores
COLOR = {
    'RED': (255, 0, 0),
    'BLUE': (0, 0, 255),
    'VICTORY': (151, 113, 67),
    'VICTORY_BG': (46, 39, 21),
    'DEFEAT': (161, 100, 58),
    'DEFEAT_BG': (89, 40, 30),
    'BLACK': (0, 0, 0),
    'WHITE': (255, 255, 255),
    'YELLOW': (244, 233, 51),
    'WHITE_BUTTON': (248, 248, 248)
}

# diretorios
DIR_BACKGROUND = './background'
DIR_UI = './ui'
DIR_CHARACTER_IMG = './personagens/imagens'
DIR_MUSIC = './music'
DIR_SOUND = './sound'

# imagens background
DIR_IMG_MENU_BG = DIR_BACKGROUND + '/background_1538x1152.png'

# imagens ui
IMG_MENU = DIR_UI + '/introcomp_menu.png'
IMG_ARROW = DIR_UI + '/introcomp_arrow.png'
IMG_GAME_1 = DIR_UI + '/introcomp_menu_game_1.png'
IMG_GAME_2 = DIR_UI + '/introcomp_menu_game_2.png'
IMG_GAME_3 = DIR_UI + '/introcomp_menu_game_3.png'

# sounds
DIR_SOUND_NEXT_BUTTON = DIR_SOUND + '/next_button.wav'
DIR_SOUND_SELECTED = DIR_SOUND + '/selected.wav'

# names
CHAMPS_MENU = ['Paladin', 'Rogue', 'Wizard', 'Hunter', 'Priest']

# pos ui menus
POS_MENU = [[80, 150], [290, 150], [500, 150], [175, 370], [400, 370]]
POS_MENU_NAMES = [[175, 315], [385, 315], [595, 315], [270, 535], [495, 535]]
POS_MENU_CHAMPS = [[175, 235], [385, 235], [595, 235], [270, 455], [495, 455]]
POS_MENU_ARROW = [[-110, 75], [100, 75], [310, 75], [-15, 295], [208, 295]]

# pos champs in game
POS_CHAMPS_GAME = [[145, 165], [55, 240], [145, 310]]
POS_ENEMY_GAME = [[600, 155], [545, 285]]

# pos hp
POS_HP_NAME = [[480, 420], [480, 470], [480, 520]]
POS_HP_HUD = [[580, 420], [580, 470], [580, 520]]

# champs
IMG_PALADIN = DIR_CHARACTER_IMG + '/paladino.png'
IMG_ROGUE = DIR_CHARACTER_IMG + '/rogue.png'
IMG_WIZARD_LEFT = DIR_CHARACTER_IMG + '/wizardfinal_left.png'
IMG_WIZARD_RIGHT = DIR_CHARACTER_IMG + '/wizardfinal_right.png'
IMG_HUNTER = DIR_CHARACTER_IMG + '/hunter_sprite.png'
IMG_PRIEST_NOSHADOW = DIR_CHARACTER_IMG + '/priest_no_shadow.png'
IMG_PRIEST_SHADOW = DIR_CHARACTER_IMG + '/priest_shadow.png'
IMG_SKELETON_LEFT = DIR_CHARACTER_IMG + '/skeleton_sprite_left.png'

# enemy
IMG_NECROMANCER_LEFT = DIR_CHARACTER_IMG + '/necromancer_left.png'
IMG_NECROMANCER_RIGHT = DIR_CHARACTER_IMG + '/necromancer_right.png'

LIST_CHAMPS = [IMG_PALADIN, IMG_ROGUE, IMG_WIZARD_LEFT, IMG_HUNTER, IMG_PRIEST_NOSHADOW]

# text
TEXT_INTRO = ['IntroBattle!', 50, COLOR['WHITE'], (WIDTH / 2, 55)]

# buttons game
BUTTONS_GAME_NAME = ['ATTACK', 'DEFEND', 'INSIGHT', 'SKILL']
BUTTONS_GAME_FONT = FONT[2]
BUTTONS_GAME_SIZE = 20
BUTTONS_GAME_COLOR = COLOR['WHITE_BUTTON']
BUTTONS_GAME_OFFSET = [[70, 465], [240, 465], [70, 510], [240, 510]]

# layout menu
LAYOUT_DIM = (512, 512)

# text turn game
TEXT_TURN_FONT = FONT[2]
TEXT_TURN_SIZE = 20
TEXT_TURN_COLOR = COLOR['WHITE_BUTTON']
TEXT_TURN_OFFSET = [70, 425]

# seta game
IMG_ARROW_RIGHT = DIR_UI + '/introcomp_arrow_right.png'
ARROW_OFFSET = [[10, 411], [180, 411], [10, 457], [180, 457]]
ARROW_OFFSET_ATTACK = [[445, 90], [382, 220]]
ARROW_OFFSET_HEAL = [[-13, 105], [-100, 180], [-15, 245]]

# texto ação
TEXT_ACTION_FONT = FONT[2]
TEXT_ACTION_SIZE = 20
TEXT_ACTION_COLOR = COLOR['WHITE_BUTTON']
TEXT_ACTION_OFFSET = [70, 470]

# texto fim de jogo
TEXT_END_FONT = FONT[2]
TEXT_END_SIZE = 26
TEXT_END_COLOR = COLOR['WHITE_BUTTON']
TEXT_END_OFFSET = [210, 430]