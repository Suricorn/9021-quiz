# Written by *** for COMP9021
#
# At stage 0, start with a toothpick centered at (0, 0).
# There is a free tip at the top, at coordinates (0, 2),
# and a free tip at the bottom, at coordinates (0, -2):
# 
#         *
#         *
#         *
#         *
#         *
#         
# At stage 1, perpendically place toothpicks on those tips.
# So there are now 3 toothpicks and 4 free tips,
# a top left one at coordinates (-2, 2),
# a top right one at coordinates (2, 2),
# a bottom left one at coordinates (-2, -2), and
# a bottom right one at coordinates (2, -2):
# 
#     * * * * *
#         *
#         *
#         *
#     * * * * *
#     
# At stage 2, perpendically place toothpicks on those tips.
# So there are now 7 toothpicks and 4 free tips,
# a top left one at coordinates (-2, 4),
# a top right one at coordinates (2, 4),
# a bottom left one at coordinates (-2, -4), and
# a bottom right one at coordinates (2, -4):
# 
# 
#     *       * 
#     *       *
#     * * * * *
#     *   *   *
#     *   *   *
#     *   *   *
#     * * * * *
#     *       *
#     *       *
# 
# Implements a function
# tooth_picks(stage, top_left_corner, bottom_right_corner)
# that displays, using black and white squares,
# that part of the plane that fits in a rectangle
# whose top left and bottom right corners are provided by the
# second and third arguments, respectively, at the stage of the
# construction provided by the first argument.
# You can assume that stage is any integer between 0 and 1000;
# top_left_corner and bottom_right_corner are arbitrary pairs
# of integers, but practically such that the output can fit
# on the screen.
# 
# For a discussion about the construction, see
# https://www.youtube.com/watch?v=_UtCli1SgjI&t=66s
# The video also points to a website that you might find useful:
# https://oeis.org/A139250/a139250.anim.html


def tooth_picks(stage, top_left_corner, bottom_right_corner):
    pass
    # REPLACE PASS WITH YOUR CODE

# POSSIBLY DEFINE OTHER FUNCTIONS
