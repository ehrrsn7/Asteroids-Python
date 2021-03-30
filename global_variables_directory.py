"""
File: global_variables_directory.py
Name: Elijah Harrison

These are Global constants to use throughout the game
"""

# import
import arcade, random, math

# screen variables
SCREEN_WIDTH                    = 800
SCREEN_HEIGHT                   = 600
SCREEN_MARGIN                   = 20
# x
SCREEN_MARGIN_X                 = SCREEN_MARGIN
SCREEN_CENTER_X                 = SCREEN_WIDTH / 2
SCREEN_LEFT_X                   = SCREEN_MARGIN_X
SCREEN_RIGHT_X                  = SCREEN_WIDTH - SCREEN_MARGIN_X
# y
SCREEN_MARGIN_Y                 = SCREEN_MARGIN
SCREEN_CENTER_Y                 = SCREEN_HEIGHT / 2
SCREEN_BOTTOM_Y                 = SCREEN_MARGIN_Y
SCREEN_TOP_Y                    = SCREEN_HEIGHT - SCREEN_MARGIN_Y
# arcade.color (tuple)
SCREEN_COLOR_LIGHT              = arcade.color.WHITE
SCREEN_COLOR_DARK               = arcade.color.BLACK

# default draw variables
DEFAULT_TEXTURE_ANGLE           = 0
DEFAULT_TEXTURE_SCALE           = 1
DEFAULT_TEXTURE_ALPHA           = 255

# on-screen text variables
TEXT_NORMAL_FONT_SIZE           = 12
TEXT_NORMAL_COLOR_LIGHT         = arcade.color.NAVY_BLUE
TEXT_NORMAL_COLOR_DARK          = arcade.color.WHITE

# score variables
SCORE_INIT                      = 0
SCORE_X                         = 10
SCORE_Y                         = SCREEN_TOP_Y

# level variables
LEVEL_COLOR_LIGHT               = arcade.color.NAVY_BLUE
LEVEL_COLOR_DARK                = arcade.color.WHITE
LEVEL_INIT                      = 1
LEVEL_X                         = SCREEN_WIDTH  - 65
LEVEL_Y                         = SCREEN_HEIGHT - 20
LEVEL_FONT_SIZE                 = 12

# ship variables
SHIP_X_INIT                     = SCREEN_CENTER_X
SHIP_Y_INIT                     = SCREEN_CENTER_Y
SHIP_RADIUS                     = 30
SHIP_ANGLE_ROTATE_AMOUNT        = 3
SHIP_THRUST_ACCELERATE_AMOUNT   = 0.25
SHIP_FIRING_RATE_DELAY          = 5
SHIP_MAX_VELOCITY               = 20
SHIP_ANGLE_INIT                 = 90
SHIP_IMAGE_FILENAME             = "resources/images/projectile images/playerShip1_orange.png"
SHIP_AIRHORN_IMAGE_FILENAME     = "resources/images/projectile images/air_horn.png"
SHIP_WITH_FLAMES_IMAGE_FILENAME = "resources/images/projectile images/playerShip1_orange_with_flames.png"
SHIP_TEXTURE_SCALE              = 0.8
SHIP_TEXTURE_ALPHA              = 255

# ship lives variables
SHIP_LIVES_INIT_AMOUNT          = 3
SHIP_LIVES_Y_POSITION           = SCREEN_TOP_Y - 20
SHIP_LIVES_X_POSITION_INIT      = 30
SHIP_LIVES_X_POSITION_SPACING   = 40
SHIP_LIVES_DRAWING_SCALE        = .325

# rifle variables
RIFLE_WIDTH                     = 100
RIFLE_HEIGHT                    = 20
RIFLE_X_INIT                    = 0
RIFLE_Y_INIT                    = 0
RIFLE_ANGLE_INIT                = 45
RIFLE_COLOR_LIGHT               = arcade.color.DARK_RED
RIFLE_COLOR_DARK                = arcade.color.LIGHT_CRIMSON

# bullet variables
BULLET_RADIUS                   = 3
BULLET_SPEED                    = 10
BULLET_TIMER                    = 40
BULLET_COLOR_LIGHT              = arcade.color.BLACK_OLIVE
BULLET_COLOR_DARK               = arcade.color.LIGHT_GRAY
BULLET_IMAGE_FILENAME           = "resources/images/projectile images/laser_bullet.png"
BULLET_FAST_IMAGE_FILENAME      = "resources/images/projectile images/laser_bullet_red.png"
BULLET_TEXTURE_SCALE            = 1
BULLET_TEXTURE_ALPHA            = 255

