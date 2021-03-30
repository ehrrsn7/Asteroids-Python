"""
File: rock_base.py
Name: Elijah Harrison

Class:      CS 241
Instructor: Brother Mellor
"""

# import
import arcade, random
import projectile_file, point_file, velocity_file

# define
import global_variables_directory as global_variables

"""
Class: Rock
Components:
"""
class Rock(projectile_file.Projectile):
    # initializer
    def __init__(self):
        super().__init__()

        # Rock components
        self.name       = "Unknown asteroid"
        self.hit_pts    = global_variables.ROCK_DEFAULT_POINTS_AWARDED

        # Rock draw components
        self.rotation   = random.randint(0, 360)
        self.dr         = global_variables.ROCK_DEFAULT_SPIN
        self.alpha      = global_variables.DEFAULT_TEXTURE_ALPHA

        # Projectile components respecified
        self.radius     = global_variables.ROCK_DEFAULT_RADIUS
        self.center     = self.get_random_center_point()
        self.timer_init = global_variables.ROCK_DEFAULT_TIMER_INIT

        # initialize velocity
        self.rock_speed = global_variables.ROCK_DEFAULT_SPEED
        self.rock_angle = random.randint(0, 360)
        self.velocity   = self.initialize_velocity()


    """
    Class variables
    """
    # class variables
    troll_mode = False
    default_texture = arcade.load_texture(global_variables.ROCK_DEFAULT_IMAGE_FILENAME)
    greg            = arcade.load_texture(global_variables.TROLL_IMAGE_FILENAME)
    greg_scale      = 0.25

    """
    Properties
    """
    @property
    def texture(self):
        if self.troll_mode:
            return self.greg
        else: return self.default_texture


    @property
    def scale(self):
        if self.troll_mode: return self.greg_scale
        else: return global_variables.DEFAULT_TEXTURE_SCALE

    """
    methods
    """
    def get_random_center_point(self, x_init = 0, y_init = 0):
        x_init  = random.randint(0, global_variables.SCREEN_WIDTH)
        y_init  = random.randint(0, global_variables.SCREEN_HEIGHT)
        return point_file.Point(x_init, y_init)

    def initialize_velocity(self):
        # create velocity based off of rock speed info
        dx, dy = self.velocity_calculator.speed_to_dx_dy_degrees(
            self.rock_speed, self.rock_angle)
        return velocity_file.Velocity(dx, dy)

    """
    DRAW
    """
    def draw(self):
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
        super().hit()
        return self.hit_pts



"""
Class:      Small Rock
Inherit:    Rock class
Components:
"""
class Rock_Small(Rock):
    # initializer
    def __init__(self, p_init: point_file.Point):
        super().__init__()

        # small rock components
        self.name       = "Small Asteroid"
        self.radius     = global_variables.ROCK_SMALL_RADIUS
        self.hit_pts    = global_variables.ROCK_SMALL_POINTS_AWARDED

        # Rock draw components respecified
        self.dr         = global_variables.ROCK_SMALL_SPIN

        # inherit p_init from split rock
        self.center     = p_init

        # initialize velocity
        self.rock_speed = global_variables.ROCK_SMALL_SPEED
        self.velocity   = self.initialize_velocity()


    """
    Class variables
    """
    # class variables
    troll_mode      = False
    default_texture = arcade.load_texture(global_variables.ROCK_SMALL_IMAGE_FILENAME)
    greg            = arcade.load_texture(global_variables.TROLL_IMAGE_FILENAME)
    greg_scale      = 0.075


"""
Class:      Medium Rock
Inherit:    Rock class
Components:
"""
class Rock_Medium(Rock):
    # initializer
    def __init__(self, p_init: point_file.Point):
        super().__init__()

        # medium rock components
        self.name       = "Medium asteroid"
        self.radius     = global_variables.ROCK_MEDIUM_RADIUS
        self.hit_pts    = global_variables.ROCK_SMALL_POINTS_AWARDED

        # Rock draw components respecified
        self.dr         = global_variables.ROCK_MEDIUM_SPIN

        # inherit p_init from split rock
        self.center     = p_init

        # initialize velocity
        self.rock_speed = global_variables.ROCK_MEDIUM_SPEED
        self.velocity   = self.initialize_velocity()

    """
    Class variables
    """
    # class variables
    troll_mode      = False
    default_texture = arcade.load_texture(global_variables.ROCK_MEDIUM_IMAGE_FILENAME)
    greg            = arcade.load_texture(global_variables.TROLL_IMAGE_FILENAME)
    greg_scale      = 0.15


    """
    Methods
    """

    """
    Split
    """
    def split(self):
        if global_variables.DEBUG: print(f"{self.name.upper()}.split()")
        rock_1_center = point_file.Point(self.center.x, self.center.y)
        rock_2_center = point_file.Point(self.center.x, self.center.y)
        return (Rock_Small(rock_1_center),
                Rock_Small(rock_2_center))


"""
Class:      Big Rock
Inherit:    Rock class
Components:
"""
class Rock_Big(Rock):
    # initializer
    def __init__(self):
        super().__init__()
        self.name = "Large asteroid"

    """
    Class variables
    """
    # class variables
    troll_mode      = False
    default_texture = arcade.load_texture(global_variables.ROCK_BIG_IMAGE_FILENAME)
    greg            = arcade.load_texture(global_variables.TROLL_IMAGE_FILENAME)
    greg_scale      = 0.25

    """
    Methods
    """

    """
    Split
    """
    def split(self):
        if global_variables.DEBUG: print(f"{self.name.upper()}.split()")
        rock_1_center = point_file.Point(self.center.x, self.center.y)
        rock_2_center = point_file.Point(self.center.x, self.center.y)
        return (Rock_Medium(rock_1_center),
                Rock_Medium(rock_2_center))

