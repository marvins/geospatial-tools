#**************************** INTELLECTUAL PROPERTY RIGHTS ****************************#
#*                                                                                    *#
#*                           Copyright (c) 2025 Terminus LLC                          *#
#*                                                                                    *#
#*                                All Rights Reserved.                                *#
#*                                                                                    *#
#*          Use of this source code is governed by LICENSE in the repo root.          *#
#*                                                                                    *#
#**************************** INTELLECTUAL PROPERTY RIGHTS ****************************#

#  TI Libraries
import ti_draw 
import ti_system

#  Project Libraries
from hal import *

class Page:

    def __init__(self):
        self.widgets = []

        self.top_left = [0,0]

    def add_widget(self, new_widget):
        self.widgets.append( new_widget )

    def draw(self):

        latest_tl = self.top_left

        #  Iterate through each widget
        for widget in self.widgets:

            #  Get it's size
            sz = widget.size

            # Compute this widget's top-left corner
            this_tl = [ latest_tl[0] + sz[0],
                        latest_tl[1] + sz[1] ]
            


class Widget:

    def __init__(self, *args, **kwargs):
        self.data = {}
        for arg in kwargs.keys():
            self.data[arg] = kwargs[arg]

class Label(Widget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs )


class Header(Widget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def draw(self):
        #  Get top-left corner