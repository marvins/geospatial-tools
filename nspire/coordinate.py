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

#  Project Libraries
from hal   import *
from utils import *

#  Global Values
screen_size = ti_draw.get_screen_dim()

#  Enumerations
TYPE_ECEF    = 0
TYPE_GEO_DD  = 1
TYPE_GEO_DM  = 2
TYPE_GEO_DMS = 3
TYPE_UTM     = 4

INPUT_WOUNDS = { TYPE_ECEF:    3,
                 TYPE_GEO_DD:  3,
                 TYPE_GEO_DM:  6,
                 TYPE_GEO_DMS: 8 }

#------------------------------------#
#-      Convert Type to String      -#
#------------------------------------#
def type_to_string( tp ):
    if tp == TYPE_ECEF:
        return 'Earth-Centered, Earth-Fixed'
    if tp == TYPE_GEO_DD:
        return 'Geographic, Decimal-Degrees'
    if tp == TYPE_GEO_DM:
        return 'Geographic, Degree-Minutes'
    if tp == TYPE_GEO_DMS:
        return 'Geographic, Degree-Minute-Seconds'
    if tp == TYPE_UTM:
        return 'Universal Transverse Mercator'
    
    raise Exception('Unsupported')


class Base:
    '''
    Base Coordinate Type
    '''
  
    def __init__(self):
        pass

class ECEF(Base):

    def __init__( self ):
        self.x = ''
        self.y = ''
        self.z = ''


class Geo(Base):
    '''
    Geographic Coordinate System
    '''
  
    def __init__( self ):
        self.lat_deg = ''
        self.lon_deg = ''
        self.elev_m  = ''

        super().__init__(self)


class UTM(Base):

    def __init__( self ):
        self.grid_zone  = ''
        self.hemisphere = ''
        self.easting    = ''
        self.northing   = ''
        self.elev_m     = ''

class Factory:

    @staticmethod
    def create( tp ):
        if tp == TYPE_ECEF:
            return ECEF()
        if tp == TYPE_UTM:
            return UTM()
        return Geo()

#---------------------------------#
#-       Geographic Input        -#
#---------------------------------#
def geo_dd_input( start_y, coord ):

    #  Latitude Input
    draw_rect( 15, start_y + 20, 50, 20, Color.GRAY )

    #  Longitude Input
    draw_rect( 100, start_y + 20, 50, 20, Color.GRAY )

def geo_dm_input( start_y, coord ):
    pass

def geo_dms_input( start_y, coord ):
    pass

#---------------------------------#
#-           UTM Input           -#
#---------------------------------#
def utm_input( start_y, coord ):
    
    #  Grid-Zone Input
    fill_rect( 10, start_y + 1, 80, 20, Color.GRAY )
    draw_text( 'Grid-Zone: ', 15, start_y + 18 )

    draw_rect( 95, start_y + 1, 100, 20, line_color = Color.GRAY )
    draw_text( coord.grid_zone, 100, start_y + 18 )

    #  Easting Input
    fill_rect( 10, start_y + 21, 75, 20, Color.LIGHT_GRAY )
    draw_text( 'East (m): ', 18, start_y + 38 )

    draw_rect( 90, start_y + 21, 120, 20, line_color = Color.LIGHT_GRAY )
    draw_text( coord.easting, 85, start_y + 35 )

    #  Northing Input
    fill_rect( 10, start_y + 41, 50, 20, Color.LIGHT_GRAY )
    draw_text( 'North (m): ', 18, start_y + 58 )

    draw_rect( 90, start_y + 41, 120, 20, line_color = Color.LIGHT_GRAY )
    draw_text( coord.northing, 85, start_y + 55 )

    #  Elevation Input
    fill_rect( 10, start_y + 61, 50, 20, Color.LIGHT_GRAY )
    draw_text( 'Z (m): ', 18, start_y + 78 )

    draw_rect( 90, start_y + 61, 120, 20, line_color = Color.LIGHT_GRAY )
    draw_text( coord.elev_m, 85, start_y + 75 )
    
