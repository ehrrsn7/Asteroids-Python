# gamestate screen displays.py
# Elijah Harrison

# import
import arcade
import global_variables_directory as global_variables
import point_file, buttons_file

"""
Default Screen
"""
class Base_Screen:
    def __init__(self):
        self.button1 = buttons_file.Button()
        self.button2 = buttons_file.Quit_Button()

    game_controls_image_texture = arcade.load_texture(
        global_variables.GAME_CONTROLS_IMAGE_FILENAME)

    def check_mouse_hovering_over_button(self, x: int, y: int):
        if self.button1.check_mouse_position(x, y):
            self.button1.mouse_hover = True
        else: self.button1.mouse_hover = False

        if self.button2.check_mouse_position(x, y):
            self.button2.mouse_hover = True
        else: self.button2.mouse_hover = False

        return (self.button1.mouse_hover, self.button2.mouse_hover)

    def check_mouse_clicked(self, x: int, y: int):
        if self.button1.check_mouse_position(x, y):
            self.button1.mouse_click = True
        else: self.button1.mouse_click = False

        if self.button2.check_mouse_position(x, y):
            self.button2.mouse_click = True
        else: self.button2.mouse_click = False

        return (self.button1.mouse_click, self.button2.mouse_click)

    def draw_buttons(self):
        self.button1.draw()
        self.button2.draw()
    
    def draw_controls(self):
        arcade.draw_scaled_texture_rectangle(
            global_variables.SCREEN_CENTER_X + 225, 
            global_variables.SCREEN_CENTER_Y - 150, 
            self.game_controls_image_texture, 
            global_variables.DEFAULT_TEXTURE_SCALE / 2,
            global_variables.DEFAULT_TEXTURE_ANGLE,
            global_variables.DEFAULT_TEXTURE_ALPHA)


"""
Main Menu Screen
"""
class Main_Menu_Screen(Base_Screen):
    def __init__(self):
        super().__init__()
        self.button1 = buttons_file.Start_Button()

    asteroids_logo_image_texture = arcade.load_texture(
        global_variables.ASTEROIDS_LOGO_IMAGE_FILENAME)

    def draw(self):
        # draw buttons
        self.draw_buttons()

        # draw controls
        self.draw_controls()

        # draw title
        arcade.draw_scaled_texture_rectangle(
            global_variables.SCREEN_CENTER_X, 
            global_variables.SCREEN_CENTER_Y + 100, 
            self.asteroids_logo_image_texture, 
            global_variables.DEFAULT_TEXTURE_SCALE,
            global_variables.DEFAULT_TEXTURE_ANGLE,
            global_variables.DEFAULT_TEXTURE_ALPHA)

class Ship_Was_Hit_Screen(Base_Screen):
    def __init__(self):
        super().__init__()
        self.button1 = buttons_file.Continue_Button()

    ship_was_hit_msg_image_texture = arcade.load_texture(
        global_variables.SHIP_WAS_HIT_MSG_IMAGE_FILENAME)

    def draw(self):
        # draw buttons
        self.draw_buttons()

        # draw controls hints
        self.draw_controls()

        # draw ship was hit message
        arcade.draw_scaled_texture_rectangle(
            global_variables.SCREEN_CENTER_X, 
            global_variables.SCREEN_CENTER_Y + 20, 
            self.ship_was_hit_msg_image_texture, 
            global_variables.DEFAULT_TEXTURE_SCALE / 2,
            global_variables.DEFAULT_TEXTURE_ANGLE,
            global_variables.DEFAULT_TEXTURE_ALPHA)

class Game_Over_Screen(Base_Screen):
    def __init__(self):
        super().__init__()
        self.button1 = buttons_file.Restart_Button()

    game_over_msg_image_texture = arcade.load_texture(
        global_variables.GAME_OVER_MSG_IMAGE_FILENAME)

    def draw(self):
        # draw buttons
        self.draw_buttons()

        # draw game over message
        arcade.draw_scaled_texture_rectangle(
            global_variables.SCREEN_CENTER_X, 
            global_variables.SCREEN_CENTER_Y + 20, 
            self.game_over_msg_image_texture, 
            global_variables.DEFAULT_TEXTURE_SCALE / 2,
            global_variables.DEFAULT_TEXTURE_ANGLE,
            global_variables.DEFAULT_TEXTURE_ALPHA)


class Pause_Screen(Base_Screen):
    def __init__(self):
        super().__init__()
        self.button1 = buttons_file.Resume_Button()

    paused_image_texture = arcade.load_texture(
        global_variables.PAUSED_IMAGE_FILENAME)

    def draw(self):
        # draw buttons
        self.draw_buttons()

        # draw controls hints
        self.draw_controls()

        # draw 'paused' message
        arcade.draw_scaled_texture_rectangle(
            global_variables.SCREEN_CENTER_X, 
            global_variables.SCREEN_CENTER_Y + 20, 
            self.paused_image_texture,
            global_variables.DEFAULT_TEXTURE_SCALE / 2,
            global_variables.DEFAULT_TEXTURE_ANGLE,
            global_variables.DEFAULT_TEXTURE_ALPHA)


class New_Level_Screen(Base_Screen):
    def __init__(self):
        super().__init__()
        self.button1 = buttons_file.Continue_Button()
    
    new_level_screen_texture = arcade.load_texture(
        global_variables.LEVEL_COMPLETE_IMAGE_FILENAME)
    
    def draw(self):
        # draw buttons
        self.draw_buttons()

        # draw message
        arcade.draw_scaled_texture_rectangle(
            global_variables.SCREEN_CENTER_X,
            global_variables.SCREEN_CENTER_Y + 20,
            self.new_level_screen_texture,
            global_variables.DEFAULT_TEXTURE_SCALE / 2,
            global_variables.DEFAULT_TEXTURE_ANGLE,
            global_variables.DEFAULT_TEXTURE_ALPHA)


class Gamestate_Screens:
    def __init__(self):
        self.main_menu_screen = Main_Menu_Screen()
        self.pause_screen     = Pause_Screen()
        self.ship_was_hit_msg = Ship_Was_Hit_Screen()
        self.game_over_screen = Game_Over_Screen()
        self.new_level_screen = New_Level_Screen()

