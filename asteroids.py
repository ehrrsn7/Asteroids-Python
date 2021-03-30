"""
File:   Asteroids.py
Author: Elijah Harrison

ABOVE AND BEYOND:

- More handle input options
"""

"""
Import
"""
# import python libraries
import arcade, random, math

# import author's files
import gamestate_file
import gamestate_screens_file
import level_file
import on_screen_text_file
import point_file
import projectile_file
import rocks_file
import score_file
import ship_file
import sounds_player_file
import velocity_file

# import global variables directory,
# save all variables we will need
# These are Global constants to use throughout the game
import global_variables_directory as global_variables

# grab some for easy reference
DEBUG         = global_variables.DEBUG
SCREEN_HEIGHT = global_variables.SCREEN_HEIGHT
SCREEN_WIDTH  = global_variables.SCREEN_WIDTH
ALIVE         = global_variables.ALIVE
DEAD          = global_variables.DEAD

"""
Class: Game
This class handles all the game callbacks and interaction
It assumes the following classes exist:
    Ship
    Rock (and it's sub-classes)
    Point
    Velocity
    Bullet
This class will then call the appropriate functions of
each of the above classes.
You are welcome to modify anything in this class, but mostly
you shouldn't have to. There are a few sections that you
must add code to.
"""
class Game(arcade.Window):
    """
    Game class variables
    """
    # class variables
    velocity_calculator = velocity_file.Velocity_Calculator()           # velocity calculator
    background_color    = global_variables.SCREEN_COLOR_DARK            # background color
    held_keys           = set()                                         # held keys
    mouse_position      = point_file.Point()                            # mouse_position
    screens             = gamestate_screens_file.Gamestate_Screens()    # screens
    sounds_player       = sounds_player_file.Sounds_Player()            # sounds

    # some 'draw objects'-related states
    mouse_pressed       = False
    mach_gun_activated  = True
    machine_gun_timer   = 0
    machine_gun_timer_delay = global_variables.SHIP_FIRING_RATE_DELAY


    """
    Initializer
    """
    def __init__(self, width, height):
        """
        Sets up the initial conditions of the game
        :param width:  Screen width
        :param height: Screen height
        """
        super().__init__(width, height)                     # initialize game window
        arcade.set_background_color(self.background_color)  # set game window color

        """
        Initialize game objects
        """
        # gamestate
        self.gamestate  = gamestate_file.Gamestate()
        # score / level
        self.score      = score_file.Score()
        self.level      = level_file.Level()
        # ship
        self.ship       = ship_file.Ship()  # initialize ship
        # bullet
        self.bullets    = [              ]  # initialize bullets list
        # rocks
        self.rocks      = [              ]  # initialize rocks list
        self.initialize_rocks()             # game must start with 5 rocks
        # lives
        self.lives      = [              ]  # initialize ship lives list
        self.initialize_ship_lives()        # game must start with 3 ship lives

        """
        Other game logic variables
        """
        # troll mode
        self.troll_mode         = False

        # sound conditional
        self.sound              = True

        # heartbeat background sound data
        self.sound_beat_delay   = global_variables.SOUND_BEAT_DELAY_INIT
        self.sound_beat_1_or_2  = 1 # (initialize)
        self.sound_beat_delay_offset = 0
        self.decrement_sound_beat_delay = True

        # score name recorded variable
        self.score_name_record  = False

        # extra life information
        self.next_extra_life    = 1


    # other initializer submethods
    def initialize_rocks(self):
        # initialing method:
        # game must begin with 5 rocks on the screen
        # therefore, __init__ must either do this 
        # explicitly or call this method.
        for _i in range(global_variables.ROCK_INIT_AMOUNT):
            if global_variables.DEBUG: print(f"Initializing rock: {_i+1}")
            new_rock = rocks_file.Rock_Big()
            if DEBUG: print("Making new rock", _i + 1)
            self.rocks.append(new_rock)
        if DEBUG:
            print("New rocks[] amount after calling self.initialize_rocks():",
                  len(self.rocks))

    @property
    def ship_lives_amount(self): return len(self.lives)

    def initialize_ship_lives(self):
        # now, make the ship life icons
        # for _i in range(global_variables.SHIP_LIVES_INIT_AMOUNT):
        for _i in range(global_variables.SHIP_LIVES_INIT_AMOUNT):
            self.append_new_ship_life_icon()
            if global_variables.DEBUG:
                print(f"Initializing ship life icon {_i + 1} of {self.ship_lives_amount}")

    def append_new_ship_life_icon(self):
        # ship lives amount
        current_ship_lives_amount = len(self.lives)
        if not DEBUG: print("Appending new ship life icon: no.", len(self.lives))

        # x position
        x_init      = global_variables.SHIP_LIVES_X_POSITION_INIT
        position_x  = x_init + (
              current_ship_lives_amount
            * global_variables.SHIP_LIVES_X_POSITION_SPACING)

        # y position
        position_y  = global_variables.SHIP_LIVES_Y_POSITION

        # make new icon
        new_ship_life_icon = ship_file.Ship_Lives_Icon(point_file.Point(position_x, position_y))

        # append new icon to self.lives[]
        self.lives.append(new_ship_life_icon)


    """
    DECONSTRUCTOR / DELETER FUNCTION
    """
    # def __del__(self): pass

    """
    DRAW
    - on_draw
    - draw all objects
        * draw ship
        * draw ship life icons
        * draw bullets
        * draw bullets
        * draw rocks
        # draw on screen text
    """
    def on_draw(self):
        """
        Called automatically by the arcade framework.
        Handles the responsibility of drawing all elements.
        """

        # clear the screen to begin drawing
        arcade.start_render()
        self.draw_all_objects()

    # on_draw submethods
    def draw_all_objects(self):
        self.draw_ship()
        self.draw_ship_life_icons()
        self.draw_bullets()
        self.draw_rocks()
        self.draw_on_screen_text()
        self.draw_gamestate_screens()

    def draw_ship(self):
        self.ship.draw()

    def draw_ship_life_icons(self):
        for ship_life_icon in self.lives:
            ship_life_icon.draw()

    def draw_bullets(self):
        if self.is_state_show_all_objects():
            for bullet in self.bullets:
                bullet.draw()

    def draw_rocks(self):
        for rock in self.rocks:
            rock.draw()

    def draw_on_screen_text(self):
        self.score.draw()
        self.level.draw()
        if not DEBUG:
            self.gamestate.draw()

    def draw_gamestate_screens(self):
        mouse_x = self.mouse_position.x
        mouse_y = self.mouse_position.y

        if self.is_main_menu():
            self.screens.main_menu_screen.draw()
            self.screens.main_menu_screen.check_mouse_hovering_over_button(mouse_x, mouse_y)
            if self.mouse_pressed:
                self.screens.main_menu_screen.check_mouse_clicked(mouse_x, mouse_y)

        if self.is_pause():
            self.screens.pause_screen.draw()

        if self.is_new_level():
            self.screens.new_level_screen.draw()

        if self.is_ship_was_hit():
            self.screens.ship_was_hit_msg.draw()

        if self.is_game_over():
            self.screens.game_over_screen.draw()
            if self.score_name_record:
                # self.write_high_score()
                self.score_name_record = False

        if self.is_resume():
            arcade.draw_scaled_texture_rectangle(
                global_variables.SCREEN_RIGHT_X - 50,
                10,
                arcade.load_texture(global_variables.PAUSE_HINT_IMAGE_FILENAME),
                global_variables.DEFAULT_TEXTURE_SCALE / 2,
                global_variables.DEFAULT_TEXTURE_ANGLE,
                global_variables.DEFAULT_TEXTURE_ALPHA)


    """
    ADVANCE
    + update
    + advance all projectiles
    + advance rocks
    + advance bullets
    """
    def update(self, delta_time):
        """
        Update each object in the game.
        :param delta_time: tells us how much time has actually elapsed
        """

        # handle objects
        self.advance_all_projectiles()
        self.wrap_objects()

        # handle events
        self.check_collisions()
        self.check_keys()
        self.handle_score()
        if not self.is_main_menu():
            self.handle_beat_sound()


    def advance_all_projectiles(self):
        self.advance_rocks()
        self.advance_bullets()
        self.advance_ship()
    
    def advance_ship(self):
        self.ship.advance()

    def advance_rocks(self):
        for rock in self.rocks:
            rock.advance()
        if len(self.rocks) == 0:
            if not self.is_new_level():
                self.new_level()

    def advance_bullets(self):
        for bullet in self.bullets:
            bullet.advance()
        
        self.machine_gun_timer -= 1

    """
    WRAP

    wrap(proj) is to be called to check 
    if any of the Projectiles 
    (the ship, or any bullets or rocks)
    have left the screen;
    in each of these cases, the individual 
    Projectile's position must be updated 
    for it to appear on the opposite side 
    of the screen.

    wrap_objects() simply calls wrap(proj)
    for each of the Projectile objects in
    the game.
    """
    def wrap_objects(self):
        buffer = 0
        # wrap ship
        if self.is_off_screen(self.ship, buffer):
            self.wrap(self.ship)
        # self.wrap(self.ship)

        # wrap bullets
        for bullet in self.bullets:
            if self.is_off_screen(bullet, buffer):
                self.wrap(bullet)
            # self.wrap(bullet)

        # wrap rocks
        for rock in self.rocks:
            if self.is_off_screen(rock, buffer):
                self.wrap(rock)
            # self.wrap(rock)

    def wrap(self, proj: projectile_file.Projectile):

        left_side_x  = 5
        right_side_x = global_variables.SCREEN_WIDTH - 5

        bottom_y     = 5
        top_y        = global_variables.SCREEN_HEIGHT - 5

        # if projectile goes off of left side, 
        # send it to the right
        if   proj.center.x < left_side_x:
            proj.center.x  = right_side_x
            if global_variables.DEBUG: print("Object reached left side")

        # or conversely, if projectile goes off 
        # of right side, send it to the left
        elif proj.center.x > right_side_x:
            proj.center.x  = left_side_x
            if global_variables.DEBUG: print("Object reached right side")

        # same process with the top and bottom:

        # if projectile goes off of left side, 
        # send it to the right
        if   proj.center.y > top_y:
            proj.center.y  = bottom_y
            if global_variables.DEBUG: print("Object reached top")

        # or conversely, if projectile goes off 
        # of right side, send it to the left
        elif proj.center.y < bottom_y:
            proj.center.y  = top_y
            if global_variables.DEBUG: print("Object reached bottom")

        # take note that each of the if statements have
        # a < or > symbol, and NOT a <= or >=
        # ...this is imperitve to having the objects 
        # being not sent into tHE ABYSS. ("dun dun duUUUUNNNNN")

    """
    EVENTS (HANDLE INPUT)
    """
    def on_key_press(self, key: int, modifiers: int):
        """
        'One time' key events:
        - add SPACE, RIGHT, LEFT and UP to self.held_keys
        - handle R, P, K, D and Q
        """

        """
        Add to self.held_keys
        these 'held keys' are handled in self.check_keys()
        """
        # space
        if key == arcade.key.SPACE:
            if not DEBUG: print("Adding key...")
            self.held_keys.add(key)

        # right
        if key == arcade.key.RIGHT:
            if not DEBUG: print("Adding key...")
            self.held_keys.add(key)

        # left
        if key == arcade.key.LEFT:
            if not DEBUG: print("Adding key...")
            self.held_keys.add(key)

        # up
        if key == arcade.key.UP:
            if not DEBUG: print("Adding key...")
            self.held_keys.add(key)

        """
        Handle Keys:
        R - resume
        P - pause
        S - toggle sound
        A - lower volume (not functional)
        D - raise volume (not functional)
        K - toggle troll mode
        Z - toggle rapid fire mode
        Q - quit game
        W or ESC - restart game
        """
        if key == arcade.key.R:
            if not DEBUG: print("'R' was pressed.")
            if (self.is_pause() or
                self.is_ship_was_hit() or
                self.is_new_level()):

                self.resume()

            elif self.is_game_over():

                self.restart_game()

        # state events:
        # pause
        if key == arcade.key.P:
            if not DEBUG: print("'P' was pressed.")
            if (self.is_resume()       or
                self.is_ship_was_hit() or
                self.is_pause()      ):
                if not DEBUG: print("Pausing game")
                self.toggle_pause()
                # TODO: delete all cases of 'hints' in asteroids,
                # put code in to draw a 'pause screen' when necessary

        # display events:
        # release the kraken
        if key == arcade.key.T:
            if not DEBUG: print("'T' was pressed.")
            self.toggle_troll()
        
        # sound events
        # mute / unmute
        if key == arcade.key.S:
            self.sound = self.toggle(self.sound)
            if not DEBUG:
                print("'S' was pressed.")
                if self.sound:  print("Sound unmuted.")
                else:           print("Sound muted.")

        # raise volume
        if key == arcade.key.D:
            if not DEBUG: print("'D' was pressed.")
            self.sounds_player.raise_volume()

        # lower volume
        if key == arcade.key.A:
            if not DEBUG: print("'A' was pressed.")
            self.sounds_player.lower_volume()

        # quit game
        if key == arcade.key.Q:
            if not DEBUG: print("'Q' was pressed.")
            self.quit_game()

        if key == arcade.key.Z:
            if not DEBUG: print("'Z' was pressed.")
            ship_file.Ship.fast_machine_gun_mode = self.toggle(
                ship_file.Ship.fast_machine_gun_mode)
            if ship_file.Ship.fast_machine_gun_mode:
                self.machine_gun_timer_delay = 1.5
                print("FAST MACHINE GUN MODE == TRUE")
            else:
                self.machine_gun_timer_delay = global_variables.SHIP_FIRING_RATE_DELAY
                print("FAST MACHINE GUN MODE == false".capitalize())

        if key == arcade.key.W or key == arcade.key.ESCAPE:
            if not DEBUG: print("'W / ESC' was pressed.")
            self.restart_game()


    def check_keys(self):
        """
        This method has the same purpose as on_key_press()..
        HOWEVER, this method is called by on_update(), not 
        the arcade mainframe itself; 
        also, when this function is called, its keys being 
        held will hold the event for more than just one frame. 
        (# MACHINE GUN TIME)

        This method also relies on self.on_key_press():
        whenever a button is pressed, that button must be
        ADDED onto self.held_keys (initialized by line of 
        code in __init__())
        we must also take it out in on_key_release()
        """
        # space
        if arcade.key.SPACE in self.held_keys:
            if DEBUG: print("arcade.key.SPACE in self.held_keys")
            if self.is_resume(): self.fire_bullet()
            if self.is_main_menu(): self.resume()

        # up
        if arcade.key.UP in self.held_keys:
            if DEBUG: print("arcade.key.UP in self.held_keys")
            if self.is_resume(): self.accelerate_ship()

        # left
        if arcade.key.LEFT in self.held_keys:
            if DEBUG: print("arcade.key.LEFT in self.held_keys")
            if self.is_resume(): self.ship.rotate_left()

        # right
        if arcade.key.RIGHT in self.held_keys:
            if DEBUG: print("arcade.key.RIGHT in self.held_keys")
            if self.is_resume(): self.ship.rotate_right()

    def on_key_release(self, key: int, modifiers: int):
        """
        Removes the current key from the set of held keys.
        """
        if key in self.held_keys:
            if not DEBUG: print("Removing key...")
            self.held_keys.remove(key)

    def on_mouse_motion(self, x, y, key, modifiers):
        """
        Called when user moves the mouse
        """
        # handle mouse motion
        if DEBUG: print("game.on_mouse_motion() called")
        if DEBUG: print(f"new game.mouse_position == Point({x}, {y})")
        self.mouse_position.x = x
        self.mouse_position.y = y

        arcade.draw_scaled_texture_rectangle(
            x, y,
            arcade.load_texture(global_variables.ASTEROIDS_LOGO_IMAGE_FILENAME), 
            global_variables.DEFAULT_TEXTURE_SCALE,
            global_variables.DEFAULT_TEXTURE_ANGLE,
            global_variables.DEFAULT_TEXTURE_ALPHA)

    def on_mouse_press(self, x, y, key, modifiers):
        """
        Called when user presses the mouse
        """
        self.mouse_pressed = True

    def on_mouse_release(self, x, y, key, modifiers):
        """
        Called when user releases the mouse
        """
        self.mouse_pressed = False


    """""""""""""""""""""
    CHECK COLLISIONS
    - check collisions
    - check collisions between rock and ship
    - check collisions between rock and bullets
    - check too close
    - clean up zombies
    """""""""""""""""""""
    def check_collisions(self):
        """
        Checks to see if bullets have hit rocks.
        Updates scores and removes dead items.
        :return:
        """

        # when gamestate is not RESUME, 
        # do not count collisions
        if self.is_resume():
            for rock in self.rocks:
                self.check_collisions_between_rock_and_ship(rock)
                self.check_collisions_between_rock_and_bullets(rock)

                # We will wait to remove the dead objects until after we
                # finish going through the list

        # Now, check for anything that is dead, and remove it
        self.cleanup_zombies()

    def check_collisions_between_rock_and_ship(self, rock):
        """
        Collision between rocks and ship
        """
        # now, check if the ship collided with any of the rocks
        if rock.alive and self.ship.alive:
            if DEBUG: print(f"rock, ship radii: {rock.radius}, {self.ship.radius}")

            if self.check_too_close(rock, self.ship):
                # it's a hit!
                if DEBUG: print(f"{rock.name} and Ship were too close")
                if DEBUG: print(f"{     rock.name:10} radius: {     rock.radius}")
                if DEBUG: print(f"{self.ship.name:10} radius: {self.ship.radius}")

                # hit ship and rock
                self.ship_was_hit()
                rock.hit()

                # split rocks if appropriate
                if rock.name == "Large asteroid" or rock.name == "Medium asteroid":
                        new_rock1, new_rock2 = rock.split()
                        self.rocks.append(new_rock1)
                        self.rocks.append(new_rock2)

    def check_collisions_between_rock_and_bullets(self, rock):
        """
        Collision between rocks and bullets
        """
        for bullet in self.bullets:

            # Make sure they are both alive before checking for a collision
            if bullet.alive and rock.alive:
                if DEBUG: print(f"bullet, rock radii: {bullet.radius}, {rock.radius}")

                if self.check_too_close(rock, bullet):
                    # it's a hit!
                    if DEBUG: print(f"\n{rock.name} and {bullet.name} were too close")
                    bullet.hit()
                    self.score.score += rock.hit()

                    # play explosion sound
                    if rock.name == "Large asteroid":  self.sounds_player.play_sound_explosion_large()
                    if rock.name == "Medium asteroid": self.sounds_player.play_sound_explosion_medium()
                    if rock.name == "Small asteroid":  self.sounds_player.play_sound_explosion_small()
                    else: self.sounds_player.play_sound_explosion_large()

                    if rock.name == "Large asteroid" or rock.name == "Medium asteroid":
                        new_rock1, new_rock2 = rock.split()
                        self.rocks.append(new_rock1)
                        self.rocks.append(new_rock2)

    def check_too_close(self, projectile1, projectile2):
        if DEBUG: print(
            f"check_too_close({projectile1.name.upper()}, {projectile2.name.upper()}) called")
        too_close = projectile1.radius   + projectile2.radius
        return (abs(projectile1.center.x - projectile2.center.x) < too_close and
                abs(projectile1.center.y - projectile2.center.y) < too_close)

    def cleanup_zombies(self):
        """
        Removes any dead bullets or rocks from the list.
        """
        # clear any bullets that were hit
        for bullet in self.bullets:
            if not bullet.alive:
                self.bullets.remove(bullet)
                if DEBUG: print("Cleaning up zombie 🧟‍♂️")

        # clear any rocks that were hit
        for rock in self.rocks:
            if not rock.alive:
                self.rocks.remove(rock)
                if DEBUG: print("Cleaning up zombie 🧟‍♂️")


    """
    IS ON SCREEN
    - is off screen
    - is on  screen
    """
    def is_off_screen(self, proj: projectile_file.Projectile, buffer = 10):
        return not self.is_on_screen(proj, buffer)

    def is_on_screen(self, proj: projectile_file.Projectile, buffer = 10):

        if ((proj.center.x > buffer and proj.center.x < global_variables.SCREEN_WIDTH  - buffer) and
            (proj.center.y > buffer and proj.center.y < global_variables.SCREEN_HEIGHT - buffer)):

            return True

        else:
            if global_variables.DEBUG: print("Projectile is off screen")
            return False


    """
    CLEAR OBJECTS
    - clear all objects
    - clear all bullets
    - clear all rocks
    """
    def clear_all_objects(self):
        self.clear_all_bullets()
        self.clear_all_rocks()
        self.initialize_rocks()
        self.ship.__init__()
        self.score.__init__()

    def clear_all_bullets(self):
        for bullet in self.bullets:
            self.bullets.remove(bullet)
            bullet = None

    def clear_all_rocks(self):
        while len(self.rocks) != 0:
            self.rocks.pop()
            if global_variables.DEBUG:
                print("Removing rock")

        if global_variables.DEBUG:
            print("Rocks[] amount after clearing all rocks:",
                  len(self.rocks))


    """
    GAME STATE
    """
    # gamestate property
    @property
    def state(self): return self.gamestate.state
    
    @state.setter
    def state(self, new_value: int):
        # To set the state to a value, we must set 
        # the state attribute within self.gamestate
        self.gamestate.state = new_value
        if not global_variables.DEBUG: print("New", self.gamestate.text)

    # setters
    def resume(self):
        if not DEBUG: print("self.resume() called")
        if not self.is_new_level():
            self.state =  global_variables.RESUME
            self.reset_sound_beat_delay()
        else: self.start_new_level()

    def pause(self):
        if not DEBUG: print("self.pause() called")
        self.state =  global_variables.PAUSE
        self.ship.velocity.__init__()

    def toggle_pause(self):
        if self.is_pause():
            self.resume()
        elif self.is_resume():
            self.pause()

    def main_menu(self):
        if not DEBUG: print("self.main_menu() called")
        self.state =  global_variables.MAIN_MENU

    def new_level(self):
        if not DEBUG: print("self.new_level() called")
        # set new state
        self.state =  global_variables.NEW_LEVEL
        # increment level: (int) text value on screen
        self.level.next_level()

    def start_new_level(self):
        self.initialize_rocks()
        self.ship.__init__()
        self.state = global_variables.RESUME

    def game_over(self):
        if not DEBUG: print("self.game_over() called")
        self.state =  global_variables.GAME_OVER
        self.score_name_record = True

    def ship_was_hit(self):
        if not DEBUG: print("self.ship_was_hit() called")
        self.state =  global_variables.SHIP_WAS_HIT
        if not DEBUG: print(f"{self.ship.name}.hit()")
        self.ship.hit()

        # remove one of the ship lives and keep going
        if len(self.lives) > 1:
            self.lives.pop()
        else:
            self.game_over()

    # getters
    def is_resume(self):        return  self.state == global_variables.RESUME
    def is_pause(self):         return  self.state == global_variables.PAUSE
    def is_main_menu(self):     return  self.state == global_variables.MAIN_MENU
    def is_new_level(self):     return  self.state == global_variables.NEW_LEVEL
    def is_game_over(self):     return  self.state == global_variables.GAME_OVER
    def is_ship_was_hit(self):  return  self.state == global_variables.SHIP_WAS_HIT

    def is_state_show_all_objects(self):
        return (self.is_resume()    or
                self.is_pause()     or
                self.is_new_level() or
                self.is_game_over() or
                self.is_ship_was_hit())
    
    def is_state_advance_all_objects(self):
        return (self.is_resume())

    """
    Other game information methods
    """
    def handle_score(self):
        if self.score.score >= self.next_extra_life * 10_000:
            self.extra_life()

    def extra_life(self):
        self.next_extra_life   += 1
        self.append_new_ship_life_icon()
        if self.sound:
            self.sounds_player.play_sound_extra_ship()

    # restart game
    def restart_game(self):
        if not DEBUG: print("Restarting game...")
        self.__init__(SCREEN_WIDTH, SCREEN_HEIGHT)
    
    # quit game
    def quit_game(self):
        if not DEBUG: print("Quitting game...")
        self.__del__()

    # troll mode
    @property
    def troll(self): return self.troll_mode
    @troll.setter
    def troll(self, new_value: bool):
        print("troll property reached")
        self.troll_mode = new_value
        ship_file.Ship.troll_mode           = new_value
        rocks_file.Rock.troll_mode          = new_value
        rocks_file.Rock_Big.troll_mode      = new_value
        rocks_file.Rock_Medium.troll_mode   = new_value
        rocks_file.Rock_Small.troll_mode    = new_value

        if self.troll_mode:
            if DEBUG: print("Troll mode: NO")
            if DEBUG: print("setting game.troll_mode = True")
            self.machine_gun_timer_delay    = 10
        else:
            if DEBUG: print("Troll mode: YES")
            if DEBUG: print("setting game.troll_mode = False")
            self.machine_gun_timer_delay    = global_variables.SHIP_FIRING_RATE_DELAY

    def toggle_troll(self):
        if not DEBUG: print("self.toggle_troll() called")
        self.troll = self.toggle(self.troll)

    def toggle(self, conditional):
        if conditional: return False
        else:           return True

    # machine gun
    def set_machine_gun_timer(self):
        self.machine_gun_timer = self.machine_gun_timer_delay

    # fire bullet
    def fire_bullet(self):
        # create Bullet
        if self.machine_gun_timer <= 0:
            new_bullet = self.ship.fire()

            # add that Bullet to self.bullets[]
            self.bullets.append(new_bullet)

            self.set_machine_gun_timer()

            # play sound
            if self.troll:
                print("Troll mode on: play air horn sound")
                if self.sound:
                    self.sounds_player.play_sound_air_horn()
            else:
                if self.sound:
                    self.sounds_player.play_sound_fire()

    # accelerate ship
    def accelerate_ship(self):
        self.ship.accelerate()
        if self.sound:
            self.sounds_player.play_sound_thrust()

    # handle beat sound
    def handle_beat_sound(self):
        """
        Decrement delay timer
        """
        decrement_amount = 1

        if not self.sound_beat_delay <= 0:
            self.sound_beat_delay -= decrement_amount
            if DEBUG: print("Decrementing sound beat delay timer...")
            if DEBUG: print(f"Sound beat delay: {self.sound_beat_delay}, ({self.sound_beat_delay_offset})")

        else:
            """
            Handle sound decrement offset details
            """
            # increment delay offset
            if self.decrement_sound_beat_delay:
                if DEBUG: print("Sound beat delay decrement == True")
                self.sound_beat_delay_offset += global_variables.BEAT_DELAY_OFFSET_INCREMENT

            # put limit on offset
            max_offset = (
                  global_variables.SOUND_BEAT_DELAY_INIT
                - global_variables.MINIMUM_BEAT_DELAY)
            if self.sound_beat_delay_offset > max_offset:
                self.sound_beat_delay_offset = max_offset

            # set new sound beat delay init based off offset value
            self.sound_beat_delay = (
                global_variables.SOUND_BEAT_DELAY_INIT
                - self.sound_beat_delay_offset)

            if DEBUG: print("new sound beat delay init:", self.sound_beat_delay)
            if DEBUG: print(f"(global variable delay: {global_variables.SOUND_BEAT_DELAY_INIT}", end=", ")
            if DEBUG: print(f"subtracted by offset: {self.sound_beat_delay_offset})")
            if DEBUG: print()

            """
            Play Sound
            """
            if self.sound_beat_1_or_2 == 1:
                self.sound_beat_1_or_2 = 2
                if self.sound:
                    self.sounds_player.play_sound_beat_1()
                # if not DEBUG: print("Playing sound beat 1...")

            if self.sound_beat_1_or_2 == 2:
                self.sound_beat_1_or_2 = 1
                if self.sound:
                    self.sounds_player.play_sound_beat_2()
                # if not DEBUG: print("Playing sound beat 2...")

    # sound beat delay methods
    def reset_sound_beat_delay(self):
        self.sound_beat_delay_offset = 0
        self.decrement_sound_beat_delay = True

    # High Scores file management
    def get_high_scores_file(self):
        line_contents = []

        # read
        with open(global_variables.HIGH_SCORES_FILENAME, 'r') as file:
            for line in file:
                print(line)
                line_contents.append(line)
        
        return line_contents
        
    def get_high_score_from_file(self):
        high_score      = 0
        _high_score_i    = 0
        line_contents   = self.get_high_scores_file()

        for i,line in enumerate(line_contents):

            line = line.split(',')
            line.append(i)

            print(line[1])
            if line[1] != '':
                if int(line[1]) > high_score:
                    high_score      = int(line[1])
                    _high_score_i    = i
        
        return int(high_score)

    def display_high_scores(self):
        hs_1 = 0
        hs_2 = 0
        hs_3 = 0

        hs_file_contents = self.get_high_scores_file()
        for i, line in enumerate(hs_file_contents):
            # if len(hs_file_contents) >= 3:
            index   = i
            name    = line[0]
            score   = line[1]
            print(f"index({index}) name({name}) score({score})")

            print("high score 1", hs_1)
            print("high score 2", hs_2)
            print("high score 3", hs_3)
            print()

    def write_high_score(self):
        # get name
        name = input("High score - Name: ")
        # get score
        score = self.score.score

        with open(global_variables.HIGH_SCORES_FILENAME, 'a') as file:
            file.write(f"{name},{score}\n")


# Creates the game and starts it going
window = Game(SCREEN_WIDTH, SCREEN_HEIGHT)
arcade.run()