#---------------------------------#
#-           ECEF Input          -#
#---------------------------------#
def ecef_input( start_y, coord ):
    
    #  X Input
    fill_rect( 10, start_y + 1, 50, 20, Color.LIGHT_GRAY )
    draw_text( 'X (m): ', 18, start_y + 18 )

    draw_rect( 75, start_y + 1, 120, 20, line_color = Color.LIGHT_GRAY )
    draw_text( coord.x, 85, start_y + 15 )

    #  Y Input
    fill_rect( 10, start_y + 21, 50, 20, Color.LIGHT_GRAY )
    draw_text( 'Y (m): ', 18, start_y + 38 )

    draw_rect( 75, start_y + 21, 120, 20, line_color = Color.LIGHT_GRAY )
    draw_text( coord.y, 85, start_y + 35 )

    #  Z Input
    fill_rect( 10, start_y + 41, 50, 20, Color.LIGHT_GRAY )
    draw_text( 'Z (m): ', 18, start_y + 58 )

    draw_rect( 75, start_y + 41, 120, 20, line_color = Color.LIGHT_GRAY )
    draw_text( coord.z, 85, start_y + 55 )


INPUT_MAP = { TYPE_ECEF:    ecef_input,
              TYPE_GEO_DD:  geo_dd_input,
              TYPE_GEO_DM:  geo_dm_input,
              TYPE_GEO_DMS: geo_dms_input,
              TYPE_UTM:     utm_input }

#--------------------------------------------#
#-          Coordinate Input Menu           -#
#--------------------------------------------#
def coord_input_menu( coord_types ):

    focus_widget = 0

    input_coord  = Factory.create( coord_types[0] )
    output_coord = Factory.create( coord_types[1] )

    #  Iterate over input and output
    redraw_all = True
    while True:

        #  Draw the header
        if redraw_all:
            ti_draw.clear()
        
        fill_rect( 5, 5, screen_size[0]-10, 35, Color.DODGER_BLUE )
        draw_text( '    Coordinate Conversions   Time:  ' + format_time(localtime()) , 5, 30 )


        #------------------------------------#
        #-          Input Coordinate        -#
        #------------------------------------#
        fill_rect( 5, 30, screen_size[0]-10, 20, Color.LIGHT_BLUE )
        draw_text( '       ' + type_to_string( coord_types[0] ), 5, 48 )
        draw_rect( 5, 50, screen_size[0]-10, 64, line_color = Color.LIGHT_GRAY )

        INPUT_MAP[coord_types[0]]( 50, input_coord )

        #------------------------------------#
        #-          Output Coordinate       -#
        #------------------------------------#
        fill_rect( 5, 115, screen_size[0]-10, 20, Color.LIGHT_BLUE )
        draw_text( '       ' + type_to_string( coord_types[1] ), 5, 131 )
        draw_rect( 5, 135, screen_size[0]-10, 64, line_color = Color.LIGHT_GRAY )
        
        INPUT_MAP[coord_types[1]]( 138, output_coord )

        #  Run the "interrupt" loop until something interest
        okay_to_run = True
        while okay_to_run:

            #  Fetch keys received
            keys = get_keys()
            if len(keys) > 0:
                for k in keys:

                    #  Exit Menu
                    if k == 'esc':
                        return None

                    else:
                        print('Key Pressed: ', k)
            else:
                sleep(0.1)


