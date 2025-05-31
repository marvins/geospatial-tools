#**************************** INTELLECTUAL PROPERTY RIGHTS ****************************#
#*                                                                                    *#
#*                           Copyright (c) 2025 Terminus LLC                          *#
#*                                                                                    *#
#*                                All Rights Reserved.                                *#
#*                                                                                    *#
#*          Use of this source code is governed by LICENSE in the repo root.          *#
#*                                                                                    *#
#**************************** INTELLECTUAL PROPERTY RIGHTS ****************************#

class Color:

    BLACK       = (   0,   0,   0 )
    BLUE        = (   0,   0, 255 )
    DODGER_BLUE = (  30, 144, 255 )
    GRAY        = ( 125, 125, 125 )
    LIGHT_BLUE  = ( 226, 234, 244 )
    LIGHT_GRAY  = ( 200, 200, 200 )
    RED         = ( 255,   0,   0 )
    USAF_BLUE   = (   0,  48, 143 )
    WHITE       = ( 255, 255, 255 )

def format_time( input, fmt_str = '' ):
    (year, mon, day, hour, min, sec, ns, yday, dst ) = input

    #  pop chars off
    return '{:02}:{:02}:{:02}'.format(hour,min,sec)