# rock variables
ROCK_INIT_AMOUNT                = 5
# default rock variables
ROCK_DEFAULT_RADIUS             = 15
ROCK_DEFAULT_SPEED              = 1.5
ROCK_DEFAULT_POINTS_AWARDED     = 20
ROCK_DEFAULT_TIMER_INIT         = 100
ROCK_DEFAULT_IMAGE_FILENAME     = "resources/images/projectile images/meteorGrey_big1.png"
ROCK_DEFAULT_SPIN               = 1
# big rock variables
ROCK_BIG_RADIUS                 = ROCK_DEFAULT_RADIUS
ROCK_BIG_SPEED                  = ROCK_DEFAULT_SPEED
ROCK_BIG_POINTS_AWARDED         = ROCK_DEFAULT_POINTS_AWARDED
ROCK_BIG_SPIN                   = ROCK_DEFAULT_SPIN
ROCK_BIG_IMAGE_FILENAME         = ROCK_DEFAULT_IMAGE_FILENAME
# medium rock variables
ROCK_MEDIUM_RADIUS              = 5
ROCK_MEDIUM_SPEED               = 2
ROCK_MEDIUM_POINTS_AWARDED      = 50
ROCK_MEDIUM_SPIN                = -2
ROCK_MEDIUM_IMAGE_FILENAME      = "resources/images/projectile images/meteorGrey_med1.png"
# small rock variables
ROCK_SMALL_RADIUS               = 2
ROCK_SMALL_SPEED                = 3
ROCK_SMALL_POINTS_AWARDED       = 100
ROCK_SMALL_SPIN                 = 5
ROCK_SMALL_IMAGE_FILENAME       = "resources/images/projectile images/meteorGrey_small1.png"
# greg
TROLL_RADIUS                    = ROCK_DEFAULT_RADIUS
TROLL_SPEED                     = ROCK_DEFAULT_SPEED
TROLL_POINTS_AWARDED            = ROCK_DEFAULT_POINTS_AWARDED
TROLL_SPIN                      = .5
TROLL_IMAGE_FILENAME            = "resources/images/projectile images/troll_face.png"

# saucer variables
SAUCER_POINTS_AWARDED           = 200
SAUCER_LARGE_POINTS_AWARDED     = 1000

# target variables
TARGET_DEFAULT_RADIUS           = 20
TARGET_DEFAULT_X_INIT           = 1
# default target
TARGET_STANDARD_POINTS          = 1
TARGET_STANDARD_COLOR_DARK      = arcade.color.BLIZZARD_BLUE
TARGET_STANDARD_COLOR_LIGHT     = arcade.color.CARROT_ORANGE
# strong target
TARGET_STRONG_POINTS            = 3
TARGET_STRONG_LIFE_INIT         = 3
TARGET_STRONG_LIFE_TEXT_SIZE    = 20
TARGET_STRONG_LIFE_TEXT_OFFSET  = -10
TARGET_STRONG_COLOR_DARK        = arcade.color.LIGHT_CORAL
TARGET_STRONG_COLOR_LIGHT       = arcade.color.BLIZZARD_BLUE
TARGET_STRONG_LIFE_COLOR_DARK   = arcade.color.BLACK
TARGET_STRONG_LIFE_COLOR_LIGHT  = arcade.color.DARK_GRAY
# safe target
TARGET_SAFE_POINTS              = -10
TARGET_SAFE_SIDE_LENGTH         = TARGET_DEFAULT_RADIUS * 2
TARGET_SAFE_TILT                = 0
TARGET_SAFE_COLOR_LIGHT         = arcade.color.BLACK
TARGET_SAFE_COLOR_DARK          = arcade.color.WHITE
# meme guy target
TARGET_MEME_GUY_IMAGE_SCALE     = 1 / 10
TARGET_MEME_GUY_IMAGE_ANGLE     = 0
TARGET_MEME_GUY_IMAGE_ALPHA     = 255

# ball variables (pong)
BALL_RADIUS                     = 10
BALL_X_INIT                     = 50
BALL_Y_INIT                     = random.randint(0, SCREEN_HEIGHT)
BALL_DX_INIT                    = random.randint(1, 5)
BALL_DY_INIT                    = random.randint(1, 5)
BALL_COLOR_DARK                 = arcade.color.WHITE
BALL_COLOR_LIGHT                = arcade.color.BLACK

# paddle variables
PADDLE_WIDTH                    = 10
PADDLE_HEIGHT                   = 50
PADDLE_X_INIT                   = SCREEN_WIDTH - 20
PADDLE_Y_INIT                   = 150
PADDLE_Y_MIN                    = 30
PADDLE_Y_MAX                    = SCREEN_HEIGHT - 30
PADDLE_COLOR_DARK               = arcade.color.WHITE
PADDLE_COLOR_LIGHT              = arcade.color.BLACK

