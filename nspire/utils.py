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

    BLACK      = (   0,   0,   0 )
    BLUE       = (   0,   0, 255 )
    LIGHT_BLUE = ( 226, 234, 244 )
    RED        = ( 255,   0,   0 )
    WHITE      = ( 255, 255, 255 )

def format_time( input, fmt_str = '' ):
    (year, mon, day, hour, min, sec, ns, yday, dst ) = input

    #  pop chars off
    return '{:02}:{:02}:{:02}'.format(hour,min,sec)