#--------------------------------------------#
#-        Menu for Geographic Coordinate    -#
#--------------------------------------------#
def geographic_menu():
    
    #  Draw the header
    ti_draw.clear()
    fill_rect( 5, 5, screen_size[0]-10, 35, Color.DODGER_BLUE )
    draw_text( '    Coordinate Conversions   Time:  ' + format_time(localtime()) , 5, 30 )

    # Draw the Content
    draw_rect( 5, 40, screen_size[0]-10, 25, line_color = Color.BLACK )
    draw_text( '     1) Decimal Degrees (d)',           5,  60 )

    draw_rect( 5, 65, screen_size[0]-10, 25, line_color = Color.BLACK )
    draw_text( '     2) Degrees, Minutes (m)',          5,  85 )

    draw_rect( 5, 90, screen_size[0]-10, 25, line_color = Color.BLACK )
    draw_text( '     3) Degrees, Minutes, Seconds (s)', 5, 110 )

    draw_rect( 5, 115, screen_size[0]-10, 25, line_color = Color.BLACK )
    draw_text( '  esc) Exit Application',            5, 135 )

    #  Run until action received
    action = None
    while True:

        #  Wait on keys
        keys = get_keys()
        if len(keys) > 0:

            for k in keys:
                
                if k == 'esc':
                    return None
                
                elif k == '1' or k == 'd':
                    return TYPE_GEO_DD
                elif k == '2' or k == 'm':
                    return TYPE_GEO_DM
                elif k == '3' or k == 's':
                    return TYPE_GEO_DMS
                else:
                    pass
        else:
            sleep(0.1)

#---------------------------#
#-      Primary Menu       -#
#---------------------------#
def coord_converter():
    
    #  Resulting Coordinates
    coord_types = []

    #  Iterate over input and output
    redraw_all = True
    while len(coord_types) < 2:

        #  Draw the header
        if redraw_all:
            ti_draw.clear()
        
        fill_rect( 5, 5, screen_size[0]-10, 35, Color.DODGER_BLUE )
        draw_text( '    Coordinate Conversions   Time:  ' + format_time(localtime()) , 5, 30 )

        #  Draw Menu Options
        if redraw_all:
            hdr = 'Input'
            if len(coord_types) == 1:
                hdr = 'Output'
        
        if redraw_all:
            fill_rect( 5, 35, screen_size[0]-10, 25, Color.LIGHT_BLUE )
            draw_text( '    ' + hdr + ' Coordinate Type:', 5, 55 )
            
            draw_rect( 5, 60, screen_size[0]-10, 25, line_color = Color.BLACK )
            draw_text( '    g)  Geographic',                    5,  80 )

            draw_rect( 5, 85, screen_size[0]-10, 25, line_color = Color.BLACK )
            draw_text( '    e)  Earth-Centered, Earth-Fixed',   5, 105 )

            draw_rect( 5, 110, screen_size[0]-10, 25, line_color = Color.BLACK )
            draw_text( '    u)  Universal Transverse Mercator', 5, 130 )

            draw_rect( 5, 135, screen_size[0]-10, 25, line_color = Color.BLACK )
            draw_text( ' esc)   Exit Application',            5, 155 )

        #  Run the "interrupt" loop until something interest
        okay_to_run = True
        while okay_to_run:

            #  Fetch keys received
            keys = get_keys()
            if len(keys) > 0:
                for k in keys:

                    #  Exit Menu
                    if k == 'esc':
                        return None

                    #  Geographic Coordinates
                    elif k == 'g':
                        geo_value = geographic_menu()
                        print( "Returned: ", geo_value )
                        if geo_value is None:
                            return
                        coord_types.append( geo_value )
                        redraw_all = True
                        okay_to_run = False
                        break

                    elif k == 'u':
                        coord_types.append( TYPE_UTM )
                        redraw_all = True
                        okay_to_run = False
                        break

                    elif k == 'e':
                        coord_types.append( TYPE_ECEF )
                        redraw_all = True
                        okay_to_run = False
                        break

                    else:
                        print('Key Pressed: ', k)
            else:
                sleep(0.1)

    #  Perform Conversion
    print( 'Performing Conversions ', coord_types )

    coord_input_menu( coord_types )
