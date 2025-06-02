#**************************** INTELLECTUAL PROPERTY RIGHTS ****************************#
#*                                                                                    *#
#*                           Copyright (c) 2025 Terminus LLC                          *#
#*                                                                                    *#
#*                                All Rights Reserved.                                *#
#*                                                                                    *#
#*          Use of this source code is governed by LICENSE in the repo root.          *#
#*                                                                                    *#
#**************************** INTELLECTUAL PROPERTY RIGHTS ****************************#

from ui import Check_Box, Header, Label, Page, Text_Input, VBoxLayout

def main():

    #  Create a page
    page = Page()

    #  Add Header
    page.add_widget( Header( title = 'Demo App',
                             show_time = True ) )

    #----------------------------------------------------#
    #-          Geographic Coordinate Widget            -#
    #----------------------------------------------------#
    page.add_widget( Label( title = 'Geographic' ) )

    page.add_widget( Text_Input( label_text  = 'Lat (deg): ',
                                 input_text  = '0',
                                 orientation = 'ud' ) )
    
    page.add_widget( Text_Input( label_text  = 'Lon (deg): ',
                                 input_text  = '0',
                                 orientation = 'ud' ) )
    
    #  Format Layout
    fmt_vbox = VBoxLayout()
    fmt_vbox.add_widget( Label( title = 'Format' ) )
    fmt_vbox.add_widget( Check_Box( label = 'Degrees', checked = False ) )
    fmt_vbox.add_widget( Check_Box( label = 'Radians', checked = False ) )

    page.add_widget( fmt_vbox )

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

    page.draw()

main()
