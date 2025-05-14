#**************************** INTELLECTUAL PROPERTY RIGHTS ****************************#
#*                                                                                    *#
#*                           Copyright (c) 2025 Terminus LLC                          *#
#*                                                                                    *#
#*                                All Rights Reserved.                                *#
#*                                                                                    *#
#*          Use of this source code is governed by LICENSE in the repo root.          *#
#*                                                                                    *#
#**************************** INTELLECTUAL PROPERTY RIGHTS ****************************#
#
#    File:    draw.py
#    Author:  Marvin Smith
#    Date:    May 13, 2025
#
#    Purpose:  Wrappers around non Turtle drawing calls
#
import kandinsky as k
import ion

def fill_rect( startX, startY, width, height, color ):
    '''
    Draw and fill-in a rectangle on the screen
    '''
    k.fill_rect( startX, startY, width, height, color )


def draw_string( text, startX, startY, textColor, bgColor, fontSize ):
    '''
    Draw a string onto the screen
    '''
    k.draw_string( text, startX, startY, textColor, bgColor, fontSize )
