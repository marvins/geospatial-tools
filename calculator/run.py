#!/usr/bin/env python3
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
#    File:    run.py
#    Author:  Marvin Smith
#    Date:    May 13, 2025
#
#    Purpose:  Wrapper for turtle that supports calculators
#

#  Python Libraries
import setup

# Terminus Libraries
from tmns_geo.ui.core import UI

#  Run the application
def main():

    options = setup.Options()

    ui = UI( options )

    return ui.show()

main()
