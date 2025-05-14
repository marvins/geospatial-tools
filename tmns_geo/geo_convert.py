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
#    File:    geo_convert.py
#    Author:  Marvin Smith
#    Date:    May 13, 2025
#
#    Purpose:  Wrapper for turtle that supports calculators
#

#  Project Libraries
from tmns_geo.ui.window import Base


class Geo_Convert( Base ):

    def __init__(self, ui):

        self.ui = ui

        self.header_bg_color = (226,234,244)

        #  Initialize Parent
        super().__init__()

    def render(self):

        #  Blank header
        self.draw_header()

    
    def draw_header(self):

        #k.fill_rect( 0, 
        #             0,
        #             self.ui.config.screen_size[0], 
        #             self.ui.config.screen_size[1],
        #             (255,255,255) )
        
        k.fill_rect( self.header_bbox[0],
                     self.header_bbox[1],
                     self.header_bbox[2],
                     self.header_bbox[3],
                     self.header_bg_color )
        
        k.draw_string( 'Coordinate Converter',
                       20, 10,
                       (0,0,0),
                       self.header_bg_color,
                       True ) 

