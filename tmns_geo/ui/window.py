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
#    File:    window.py
#    Author:  Marvin Smith
#    Date:    May 13, 2025
#
#    Purpose:  Wrapper for turtle that supports calculators
#


class Base:

    def __init__(self):

        self.border_gap = 5
        self.header_bbox = (self.border_gap,
                            self.border_gap,
                            self.ui.config.screen_size[0] - self.border_gap * 2,
                            25 )
        
