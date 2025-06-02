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
import ndarray as np

class Page:

    def __init__(self):
        self.widgets = []
        self.top_left = np.array( [0,0], dtype = int )

    def add_widget(self, new_widget):
        self.widgets.append( new_widget )

    def draw(self):

        latest_tl = self.top_left

        #  Iterate through each widget
        for widget in self.widgets:

            #  Draw the widget
            widget.draw( latest_tl )
            
            # Compute new top-left corner
            latest_tl[1] += widget.size()[1]

            if latest_tl[0] > 320 or latest_tl[1] > 240:
                break
        

class Widget:

    def __init__(self, *args, **kwargs):
        self.data = {}
        for arg in kwargs.keys():
            setattr( self, arg, kwargs[arg] )
        
        self.refresh_needed = True


class VBoxLayout( Widget ):

    def __init__(self, *args, **kwargs ):
        super().__init__(*args, **kwargs )

        self.widgets = []

    def add_widget( self, widget ):
        self.widgets.append( widget )

    def size(self):

        sz = np.array( [0,0], dtype = int )
        for widget in self.widgets:
            sz[0] = max( sz[0], widget.size()[0] )
            sz[1] += widget.size()[1]
        return sz

    def draw( self, tl ):

        current_tl = tl

        #  Iterate over each widget
        for widget in self.widgets:

            #  Draw the widget
            widget.draw( current_tl )

            #  Offset
            current_tl += np.array( [ 0, widget.size()[1] ],
                                    dtype = int )


class Label(Widget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs )

        if not hasattr(self, 'background_color'):
            self.background_color = Color.LIGHT_BLUE

    def size(self):
        return np.array( [300, 20], dtype = float )

    def draw(self, tl):

        if not self.refresh_needed:
            return
        
        #  Draw background
        sz = self.size()
        fill_rect( tl[0], tl[1],
                   sz[0], sz[1],
                   self.background_color )

        #  Draw the text
        draw_text( self.title,
                   tl[0] + 10,
                   tl[1] + sz[1] - 5 )
        
        self.refresh_needed = False


class Header(Widget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if not hasattr(self, 'background_color'):
            self.background_color = Color.DODGER_BLUE

    def size(self):
        return np.array( [300, 20], dtype = float )

    def draw(self, tl):

        if not self.refresh_needed:
            return
        
        #  Draw background
        sz = self.size()
        fill_rect( tl[0], tl[1],
                   sz[0], sz[1],
                   self.background_color )

        #  Draw the text
        draw_text( self.title,
                   tl[0] + 10,
                   tl[1] + sz[1] - 5 )
        
        self.refresh_needed = False

class Text_Input( Widget ):

    def __init__( self, *args, **kwargs ):
        super().__init__( *args, **kwargs )

        if not hasattr(self, 'label_bg_color'):
            self.label_bg_color = Color.LIGHT_GRAY
        if not hasattr(self, 'orientation'):
            self.orientation = 'lr'
    
    def label_width(self):
        return len(self.label_text) * 5 + 10
    
    def size(self):

        return np.array( [ self.label_width() + 100, 20 ],
                         dtype = int )
    
    def draw(self,tl):

        if not self.refresh_needed:
            return
        
        #-----------------------#
        #-      Draw Label     -#
        #-----------------------#
        #  Draw label background
        sz = self.size()
        fill_rect( tl[0], tl[1],
                   self.label_width() + 10, sz[1],
                   self.label_bg_color )

        #  Draw the text
        draw_text( self.label_text,
                   tl[0] + 5,
                   tl[1] + sz[1] - 5 )
        
        #-----------------------#
        #-      Draw Input     -#
        #-----------------------#
        #  Draw label background
        text_width = len(self.input_text) * 5
        box_width  = 100
        draw_rect( tl[0] + self.label_width() + 10, tl[1],
                   box_width,                       sz[1]-2 )

        #  Draw the text
        draw_text( self.input_text,
                   tl[0] + self.label_width() + 15,
                   tl[1] + sz[1] - 5 )

        self.refresh_needed = False
        
class Check_Box( Widget ):

    def __init__( self, *args, **kwargs ):
        super().__init__( *args, **kwargs )

        if not hasattr(self, 'checked'):
            self.checked = False
        if not hasattr(self, 'box_height'):
            self.box_height = 14
        if not hasattr(self, 'orientation'):
            self.orientation = 'lr'

    def size( self ):
        return np.array( [20,20], dtype = int )
    
    def draw(self, tl):

        if not self.refresh_needed:
            return
        
        #-----------------------#
        #-      Draw Label     -#
        #-----------------------#
        #  Draw label background
        sz = self.size()
        fill_rect( tl[0], tl[1],
                   self.label_width() + 10, sz[1],
                   self.label_bg_color )

        #  Draw the text
        draw_text( self.label,
                   tl[0] + 5,
                   tl[1] + sz[1] - 5 )

        #----------------------#
        #-      Draw Box      -#
        #----------------------#
        offset = tl
        if self.orientation == 'lr':
            offset[0] += self.size()[0]
            offset[1]  = max( offset[1], self.box_height )
        elif self.orientation == 'ud':
            offset[0]  = max( offset[0], self.box_height )
            offset[1] += self.size()[1]
        else:
            raise Exception( 'Unsupported Mode: ' + self.orientation )


        draw_rect( offset[0],
                   offset[1],
                   self.box_height,
                   self.box_height )
        
        if self.checked:
            draw_line( offset[0],
                       offset[1],
                       offset[0] + self.box_height,
                       offset[1] + self.box_height )
        
        self.refresh_needed = False
