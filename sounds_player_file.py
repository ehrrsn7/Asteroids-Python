"""
File: sounds_player_file.py
Name: Elijah Harrison

This file contains the Sounds_Player class.
"""

# import
import arcade

# define
import global_variables_directory as global_variables
DEFAULT_VOLUME = 1.0


class Sounds_Player:
    def __init__(self):
        self.volume = DEFAULT_VOLUME

    # sounds
    fire_sound              = arcade.load_sound(global_variables.SOUND_FIRE)
    sound_explosion_large   = arcade.load_sound(global_variables.SOUND_EXPLOSION_LARGE)
    sound_explosion_medium  = arcade.load_sound(global_variables.SOUND_EXPLOSION_MEDIUM)
    sound_explosion_small   = arcade.load_sound(global_variables.SOUND_EXPLOSION_SMALL)
    sound_beat_1            = arcade.load_sound(global_variables.SOUND_BEAT_1)
    sound_beat_2            = arcade.load_sound(global_variables.SOUND_BEAT_2)
    sound_extra_ship        = arcade.load_sound(global_variables.SOUND_EXTRA_SHIP)
    sound_fire              = arcade.load_sound(global_variables.SOUND_FIRE)
    sound_air_horn          = arcade.load_sound(global_variables.SOUND_AIRHORN)
    sound_thrust            = arcade.load_sound(global_variables.SOUND_THRUST)

    # sound players
    def play_sound(self, sound, volume):
        try:
            arcade.sound.volume = volume
            arcade.play_sound(sound)
        except ValueError:
            print("ERROR: INVALID SOUND FORMAT")
            if not global_variables.DEBUG: print("(Check asteroids.py, line 296)")
            if not global_variables.DEBUG: print()

    def play_sound_explosion_large(self):   self.play_sound(self.sound_explosion_large, self.volume)
    def play_sound_explosion_medium(self):  self.play_sound(self.sound_explosion_medium,self.volume)
    def play_sound_explosion_small(self):   self.play_sound(self.sound_explosion_small, self.volume)
    def play_sound_beat_1(self):            self.play_sound(self.sound_beat_1,          self.volume)
    def play_sound_beat_2(self):            self.play_sound(self.sound_beat_2,          self.volume)
    def play_sound_extra_ship(self):        self.play_sound(self.sound_extra_ship,      self.volume)
    def play_sound_thrust(self):            self.play_sound(self.sound_thrust,          self.volume - 0.3)
    def play_sound_fire(self):              self.play_sound(self.sound_fire,            self.volume)
    def play_sound_air_horn(self):          self.play_sound(self.sound_air_horn,        self.volume)


    """
    Raise / Lower Volume
    """
    def raise_volume(self):
        if not global_variables.DEBUG: print("sounds_player.raise_volume() called")
        if self.volume < 10.0:
            self.volume += 1
        if not global_variables.DEBUG: print(f"New volume: {self.volume:.1f}")
        arcade.sound.volume = self.volume

    def lower_volume(self):
        if not global_variables.DEBUG: print("sounds_player.lower_volume() called")
        if self.volume > 0.1:
            self.volume -= 1
        if not global_variables.DEBUG: print(f"New volume: {self.volume:.1f}")
        arcade.sound.volume = self.volume


