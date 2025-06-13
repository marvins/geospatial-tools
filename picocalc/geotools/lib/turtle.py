
#  Micropython Libraries
from enum import Enum
import framebuf

# PicoCalc Libraries
import picocalc 

class Key(Enum):
    '''
    This class is organized by the value of the first entry.  Note the keyboard API
    tends 
    '''
    Key_UNKNOWN    = (   0 )                 #  This should be an error condition
    Key_TAB        = (   9 )
    Key_ENTER      = (  13 )                 # Key:  Enter
    Key_ESCAPE     = (  27,  27 )            # Key:  Escape key
    Key_INSERT     = (  27,  73 )            # Key:  Insert
    Key_DELETE     = (  27,  91,  51, 126 )  # Key:  Delete
    Key_END        = (  27,  91,  70 )       # Key:  Home
    Key_HOME       = (  27,  91,  72 )       # Key:  Home
    Key_SPACE      = (  32 )                 # Key:  " " (Spacebar)
    Key_BANG       = (  33 )                 # Key:  !   (Exclaimation-Point)
    Key_DBQUOTE    = (  34 )                 # Key:  "   (Double-Quote)
    Key_HASH       = (  35 )                 # Key:  #   (Octothorpe)
    Key_DOLLAR     = (  36 )                 # Key:  $   (Dollar-Sign)
    Key_PERCENT    = (  37 )                 # Key:  %   (Percent)
    Key_AMPERSAND  = (  38 )                 # Key:  &   (Ampersand)
    Key_QUOTE      = (  39 )                 # Key:  '   (Single-Quote)
    Key_LPAREN     = (  40 )                 # Key:  (   (Left-Parenthesis)
    Key_RPAREN     = (  41 )                 # Key:  )   (Right-Parenthesis)
    Key_STAR       = (  42 )                 # Key:  *   (Star / Multiply)
    Key_PLUS       = (  43 )                 # Key:  +   (Plus-Sign)
    Key_COMMA      = (  44 )                 # Key:  ,   (Comma)
    Key_MINUS      = (  45 )                 # Key:  -   (Minus)
    Key_PERIOD     = (  46 )                 # Key:  .   (Period)
    Key_SLASH      = (  47 )
    Key_0          = (  48 )
    Key_1          = (  49 )
    Key_2          = (  50 )
    Key_3          = (  51 )
    Key_4          = (  52 )
    Key_5          = (  53 )
    Key_6          = (  54 )
    Key_7          = (  55 )
    Key_8          = (  56 )
    Key_9          = (  57 )
    Key_COLON      = (  58 )
    Key_SEMICOLON  = (  59 )
    Key_LANGLE     = (  60 )                # Key:  < (Left Angle-Bracket)
    Key_EQUAL      = (  61 )                # Key:  = (Equal Sign)
    Key_RANGLE     = (  62 )                # Key:  > (Right Angle-Bracket)
    Key_QUESTION   = (  63 )
    Key_AT         = (  64 )
    Key_LBRACKET   = (  91 )
    Key_BACKSLASH  = (  92 )
    Key_RBRACKET   = (  93 )                # Key: ] (Right-Bracket)
    Key_CARROT     = (  94 )                # Key: ^ (Carrot)
    Key_UNDERSCORE = (  95 )
    Key_TICK       = (  96 )
    Key_LBRACE     = ( 123 )                # Key: { (Left-Squigly-Brace)
    Key_PIPE       = ( 124 )
    Key_RBRACE     = ( 125 )
    Key_TILDE      = ( 126 )
    Key_BACK       = ( 127 )
    Key_F1         = ( 129 )
    Key_F2         = ( 130 )
    Key_F3         = ( 131 )
    Key_F4         = ( 132 )
    Key_F5         = ( 133 )
    Key_F6         = ( 134 )
    Key_F7         = ( 135 )
    Key_F8         = ( 136 )
    Key_F9         = ( 137 )
    Key_F10        = ( 144 )
    Key_CAPS_LOCK  = ( 193 )
    Key_BREAK      = ( 208 )

    @staticmethod
    def is_lowercase_letter( key ):
        return key >= 97 and key <= 122
    
    @staticmethod
    def is_uppercase_letter( key ):
        return key >= 65 and key <= 90
    
    @staticmethod
    def is_number( key ):
        return key >= 48 and key <= 57
    

    @staticmethod
    def is_letter( key ):
        return Key.is_uppercase_letter( key ) or Key.is_lowercase_letter( key )


    @staticmethod
    def pop_next( arr ):
        '''
        Given an array, pop the next key off, returning the key and the remainder of the array
        '''

        arr = list(arr)
        key = None

        current = []

        while len( arr ) > 0:

            # Get next key
            k = arr.pop(0)

            #  If we have 27, and previous value was 27, it's Escape
            if k == 27 and len(current) > 0 and current[-1] == 27:
                key = Key.Key_ESCAPE
                current = []
                break
            
            # Otherwise, if we have 27, then it's the start of a special key
            elif k == 27:
                current.append( k )
                continue

            #  Otherwise, if we don't have 27, and we have an active entry, check 
            elif len(current) > 0 and current[0] == 27:

                # Append to current variable
                current.append( k )
                temp = tuple(current)

                # Check if there is a match
                if temp == Key.Key_INSERT:
                    key = Key.Key_INSERT
                    break
                elif temp == Key.Key_DELETE:
                    key = Key.Key_DELETE
                    break
                elif temp == Key.Key_END:
                    key = Key.Key_END
                    break
                elif temp == Key.Key_HOME:
                    key = Key.Key_HOME
                    break
                else:
                    key = Key.Key_UNKNOWN
                    break
            
            # All single-value keys
            else:
                for k in Key:
                    print(k)


        return key, arr


class TurtleScreen:

    def __init__(self, display ):

        self.display = display

    def fill( self, color ):
        self.display.fill( color )

    def fill_rect( self, x, y, w, h, color ):
        self.display.fill_rect( x, y, w, h, color )

    def draw_text( self, text, x, y, color ):
        self.display.text( text, x, y, color )

    def show( self ):
        self.display.show()

    def log_info(self):

        print(self.display.getLUT())

def screensize():
    return (320,320)

def init( w, h, 
          format = framebuf.GS4_HMSB,
          skip_init = False ):

    disp = picocalc.PicoDisplay( w, h, 
                                 color_type = format,
                                 skip_init = skip_init )

    return TurtleScreen( disp )

def check_keyboard():

    output = []
    temp = bytearray(1)
    while picocalc.keyboard.readinto(temp):
        output.append( temp[0] )

    # Try to discern specific keys

    return output