# game state
RESUME                          = 0
PAUSE                           = 1
MAIN_MENU                       = 2
NEW_LEVEL                       = 4
GAME_OVER                       = 5
SHIP_WAS_HIT                    = 6
STATE_INIT                      = MAIN_MENU
GAMESTATE_POSITION_X            = SCREEN_CENTER_X - 80
GAMESTATE_POSITION_Y            = SCREEN_TOP_Y

# game state draw variables
ASTEROIDS_LOGO_IMAGE_FILENAME   = "resources/images/gamestate screen images/asteroids_game_logo.png"
GAME_WELCOME_MSG_IMAGE_FILENAME = "resources/images/gamestate screen images/asteroids_game_welcome_msg.png"
GAME_CONTROLS_IMAGE_FILENAME    = "resources/images/gamestate screen images/asteroids_controls.png"
GAME_OVER_MSG_IMAGE_FILENAME    = "resources/images/gamestate screen images/game_over_msg.png"
LEVEL_COMPLETE_IMAGE_FILENAME   = "resources/images/gamestate screen images/level_complete_msg.png"
PAUSE_HINT_IMAGE_FILENAME       = "resources/images/gamestate screen images/p_to_pause_game.png"
PAUSED_IMAGE_FILENAME           = "resources/images/gamestate screen images/paused_msg.png"
SHIP_WAS_HIT_MSG_IMAGE_FILENAME = "resources/images/gamestate screen images/ship_was_hit_msg.png"

# button variables
BUTTON_DEFAULT_SCALE            = 1 / 4
BUTTON_X                        = SCREEN_CENTER_X - 200
BUTTON_Y_TOP                    = SCREEN_CENTER_Y - 100
BUTTON_Y_BOTTOM                 = SCREEN_CENTER_Y - 200
BUTTON_DEFAULT_WIDTH            = 50
BUTTON_DEFAULT_HEIGHT           = 25
BUTTON_DEFAULT_IMAGE_FILENAME   = "resources/images/buttons images/default_button.png"
BUTTON_DEFAULT_MH_IMAGE_FILENAME = "resources/images/buttons images/default_button_mouse_hover_mouse_click.png"
# start button
BUTTON_START_IMAGE_FILENAME     = "resources/images/buttons images/start_button.png"
BUTTON_START_MH_IMAGE_FILENAME  = "resources/images/buttons images/start_button_mouse_hover_mouse_click.png"
# continue button
BUTTON_CONT_IMAGE_FILENAME      = "resources/images/buttons images/continue_button.png"
BUTTON_CONT_MH_IMAGE_FILENAME   = "resources/images/buttons images/continue_button_mouse_hover_mouse_click.png"
# resume button
BUTTON_RESUME_IMAGE_FILENAME    = "resources/images/buttons images/resume_button.png"
BUTTON_RESUME_MH_IMAGE_FILENAME = "resources/images/buttons images/resume_button_mouse_hover_mouse_click.png"
# quit button
BUTTON_QUIT_IMAGE_FILENAME      = "resources/images/buttons images/quit_button.png"
BUTTON_QUIT_MH_IMAGE_FILENAME   = "resources/images/buttons images/quit_button_mouse_hover_mouse_click.png"
# restart button
BUTTON_RSRT_IMAGE_FILENAME      = "resources/images/buttons images/restart_button.png"
BUTTON_RSRT_MH_IMAGE_FILENAME   = "resources/images/buttons images/restart_button_mouse_hover_mouse_click.png"

# game sounds
SOUND_EXPLOSION_LARGE           = "resources/sounds/bangLarge.wav"
SOUND_EXPLOSION_MEDIUM          = "resources/sounds/bangMedium.wav"
SOUND_EXPLOSION_SMALL           = "resources/sounds/bangSmall.wav"
SOUND_BEAT_1                    = "resources/sounds/beat1.wav"
SOUND_BEAT_2                    = "resources/sounds/beat2.wav"
SOUND_EXTRA_SHIP                = "resources/sounds/extraShip.wav"
SOUND_FIRE                      = "resources/sounds/fire.wav"
SOUND_AIRHORN                   = "resources/sounds/airHorn.mp3"
SOUND_SAUCER_BIG                = "resources/sounds/saucerBig.wav"
SOUND_SAUCER_SMAL               = "resources/sounds/saucerSmall.wav"
SOUND_THRUST                    = "resources/sounds/thrust.wav"
# sound beat variables
SOUND_BEAT_DELAY_INIT           = 250
MINIMUM_BEAT_DELAY              = 25
BEAT_DELAY_OFFSET_INCREMENT     = 25


# high scores variable
HIGH_SCORES_FILENAME            = "resources/texts/high_scores.txt"


# other variables
MOVE_AMOUNT                     = 5
DELAY_INIT                      = 5
SCORE_HIT                       = 1
SCORE_MISS                      = 5
ALIVE                           = True
DEAD                            = False
DEBUG                           = False
DARK_MODE_INIT                  = True
PI_OVER_2                       = math.radians(90)

