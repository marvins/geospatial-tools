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
        self.active = None
        self.input_list = []

    def add_widget(self, new_widget):
        self.widgets.append( new_widget )

        #  Update the input focus list
        if new_widget.is_input:
            self.input_list.append( len( self.widgets ) - 1 )

            if self.active is None:
                self.active = 0
                self.widgets[self.input_list[-1]].is_active = True

    def draw(self, force_draw = False ):

        latest_tl = self.top_left.clone()

        if force_draw:
            ti_draw.clear()

        #  Iterate through each widget
        for widget in self.widgets:

            #  Draw the widget
            widget.draw( latest_tl, force_draw )
            
            # Compute new top-left corner
            latest_tl[1] += widget.size()[1]

            if latest_tl[0] > 320 or latest_tl[1] > 240:
                break
    
    def check_keyboard(self):

        #  Check for keys
        action = None
        while True:
            keys = get_keys()
            for k in keys:
                for widget in self.widgets:
                    action = widget.check_keyboard( k )
                    if not action is None:
                        return action
                if k == 'esc':
                    return 'exit'
                elif k == 'down':
                    self.increment_focus()
                elif k == 'up':
                    self.decrement_focus()
    
    def increment_focus(self):

        if len(self.input_list) < 2:
            return
        
        old_id = self.input_list[self.active]
        self.active = (self.active + 1) % len(self.input_list)
        new_id = self.input_list[self.active]

        self.widgets[old_id].is_active = False
        self.widgets[new_id].is_active = True

        #  Redraw both widgets
        self.widgets[old_id].refresh_needed = True
        self.widgets[new_id].refresh_needed = True
    

    def decrement_focus(self):

        if len(self.input_list) < 2:
            return
        
        old_id = self.input_list[self.active]
        self.active = self.active - 1
        if self.active < 0:
            self.active = len(self.input_list-1)
        new_id = self.input_list[self.active]

        self.widgets[old_id].is_active = False
        self.widgets[new_id].is_active = True

        #  Redraw both widgets
        self.widgets[old_id].refresh_needed = True
        self.widgets[new_id].refresh_needed = True

class Widget:

    def __init__(self, *args, **kwargs):
        self.data = {}
        for arg in kwargs.keys():
            setattr( self, arg, kwargs[arg] )
        if not hasattr( self, 'is_input' ):
            self.is_input = False
        
        self.refresh_needed = True
    
    def check_keyboard( self, key ):
        pass

class BaseLayout( Widget ):

    def __init__(self, *args, **kwargs ):
        super().__init__(*args, **kwargs )
        self.widgets = []

    def add_widget( self, widget ):
        self.widgets.append( widget )

class HBoxLayout( BaseLayout ):

    def __init__(self, *args, **kwargs ):
        super().__init__(*args, **kwargs )

    def size(self):
        sz = np.array( [0,0], dtype = int )
        for widget in self.widgets:
            sz[0] += widget.size()[0]
            sz[1] = max( sz[1], widget.size()[1] )
        return sz

    def draw( self, tl, force_draw = False ):

        current_tl = tl.clone()

        #  Iterate over each widget
        for widget in self.widgets:

            #  Draw the widget
            widget.draw( current_tl, force_draw )

            #  Offset
            current_tl[0] += widget.size()[0]

class VBoxLayout( BaseLayout ):

    def __init__(self, *args, **kwargs ):
        super().__init__(*args, **kwargs )

    def size(self):
        sz = np.array( [0,0], dtype = int )
        for widget in self.widgets:
            sz[0] = max( sz[0], widget.size()[0] )
            sz[1] += widget.size()[1]
        return sz

    def draw( self, tl, force_draw = False ):

        current_tl = tl.clone()

        #  Iterate over each widget
        for widget in self.widgets:

            #  Draw the widget
            widget.draw( current_tl, force_draw )

            #  Offset
            current_tl[1] += widget.size()[1]


