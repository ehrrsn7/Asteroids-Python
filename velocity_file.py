"""
File: velocity.py
Name: Elijah Harrison

Class:      CS 241
Instructor: Brother Mellor

This file contains the Velocity class.
"""

# include
import math

class Velocity_Calculator:

    def magnitude_to_x_y_radians(self, magnitude: float, angle_radians: float):
        x   =   float(magnitude * math.cos(angle_radians))
        y   =   float(magnitude * math.sin(angle_radians))
        return (x, y)

    def get_magnitude_from_(self, x: float, y: float):
        return math.sqrt((x ** 2) + (y ** 2))

    def get_x_y_from_(self, magnitude: float, angle_degrees: float):
        return (magnitude * math.cos(math.radians(angle_degrees)),
                magnitude * math.sin(math.radians(angle_degrees)))

    def speed_to_dx_dy_radians(self, speed: float, angle_radians: float):
        return self.magnitude_to_x_y_radians(speed, angle_radians)

    def speed_to_dx_dy_degrees(self, speed: float, angle_degrees: float):
        return self.speed_to_dx_dy_radians(speed, math.radians(angle_degrees))

    def dx_dy_to_speed(self, dx: float, dy: float):
        return self.get_magnitude_from_(dx, dy)

    def dx_dy_to_angle_radians(self, dx: float, dy: float):
        return self.get_angle_degrees_from(dx, dy)

    def dx_dy_to_angle_degrees(self, dx: float, dy: float):
        return math.degrees(self.dx_dy_to_angle_radians(dx, dy))

    def get_angle_degrees_from(self, x: float, y: float):
        return math.atan2(y, x)



"""
Class:      Velocity
parameters: dx_init       (number)
            dy_init       (number)
components: dx            (number)
            dy            (number)
            ds            (number)
            speed         (number)
            angle_radians (number)
"""
class Velocity:
    # class variables
    calculator = Velocity_Calculator()

    # initializer
    def __init__(self, dx_init=0, dy_init=0):
        # initialize Velocity components
        self.dx = float(dx_init)
        self.dy = float(dy_init)

    """
    Properties
    """

    # SPEED
    @property
    def speed(self):
        return float(self.calculator.dx_dy_to_speed(self.dx, self.dy))

    @speed.setter
    def speed(self, speed):
        self.dx, self.dy = (
            self.calculator.speed_to_dx_dy_degrees(speed, self.angle_degrees)
        )

    # ANGLE_DEGREES
    @property
    def angle_degrees(self): return float(math.degrees(self.angle_radians))
    @angle_degrees.setter
    def angle_degrees(self, new_angle):
        self.angle_radians = float(math.radians(new_angle))

    # Angle Radians
    @property
    def angle_radians(self): return math.atan2(self.dy, self.dx)
    @angle_radians.setter
    def angle_radians(self, new_angle: float):
        # update dx and dy
        current_speed = self.speed
        self.dx = current_speed * math.cos(new_angle)
        self.dy = current_speed * math.sin(new_angle)

    """
    Methods
    """

    """
    Adders
    """
    def accelerate(self, d_speed: float): self.speed = self.speed + d_speed
    def add_dx(self,     ddx:     float): self.dx    = self.dx    + ddx
    def add_dy(self,     ddy:     float): self.dy    = self.dy    + ddy

    def add_dx_dy(self, dv):
        self.add_dx(dv._dx)
        self.add_dy(dv._dy)

    def add_angle_radians(self, d_angle): self.angle_radians = self.angle_radians + d_angle
    def add_angle_degrees(self, d_angle): self.angle_degrees = self.angle_degrees + d_angle

    """
    Operators
    """
    # +
    def __add__(self, rhs):
        # return Class_Template(new_t)
        dx = self.dx + rhs.dx
        dy = self.dy + rhs.dy
        return Velocity(dx, dy)

    # +=
    def __iadd__(self, rhs):
        return self + rhs

    # *
    def __mul__(self, rhs: float):
        dx = self.dx * rhs
        dy = self.dy * rhs
        return Velocity(dx, dy)

    # *=
    def __imul__(self, rhs: float):
        self.dx = self.dx * rhs
        self.dy = self.dy * rhs
