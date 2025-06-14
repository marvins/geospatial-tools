
#  Project Libraries
import turtle

def run():
    
    okay_to_run = True
    while okay_to_run:

        # Check for keyboard input
        keys = turtle.check_keyboard()
        if len(keys) > 0:
            for key in keys:
                
                #. Get the mapped key
                print( 'Detected: ', key, ', Key: ', turtle.Key.to_key( key ) )

                if key == turtle.Key.ESCAPE:
                    print('Exiting Application')
                    okay_to_run = False
                    break