class Label(Widget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs )

        if not hasattr(self, 'background_color'):
            self.background_color = Color.LIGHT_BLUE

    def size(self):
        return np.array( [300, 20], dtype = float )

    def draw(self, tl, force_draw = False ):

        if force_draw == False and self.refresh_needed == False:
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

    def draw( self, tl, force_draw = False ):

        if force_draw == False and self.refresh_needed == False:
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
        if not hasattr(self, 'text_offset' ):
            self.text_offset = 8
        if not hasattr(self, 'input_width' ):
            self.input_width = 100
        self.is_input = True
        if not hasattr(self,'is_active'):
            self.is_active = False
        
    
    def label_width(self):
        return len(self.label_text) * 6 + 10
    
    def size(self):

        return np.array( [ self.label_width() + self.input_width, 20 ],
                         dtype = int )
    
    def draw( self, tl, force_draw = False ):

        if force_draw == False and self.refresh_needed == False:
            return
        
        #-----------------------#
        #-      Draw Label     -#
        #-----------------------#
        #  Draw label background
        sz = self.size()
        fill_rect( tl[0], tl[1],
                   self.label_width(), sz[1],
                   self.label_bg_color )

        #  Draw the text
        draw_text( self.label_text,
                   tl[0] + 5,
                   tl[1] + sz[1] - 5 )
        
        #-----------------------#
        #-      Draw Input     -#
        #-----------------------#
        #  Draw label background
        start_input_x = tl[0] + self.label_width()
        draw_rect( start_input_x, 
                   tl[1],
                   self.input_width - 1, sz[1]-2 )

        #  Draw the text
        draw_text( self.input_text,
                   start_input_x + self.text_offset,
                   tl[1] + sz[1] - 5 )

        self.refresh_needed = False

class Button( Widget ):

    def __init__( self, *args, **kwargs ):
        super().__init__( *args, **kwargs )

        if not hasattr(self, 'padding'):
            self.padding = 4
        if not hasattr(self, 'bg_color'):
            self.button_color = Color.LIGHT_GRAY
        
        self.is_input = True
        if not hasattr(self,'is_active'):
            self.is_active = False

    def size( self ):
        return np.array( [300, 30], dtype = float )
    
    def draw( self, tl, force_draw = False ):

        if force_draw == False and self.refresh_needed == False:
            return
        
        #  box needs to be smaller by the padding amount
        sz = self.size()
        
        fill_rect( tl[0] + self.padding, tl[1] + self.padding,
                   sz[0] - self.padding * 2,
                   sz[1] - self.padding * 2,
                   self.button_color )
        
        #  Color depends if active
        line_color = Color.GRAY
        if self.is_active:
            line_color = Color.BLACK

        draw_rect( tl[0] + self.padding, tl[1] + self.padding,
                   sz[0] - self.padding * 2,
                   sz[1] - self.padding * 2,
                   line_color = line_color )
        

        #  Draw the text
        draw_text( self.title,
                   tl[0] + self.padding + 5,
                   tl[1] + sz[1] - self.padding - 5 )

        
        self.refresh_needed = False

    def check_keyboard(self, key):
        
        if hasattr( self, 'hotkey' ):
            if key == self.hotkey:
                return self.retcode

class Check_Box( Widget ):

    def __init__( self, *args, **kwargs ):
        super().__init__( *args, **kwargs )

        if not hasattr(self, 'checked'):
            self.checked = False
        if not hasattr(self, 'box_height'):
            self.box_height = 14
        if not hasattr(self, 'label_bg_color'):
            self.label_bg_color = Color.LIGHT_GRAY
        if not hasattr(self, 'orientation'):
            self.orientation = 'lr'
        self.is_input = True
        if not hasattr(self,'is_active'):
            self.is_active = False

    def label_width(self):
        return len(self.label) * 5 + 10
    
    def size( self ):
        
        x = self.label_width() + 20
        return np.array( [x,20], dtype = int )
    
    def draw( self, tl, force_draw = False ):

        if force_draw == False and self.refresh_needed == False:
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
        offset = tl.clone()
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
            draw_line( offset[0] + self.box_height,
                       offset[1],
                       offset[0],
                       offset[1] + self.box_height )
        
        self.refresh_needed = False


            