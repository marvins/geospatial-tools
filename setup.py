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
#    File:    setup.py
#    Author:  Marvin Smith
#    Date:    May 13, 2025
#
#    Purpose:  Provides settings to configure apps using this API.
#

#  Enter your device here
#  options:
#  - numworks
#  - nspire
#  - unix
device='numworks'

if device == 'nspire':
    from tmns_geo.nspire.draw import *
    from tmns_geo.nspire.hal  import *

elif device == 'numworks':
    from tmns_geo.numworks.draw import *
    from tmns_geo.numworks.hal  import *


class Options:
    screen_size     = (320,240)
    sleep_time_secs = 0.1