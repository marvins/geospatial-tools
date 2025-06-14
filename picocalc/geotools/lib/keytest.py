
#  Project Libraries
import turtle

def run():
    
    sz = turtle.screensize()

    screen = turtle.init( sz[0], sz[1], skip_init = True )
    #screen.fill( colors.GS4.BLACK )

    okay_to_run = True
    while okay_to_run:

        # Check for keyboard input
        keys = turtle.check_keyboard()
        if len(keys) > 0:
            for key in keys:
                print( 'Key: ', key, ', Mapped Value: ', turtle.KEYMAP[key] )

                if key == turtle.Key.ESCAPE:
                    print('Exiting Application')
                    okay_to_run = False
                    break

    #  Put everything back
    screen.reset()
    


