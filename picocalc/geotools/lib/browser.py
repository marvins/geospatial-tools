
#  Micropython Libraries
import os
import sys

#  Project Libraries
import colors
import turtle


def main( cdir ):
    
    sz = turtle.screensize()

    screen = turtle.init( sz[0], sz[1], skip_init = True )
    #screen.fill( colors.GS4.BLACK )


    while True:

        # Check for keyboard input
        keys = turtle.check_keyboard()
        print( 'keys: ', keys )


    #screen.draw_text("Hello PicoCalc!", 10, 310, 15)
    #screen.show()

    #  Put everything back
    screen.reset()
    

#  Sort out what directory to start with
start_dir = os.getcwd()
if len(sys.argv) > 0:
    start_dir = sys.argv[0]

main( start_dir )
