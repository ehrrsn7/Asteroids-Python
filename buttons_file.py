"""
File: buttons.py
Name: Elijah Harrison
"""

# import
import arcade
import point_file
import global_variables_directory as global_variables


class Button:
    def __init__(self):
        self.name           = "Default button"
        self.texture        = arcade.load_texture(global_variables.BUTTON_DEFAULT_IMAGE_FILENAME)
        self.mh_texture     = arcade.load_texture(global_variables.BUTTON_DEFAULT_MH_IMAGE_FILENAME)
        self.center         = point_file.Point()
        self.mouse_hover    = False
        self.mouse_click    = False
        self.display        = False

        self.center.x               = global_variables.SCREEN_RIGHT_X - 75
        self.half_width             = global_variables.BUTTON_DEFAULT_WIDTH
        self.half_height            = global_variables.BUTTON_DEFAULT_HEIGHT

    def draw(self):
        if self.display:
            if not self.mouse_hover or not self.mouse_click:
                arcade.draw_scaled_texture_rectangle(
                    self.center.x,
                    self.center.y,
                    self.texture,
                    global_variables.BUTTON_DEFAULT_SCALE * 1.5,
                    global_variables.DEFAULT_TEXTURE_ANGLE,
                    global_variables.DEFAULT_TEXTURE_ALPHA)
            else:
                arcade.draw_scaled_texture_rectangle(
                    self.center.x,
                    self.center.y,
                    self.mh_texture,
                    global_variables.BUTTON_DEFAULT_SCALE * 1.5,
                    global_variables.DEFAULT_TEXTURE_ANGLE,
                    global_variables.DEFAULT_TEXTURE_ALPHA)

    def check_mouse_position(self, x, y):
        if (x < self.button_position_right and x > self.button_position_left and
            x < self.button_position_top   and x > self.button_position_bottom):
            if global_variables.DEBUG:
                print(f">>> Mouse is on {self.name}")
            return True
        else:
            if global_variables.DEBUG:
                print(f"    Mouse is not on {self.name}")
            return False

    def set_button_position_limits(self):
        self.button_position_right  = self.center.x + self.half_width
        self.button_position_left   = self.center.x - self.half_width
        self.button_position_top    = self.center.y + self.half_height
        self.button_position_bottom = self.center.y - self.half_height


class Start_Button(Button):
    def __init__(self):
        super().__init__()
        self.name       = "Start button"
        self.center.y   = 200
        self.texture    = arcade.load_texture(global_variables.BUTTON_START_IMAGE_FILENAME)
        self.mh_texture = arcade.load_texture(global_variables.BUTTON_START_MH_IMAGE_FILENAME)
        self.set_button_position_limits()

class Continue_Button(Button):
    def __init__(self):
        super().__init__()
        self.name       = "Continue button"
        self.center.y   = 200
        self.texture    = arcade.load_texture(global_variables.BUTTON_CONT_IMAGE_FILENAME)
        self.mh_texture = arcade.load_texture(global_variables.BUTTON_CONT_MH_IMAGE_FILENAME)
        self.set_button_position_limits()


class Restart_Button(Button):
    def __init__(self):
        super().__init__()
        self.name       = "Restart button"
        self.center.y   = 200
        self.texture    = arcade.load_texture(global_variables.BUTTON_RSRT_IMAGE_FILENAME)
        self.mh_texture = arcade.load_texture(global_variables.BUTTON_RSRT_MH_IMAGE_FILENAME)
        self.set_button_position_limits()

class Resume_Button(Button):
    def __init__(self):
        super().__init__()
        self.name       = "Resume button"
        self.center.y   = 200
        self.texture    = arcade.load_texture(global_variables.BUTTON_RESUME_IMAGE_FILENAME)
        self.mh_texture = arcade.load_texture(global_variables.BUTTON_RESUME_MH_IMAGE_FILENAME)
        self.set_button_position_limits()

class Quit_Button(Button):
    def __init__(self):
        super().__init__()
        self.name       = "Quit button"
        self.center.y   = 100
        self.texture    = arcade.load_texture(global_variables.BUTTON_QUIT_IMAGE_FILENAME)
        self.mh_texture = arcade.load_texture(global_variables.BUTTON_QUIT_MH_IMAGE_FILENAME)
        self.set_button_position_limits()

