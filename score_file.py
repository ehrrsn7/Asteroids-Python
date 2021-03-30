"""
File: score.py
Name: Elijah Harrison

Class:      CS 241
Instructor: Brother Mellor
"""

# import
import point_file, on_screen_text_file
import global_variables_directory as global_variables

# define
# n/a

"""
Class: Score

(https://www.ign.com/faqs/2003/3-d-asteroids-general-faq-430472)
Scoring in this game is pretty simple:

Large Asteroids:     20 points
Medium Asteroids:    50 points
Small Asteroids:    100 points
Large Saucer:       200 points
Small Saucer:      1000 points.

On the normal machine set up, you earn a 
free spaceship every 10,000 points.
"""
class Score(on_screen_text_file.On_Screen_Text):
    def __init__(self):
        super().__init__()

        # center point
        x       = global_variables.SCORE_X
        y       = global_variables.SCORE_Y
        self.p  = point_file.Point(x, y)

        # score count (int)
        self.score      = global_variables.SCORE_INIT

        # display text (bool)
        self.display_text = True


    """
    Text
    """
    @property
    def text(self): return f"Score: {self.score}"

    """
    Operators
    """
    # +=
    def __iadd__(self, rhs: int): self.score += rhs
    def __isub__(self, rhs: int): self.score -= rhs

