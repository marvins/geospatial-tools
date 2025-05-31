#**************************** INTELLECTUAL PROPERTY RIGHTS ****************************#
#*                                                                                    *#
#*                           Copyright (c) 2025 Terminus LLC                          *#
#*                                                                                    *#
#*                                All Rights Reserved.                                *#
#*                                                                                    *#
#*          Use of this source code is governed by LICENSE in the repo root.          *#
#*                                                                                    *#
#**************************** INTELLECTUAL PROPERTY RIGHTS ****************************#

#  TI Libraries
import ti_draw 
import ti_system

#  Project Libraries
from utils import Color

app_config = { 'screen_size':   [320,240],
               'axes_centered': False,
               'swap_y_axes':   True }

def init_screen( **kwargs ):
    '''
    Initialize the screen.
    - For the TI Nspire, this is a no-op
    '''
    pass

def draw_text( text, x, y, color = Color.BLACK ):
    ti_draw.set_color( color[0], color[1], color[2] )
    ti_draw.draw_text( x, y, text )


def fill_rect( x, y, w, h, color ):
    ti_draw.set_color( color[0], color[1], color[2] )
    ti_draw.fill_rect( x, y, w, h )


def draw_rect( x, y, w, h, **kwargs ):
    '''
    Draw a rectangle and place on screen
    '''

    if 'line_color' in kwargs.keys():
        color = kwargs['line_color']
        ti_draw.set_color( color[0], color[1], color[2] )

    ti_draw.draw_rect( x, y, w, h )



def get_keys():
    
    keys = []
    while True:
        k = ti_system.get_key()
        if len(k) < 1:
            return keys
        keys.append(k)
