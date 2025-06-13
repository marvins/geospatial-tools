
#  Project Libraries
import turtle

def run():
    
    sz = turtle.screensize()

    screen = turtle.init( sz[0], sz[1], skip_init = True )
    #screen.fill( colors.GS4.BLACK )

    while True:

        # Check for keyboard input
        keys = turtle.check_keyboard()
        if len(keys) > 0:
            print( 'keys: ', keys )

    #  Put everything back
    screen.reset()
    


