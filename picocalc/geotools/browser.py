
#  Micropython Libraries
import os
import sys

#  Project Libraries
import colors
import turtle


def main( cdir ):
    
    sz = turtle.screensize()

    screen = turtle.init( sz[0], sz[1] )
    screen.fill( colors.RGB_585.GREEN )

    # Draw 16 color bars, dark to light
    for x in range( 8 ):
        r = 0
        g = 0
        b = int(255 * float(x) / 7)

        screen.fill_rect( 0, 40 * x, 
                          sz[0], sz[1] / 8,
                           )

    screen.draw_text("Hello PicoCalc!", 10, 310, 15)
    screen.show()

    screen.log_info()

#  Sort out what directory to start with
start_dir = os.getcwd()
if len(sys.argv) > 0:
    start_dir = sys.argv[0]

main( start_dir )