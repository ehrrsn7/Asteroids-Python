"""
File:   bullets.py
Author: Elijah Harrison

Class:      CS 241
Instructor: Brother Mellor

This file contains the Bullet class.
"""

# import
import arcade
import point_file, projectile_file, velocity_file
import global_variables_directory as global_variables

class Bullet(projectile_file.Projectile):
    def __init__(self, p_init: point_file.Point, v_init: velocity_file.Velocity, rotation: float):
        super().__init__()

        # Bullet components
        self.name           = "Bullet"
        self.timer_init     = global_variables.BULLET_TIMER
        self.die_on_timer   = True
        self.red            = False
        self.set_timer()

        # Bullet draw() components
        self.scale          = global_variables.BULLET_TEXTURE_SCALE
        self.alpha          = global_variables.BULLET_TEXTURE_ALPHA
        self.rotation       = rotation + 90

        # Projectile components respecified
        self.center         = p_init    # (to be specified when fire() is called)
        self.velocity       = v_init    # (to be specified when fire() is called)
        self.radius         = global_variables.BULLET_RADIUS

        # debug
        # self.debug()

    """
    Class Variables
    """
    texture_def = arcade.load_texture(global_variables.BULLET_IMAGE_FILENAME)
    texture_red = arcade.load_texture(global_variables.BULLET_FAST_IMAGE_FILENAME)


    """
    Properties
    """
    @property
    def texture(self):
        if self.red:    return self.texture_red
        else:           return self.texture_def


    """
    Methods
    """

    """
    Draw
    """
    def draw(self):
        delay = 5
        if self.red: delay = 0.5
        if self.timer < global_variables.BULLET_TIMER - delay:
            arcade.draw_scaled_texture_rectangle(
                self.center.x, 
                self.center.y, 
                self.texture, 
                self.scale, 
                self.rotation, 
                self.alpha)

    """
    Hit
    """
    def hit(self):
        self.alive = global_variables.DEAD
        if global_variables.DEBUG: print(f"{self.name.upper()}.hit()")

