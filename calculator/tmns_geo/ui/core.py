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
#    File:    ui.py
#    Author:  Marvin Smith
#    Date:    May 13, 2025
#
#    Purpose:  Basic UI Runner
#

#  Python Standard Libraries
import time

#  Project Libraries
from tmns_geo.geo_convert import Geo_Convert
from tmns_geo.main_menu   import Main_Menu

class UI:

    def __init__(self, config):
        self.config = config
        self.okay_to_run = True
        self.redraw = True

        self.id = 0

        self.apps = [ Main_Menu( self ),
                      Geo_Convert( self ) ]

    def show(self):

        iters = 0
        while self.okay_to_run:

            if self.redraw:
                self.apps[self.id].render()
            
            # sleep for a period
            time.sleep( self.config.sleep_time )

            iters += 1

            if iters > 10000:
                break
            
        
