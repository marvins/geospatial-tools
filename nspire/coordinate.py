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
    fill_rect( 5, 5, screen_size[0]-10, 35, Color.LIGHT_BLUE )
    draw_text( 'Geographic Coordinate' , 5, 30 )

    # 
    draw_text( '1. Decimal Degrees (d)',           5,  60 )
    draw_text( '2. Degrees, Minutes (m)',          5,  85 )
    draw_text( '3. Degrees, Minutes, Seconds (s)', 5, 110 )
    draw_text( 'esc: Exit Application',            5, 135 )

    #  Run until action received
    action = None
    while True:

        #  Wait on keys
        keys = get_keys()
        if len(keys) > 0:

            for k in keys:
                
                if k == 'esc':
                    action = 'exit'
                    break
                
                elif k == '1' or k == 'd':
                    return dd_menu()
                elif k == '2' or k == 'm':
                    return dm_menu()
                elif k == '3' or k == 's':
                    return dms_menu()
                else:
                    pass
        
        else:
            sleep(0.1)

#---------------------------#
#-      Primary Menu       -#
#---------------------------#
def coord_converter():
    
    #  Resulting Coordinates
    input_coord = None
    output_type = None

    for x in range(2):

        #  Draw the header
        ti_draw.clear()
        fill_rect( 5, 5, screen_size[0]-10, 35, Color.LIGHT_BLUE )
        draw_text( 'Coordinate Conversions   Time:  ' + format_time(localtime()) , 5, 30 )

        #  Draw Menu Options
        hdr = 'Input'
        if x == 1:
            hdr = 'Output'
        
        draw_text( hdr + ' Coordinate Type:', 5, 55 )
        draw_text( '----------------------', 5, 65 )
        draw_text( '  g) Geographic',                    5,  85 )
        draw_text( '  e) Earth-Centered, Earth-Fixed',   5, 105 )
        draw_text( '  u) Universal Transverse Mercator', 5, 125 )
        draw_text( ' esc.  Exit Application',            5, 145 )

        #  Run the "interrupt" loop until something interest
        okay_to_run = True
        while okay_to_run:

            #  Fetch keys received
            keys = get_keys()
            if len(keys) > 0:
                for k in keys:

                    if k == 'esc':
                        okay_to_run = False
                        action = 'exit'
                        break

                    elif k == 'g':
                        coord_types.append( 'geo' )
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
                sleep(0.2)

        if action == 'exit':
            return action
    
    
    print('Exiting Coordinate Menu' )
    return action

