"""
Class: 
Components:
"""

# import
import arcade, math
import bullet_file
import projectile_file, point_file, velocity_file

# define
import global_variables_directory as global_variables

class Ship(projectile_file.Projectile):
    # initializer
    def __init__(self):
        super().__init__()

        # ship components
        self.name = "Ship"

        # Projectile components respecified
        self.center         = self.initialize_center()
        self.radius         = global_variables.SHIP_RADIUS
        self.angle_degrees  = global_variables.SHIP_ANGLE_INIT
        self.rotate_amnt    = global_variables.SHIP_ANGLE_ROTATE_AMOUNT

        # Ship draw components
        self.scale          = global_variables.SHIP_TEXTURE_SCALE
        self.alpha          = global_variables.SHIP_TEXTURE_ALPHA
        self.dark_mode      = global_variables.DARK_MODE_INIT

        # flames
        self.flames_p       = point_file.Point(self.center.x, self.center.y)
        self.thrust         = False

        # is ship life icon
        self.is_ship_life_icon   = False

    def initialize_center(self):
        return point_file.Point(
            global_variables.SHIP_X_INIT,
            global_variables.SHIP_Y_INIT - 125)

    """
    Class variables
    """
    troll_mode       = False
    ship_texture     = arcade.load_texture(global_variables.SHIP_IMAGE_FILENAME)
    air_horn_texture = arcade.load_texture(global_variables.SHIP_AIRHORN_IMAGE_FILENAME)
    ship_with_flames_texture = arcade.load_texture(global_variables.SHIP_WITH_FLAMES_IMAGE_FILENAME)

    """
    properties
    """
    @property
    def texture(self):
        if self.troll_mode: return self.air_horn_texture
        else:               return self.ship_texture

    """
    methods
    """

    """
    HIT
    """
    def hit(self):
        super().hit()
        self.__init__()

    """
    Advance
    """
    def advance(self):
        super().advance()
        self.thrust = False

    """
    DRAW
    """
    def draw(self):
        # draw ship (or air horn)
        scale   = self.scale
        texture = self.texture
        rotation = self.rotation

        if self.troll_mode:
            scale /= 2
            texture = self.air_horn_texture
            if self.is_ship_life_icon: rotation -= 90


        if self.thrust:
            texture = self.ship_with_flames_texture

        arcade.draw_scaled_texture_rectangle(
            self.center.x, 
            self.center.y, 
            texture, 
            scale, 
            rotation, 
            self.alpha)


    """
    ROTATE
    """
    def rotate_left(self):  self.rotation += global_variables.SHIP_ANGLE_ROTATE_AMOUNT
    def rotate_right(self): self.rotation -= global_variables.SHIP_ANGLE_ROTATE_AMOUNT

    """
    ACCELERATE
    """
    def accelerate(self):
        self.thrust     = True

        # set flames location
        angle           = self.angle_radians
        distance        = -25 # (negative because flames are behind ship)
        distance_x      = distance * math.cos(angle)
        distance_y      = distance * math.sin(angle)
        self.flames_p.x = self.center.x + distance_x
        self.flames_p.y = self.center.y + distance_y

        # get current speed
        current_v       = self.velocity

        # get acceleration and d_v amounts
        acceleration    = global_variables.SHIP_THRUST_ACCELERATE_AMOUNT
        dx, dy          = self.velocity_calculator.speed_to_dx_dy_degrees(acceleration, self.rotation + 90)
        d_v             = velocity_file.Velocity(dx, dy)

        # check if current speed has gone over speed limit
        if ((abs(current_v.dx + d_v.dx) > global_variables.SHIP_MAX_VELOCITY) or
            (abs(current_v.dy + d_v.dy) > global_variables.SHIP_MAX_VELOCITY)):
            self.velocity.speed -= 1

        # if not, then ACCELERATE!!!!! hehe
        else: self.velocity += d_v

    """
    FIRE
    + bullet speed
    + fast machine gun mode
    + fire()
    """
    # fast machine gun mode
    fast_machine_gun_mode = False

    # self.fire()
    def fire(self):
        # BULLET LOCATION
        # new bullet position: (Point object)
        bullet_location = point_file.Point(self.location.x, self.location.y)

        # BULLET VELOCITY

        # define bullet speed
        bullet_speed = global_variables.BULLET_SPEED
        if self.fast_machine_gun_mode:bullet_speed *= 2
        if global_variables.DEBUG: print(f"Bullet speed:", bullet_speed)

        # add bullet speed
        dx, dy = self.velocity_calculator.speed_to_dx_dy_degrees(
            bullet_speed, self.rotation + 90)
        bullet_velocity = velocity_file.Velocity(dx, dy)

        # add ship speed
        bullet_velocity += self.velocity

        # BULLET DRAW ROTATION
        rotation = self.rotation

        # fire new bullet
        new_bullet = bullet_file.Bullet(bullet_location, bullet_velocity, rotation)
        if self.fast_machine_gun_mode: new_bullet.red = True
        return new_bullet

    """
    DEBUG
    """
    def debug(self):
        super().debug()
        if True:
            print(f"{self.name} Point:    ({self.center.x   }, {self.center.y   })")
            print(f"{self.name} Velocity: ({self.velocity.dx}, {self.velocity.dy})")

# Rendered as a rectangle.
# The aim is controlled to match the mouse cursor.


class Ship_Lives_Icon(Ship):
    def __init__(self, p_init: point_file.Point):
        super().__init__()
        # ship lives variabels
        self.name = "Ship lives icon"
        self.is_ship_life_icon   = True

        # projectile variables respecified
        self.center = p_init
        self.scale  = global_variables.SHIP_LIVES_DRAWING_SCALE

    # override self.accelerate() and have it do nothing
    def accelerate(self): pass
