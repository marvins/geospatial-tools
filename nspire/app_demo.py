#**************************** INTELLECTUAL PROPERTY RIGHTS ****************************#
#*                                                                                    *#
#*                           Copyright (c) 2025 Terminus LLC                          *#
#*                                                                                    *#
#*                                All Rights Reserved.                                *#
#*                                                                                    *#
#*          Use of this source code is governed by LICENSE in the repo root.          *#
#*                                                                                    *#
#**************************** INTELLECTUAL PROPERTY RIGHTS ****************************#

from ui import Check_Box, HBoxLayout, Header, Label, Page, Text_Input, VBoxLayout

from time import sleep

def build_gui():

    #  Create a page
    page = Page()

    #  Add Header
    page.add_widget( Header( title = 'Demo App',
                             show_time = True ) )

    #----------------------------------------------------#
    #-          Geographic Coordinate Widget            -#
    #----------------------------------------------------#
    page.add_widget( Label( title = 'Geographic' ) )

    hbox = HBoxLayout()

    # Input Layout
    inp_vbox = VBoxLayout()
    inp_vbox.add_widget( Text_Input( label_text  = 'Lat (deg): ',
                                     input_text  = '0',
                                     orientation = 'ud' ) )
    
    inp_vbox.add_widget( Text_Input( label_text  = 'Lon (deg): ',
                                     input_text  = '0',
                                     orientation = 'ud' ) )
    hbox.add_widget( inp_vbox )
    
    #  Format Layout
    fmt_vbox = VBoxLayout()
    fmt_vbox.add_widget( Label( title = 'Format' ) )
    fmt_vbox.add_widget( Check_Box( label = 'Degrees', checked = True ) )
    fmt_vbox.add_widget( Check_Box( label = 'Radians', checked = False ) )

    hbox.add_widget( fmt_vbox )

    page.add_widget( hbox )

    #----------------------------------------------------#
    #-              UTM Coordinate Widget               -#
    #----------------------------------------------------#
    page.add_widget( Label( title = 'UTM' ) )

    #  Add Input Widgets
    page.add_widget( Text_Input( label_text  = 'Easting (m)',
                                 input_text  = '0',
                                 orientation = 'lr' ) )
    
    page.add_widget( Text_Input( label_text  = 'Northing (m)',
                                 input_text  = '0',
                                 orientation = 'lr' ) )
    
    page.add_widget( Text_Input( label_text  = 'Elev (m)',
                                 input_text  = '0',
                                 orientation = 'lr' ) )
    
    #----------------------------------------------------#
    #-             ECEF Coordinate Widget               -#
    #----------------------------------------------------#
    page.add_widget( Label( title = 'ECEF' ) )

    page.add_widget( Text_Input( label_text  = 'X (m): ',
                                 input_text  = '0',
                                 orientation = 'lr' ) )
    
    page.add_widget( Text_Input( label_text  = 'Y (m): ',
                                 input_text  = '0',
                                 orientation = 'lr' ) )
    
    page.add_widget( Text_Input( label_text  = 'Z (m): ',
                                 input_text  = '0',
                                 orientation = 'lr' ) )

    return page

def main():

    page = build_gui()

    while True:

        page.draw()

        action = page.check_keyboard()

        if not action is None:
            if action == 'exit':
                break
        else:
            sleep(0.1)
        

main()
