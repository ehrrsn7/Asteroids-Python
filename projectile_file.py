"""
File: projectile.py
Name: Elijah Harrison

Class:      CS 241
Instructor: Brother Mellor

This file contains the Projectile class.
"""

# import
import arcade
import point_file, velocity_file

# define
import global_variables_directory as global_variables

# screen variables
SCREEN_WIDTH  = global_variables.SCREEN_WIDTH
SCREEN_HEIGHT = global_variables.SCREEN_HEIGHT

# other variables
DEAD          = global_variables.DEAD
DEBUG         = global_variables.DEBUG

"""
Class:      Projectile
Components: p       (Point)    // Point    component
            v       (Velocity) // Velocity component
            isalive (boolean)  // is alive
            angle   (number)   // angle    component
            r       (number)   // current  rotation
            radius  (number)   // radius of projectile
            thrust  (boolean)  // acceleration is being applied (y/n)
            timer   (number)   // delay timer
"""
class Projectile:
    # class variables
    velocity_calculator = velocity_file.Velocity_Calculator()

    # dark mode
    dark_mode           = global_variables.DARK_MODE_INIT

    # initializer
    def __init__(self):
        # name
        self.name = "Unknown projectile"

        # point base component
        self.p               = point_file.Point()

        # velocity component
        self.v              = velocity_file.Velocity()

        # rotation / change in rotation base component
        self.r              = 0
        self.dr             = 0

        # object radius
        self.radius         = 0

        # is alive
        self.alive          = global_variables.ALIVE

        # timer (to keep track of frames elapsed when needed)
        self.timer          = 0
        self.timer_init     = 0
        self.die_on_timer   = False

        # debug
        # self.debug()

    """
    Properties
    """
    # velocity
    @property
    def velocity(self): return self.v
    @velocity.setter
    def velocity(self, new_velocity: velocity_file.Velocity):
        self.v = new_velocity

    # angle_degrees
    @property
    def angle_degrees(self): return float(self.v.angle_degrees)
    @angle_degrees.setter
    def angle_degrees(self, new_angle: float):
        self.v.angle_degrees = new_angle

    # angle_radians
    @property
    def angle_radians(self): return float(self.v.angle_radians)
    @angle_radians.setter
    def angle_radians(self, new_angle: float):
        self.v.angle_radians = new_angle

    # center (position)
    @property
    def center(self): return self.p
    @center.setter
    def center(self, new_p: point_file.Point):
        self.p = new_p

    # position
    @property
    def location(self): return self.p
    @location.setter
    def location(self, new_p: point_file.Point):
        self.p = new_p

    # rotation
    @property
    def rotation(self): return self.r
    @rotation.setter
    def rotation(self, new_rotation: float):
        self.r = new_rotation

    """
    Methods
    """

    """
    Advance
    """
    def advance(self):
        self.center     += point_file.Point(self.velocity.dx, self.velocity.dy)
        self.rotation   += self.dr

        # handle timer
        # if there is time on timer, decrement timer counter
        if self.timer > 0:
            self.timer -= 1
            if DEBUG:
                print(f"Time remaining for {self.name}: {self.timer}")
        # if time is out, check if timer was set
        else:
            if self.die_on_timer: self.hit()

    """
    Draw (virtual function)
    """
    def draw(self): pass

    """
    Hit (virtual function)
    """
    def hit(self):
        if self.timer <= 0:
            self.alive = DEAD
            if not global_variables.DEBUG:
                print(f"{self.name.upper()}.hit()")

    """
    Set Timer
    """
    def set_timer(self):
        self.timer = self.timer_init
        self.die_on_timer = True

    """
    adders
    """
    def add_rotation(self, dr): self.rotation += dr

    """
    dark mode getter/setters
    """
    # get dark mode
    def is_dark_mode(self): return self.dark_mode

    # set dark_mode
    def set_dark_mode(self):
        self.dark_mode = True
        self.color = self.initialize_color()
    
    def set_light_mode(self):
        self.dark_mode = False
        self.color = self.initialize_color()

    def initialize_color(self):
        color                    = arcade.color.WHITE
        if self.dark_mode: color = arcade.color.BLACK

        return color

    """
    Debug
    """
    def debug(self):
        if not global_variables.DEBUG: 
            print(f"{self.name.upper()} created")
