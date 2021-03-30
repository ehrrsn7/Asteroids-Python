"""
File: class_template.py
Name: Elijah Harrison

Class:      CS 241
Instructor: Brother Mellor
"""

# import
import point_file, on_screen_text_file

# define
import global_variables_directory as global_variables
RESUME          = global_variables.RESUME
PAUSE           = global_variables.PAUSE
MAIN_MENU       = global_variables.MAIN_MENU
NEW_LEVEL       = global_variables.NEW_LEVEL
GAME_OVER       = global_variables.GAME_OVER
SHIP_WAS_HIT    = global_variables.SHIP_WAS_HIT


class Gamestate(on_screen_text_file.On_Screen_Text):
    def __init__(self):
        # inherit On_Screen_Text class attributes
        super().__init__()

        # On_Screen_Text draw attributes
        self.display_text = False
        self.p = point_file.Point(
            global_variables.GAMESTATE_POSITION_X, 
            global_variables.GAMESTATE_POSITION_Y)

        # gamestate attributes
        self.state  = global_variables.STATE_INIT
        if not global_variables.DEBUG: print(f"initializing gamestate")
        if not global_variables.DEBUG: print(f"initial gamestate:", self.text)

    @property
    def state_text(self):
        if   self.state == RESUME      : return f"RESUME      " # .capitalize()
        elif self.state == PAUSE       : return f"PAUSE       " # .capitalize()
        elif self.state == MAIN_MENU   : return f"MAIN_MENU   " # .capitalize()
        elif self.state == NEW_LEVEL   : return f"NEW_LEVEL   " # .capitalize()
        elif self.state == GAME_OVER   : return f"GAME_OVER   " # .capitalize()
        elif self.state == SHIP_WAS_HIT: return f"SHIP_WAS_HIT" # .capitalize()
        else:                            return f"Unknown state"

    @property
    def text(self):
        return f"State: {self.state_text} ({self.state})"