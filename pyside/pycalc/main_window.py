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

#  PySide Libraries
from PySide6.QtWidgets import QMainWindow


class Main_Window( QMainWindow ):

    def __init__(self):
        super().__init__()

        #  Setup Main Page
        self.setWindowTitle( 'Terminus Geospatial Toolbox' )
        
        
if __name__ == '__main__':
    main()