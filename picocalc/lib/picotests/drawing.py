
#  Micropython Libraries
import logging
import time

#  Project Libraries
import colors
import turtle

#  Run Test
def run( log_level = logging.DEBUG,
         log_path  = './browser.log' ):
    
    #  Setup Logger
    if not log_path is None:
        logging.basicConfig( level    = log_level,
                             filename = log_path )
    else:
        logging.basicConfig( level = log_level )
    logging.info( 'Logging initialized' )

    #  Setup the Turtle Display
    screen = turtle.init()
    screen.fill( colors.GS4.BLACK )

    screen.wait_update_finished()
    screen.draw_text( "PicoCalc Filesystem Browser", 10, 10, colors.GS4.GREEN )

    #while True:
    #
    #    # Check for keyboard input
    #    keys = turtle.check_keyboard()
    #    
    #    for key in keys:
    #        if key == turtle.Key.ESCAPE:
    #            screen.draw_text("Hello PicoCalc!", 10, 310, 15, colors.GS4.GREEN )
    #            break
    #
    #    time.sleep(0.1)
    time.sleep(5)

    #screen.draw_text("Hello PicoCalc!", 10, 310, 15)
    #screen.show()

    #  Put everything back
    screen.reset()

    logging.debug( 'Exiting Application' )