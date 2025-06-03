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
import coordinate
from hal import *
from utils import *

from ui import Button, Check_Box, HBoxLayout, Header, Label, Page, Text_Input, VBoxLayout

#  Configuration Values
max_loops = 20
screen_size = ti_draw.get_screen_dim()


def build_main_menu():

    page = Page()

    #  Add Header
    page.add_widget( Header( title = 'Converter',
                             show_time = True ) )
    
    #  Add Labels for options
    page.add_widget( Button( title   = '1) Coordinate Conversions',
                             hotkey  = '1',
                             retcode = 'coord' ) )
    page.add_widget( Button( title = '2) Time Conversions' ) )

    return page
    
def main_menu():

    page = build_main_menu()

    #  Run Primary Menu
    exit_app = False
    while not exit_app:
    
        #  Draw the UI
        page.draw()
        
        #  Run the "interrupt" loop until something interest
        for x in range( max_loops ):
      
            action = page.check_keyboard()
            
            if not action is None:
                if action == 'exit':
                    exit_app = True
                if action == 'coord':
                    action = coordinate.coord_converter()
                break
            else:
                sleep(0.1)
  
  
main_menu()