#**************************** INTELLECTUAL PROPERTY RIGHTS ****************************#
#*                                                                                    *#
#*                           Copyright (c) 2025 Terminus LLC                          *#
#*                                                                                    *#
#*                                All Rights Reserved.                                *#
#*                                                                                    *#
#*          Use of this source code is governed by LICENSE in the repo root.          *#
#*                                                                                    *#
#**************************** INTELLECTUAL PROPERTY RIGHTS ****************************#

#  Python Libraries
from time import *

#  TI Libraries
import ti_draw
import ti_system

#  Project Libraries
from hal import *
from utils import *


#  Configuration Values
max_loops = 20
screen_size = ti_draw.get_screen_dim()


def main_menu():

  #  Run Primary Menu
  exit_app = False
  while not exit_app:
    
    #  Draw the header
    ti_draw.clear()
    fill_rect( 5, 5, screen_size[0]-10, 35, Color.LIGHT_BLUE )
    draw_text( '    Converter       Time:  ' + format_time(localtime()) , 5, 30 )
    
    #  Draw Menu Options
    draw_rect( 5, 40, screen_size[0]-10, 25, line_color = Color.BLACK )
    draw_text( '    1)  Coordinate Conversions', 5, 60 )

    draw_rect( 5, 65, screen_size[0]-10, 25, line_color = Color.BLACK )
    draw_text( '    2)  Time Conversions', 5, 85 )

    draw_rect( 5, 90, screen_size[0]-10, 25, line_color = Color.BLACK )
    draw_text( ' esc)  Exit Application', 5, 110 )
    
    #  Run the "interrupt" loop until something interest
    for x in range( max_loops ):
  
        #  Fetch 
        keys = get_keys()
        if len(keys) > 0:
            for k in keys:
                if k == 'esc':
                    exit_app = True
                    break
            
                elif k == '1':
                    action = coordinate.coord_converter()
                    if action == 'exit':
                       return
                    break

                else:
                    print('Key Pressed: ', k)
        else:
            sleep(0.1)
        
        if x > (max_loops-1):
            exit_app = True
  
  
main_menu()