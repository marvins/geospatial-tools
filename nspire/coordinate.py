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
ECEF    = 0
GEO_DD  = 1
GEO_DM  = 2
GEO_DMS = 3
UTM     = 4

class Base:
    '''
    Base Coordinate Type
    '''
  
    def __init__(self):
        pass


class Geo(Base):
    '''
    Geographic Coordinate System
    '''
  
    def __init__( self,
                  lat_deg = 0,
                  lon_deg = 0,
                  elev_m  = 0 ):
        self.m_lat_deg = lat_deg
        self.m_lon_deg = lon_deg
        self.m_elev_m  = elev_m

        super().__init__(self)

    @staticmethod
    def from_dms( lat_deg, lat_min, lat_sec,
                  lon_deg, lon_min, lon_sec,
                  elev_m = 0 ):
        
        lat = lat_deg + lat_min / 60.0 + lat_sec / 3600.0
        lon = lon_deg + lon_min / 60.0 + lon_sec / 3600.0
        return Geo( lat_deg = lat,
                    lon_deg = lon,
                    elev_m  = elev_m )
    
    @staticmethod
    def from_dm( lat_deg, lat_min,
                 lon_deg, lon_min,
                 elev_m = 0 ):

        lat = lat_deg + lat_min / 60.0
        lon = lon_deg + lon_min / 60.0

        return Geo( lat_deg = lat,
                    lon_deg = lon,
                    elev_m  = elev_m )

    @staticmethod
    def from_dd( lat_deg, lon_deg, elev_m = 0 ):

        return Geo( lat_deg = lat,
                    lon_deg = lon,
                    elev_m  = elev_m )


class UTM(Base):

    def __init__( self, 
                  grid_zone = None,
                  hemisphere = 'n',
                  easting = 0,
                  northing = 0,
                  elev_m  = 0 ):
        self.m_grid_zone  = grid_zone
        self.m_hemisphere = hemisphere
        self.m_easting    = easting
        self.m_northing   = northing
        self.m_elev_m     = elev_m

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
                    return GEO_DD
                elif k == '2' or k == 'm':
                    return GEO_DM
                elif k == '3' or k == 's':
                    return GEO_DMS
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
                        coord_types.append( 'utm' )
                        okay_to_run = False
                        break

                    elif k == 'e':
                        coord_types.append( 'ecef' )
                        okay_to_run = False
                        break

                    else:
                        print('Key Pressed: ', k)
            else:
                sleep(0.1)

