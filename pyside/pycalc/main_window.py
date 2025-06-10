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
from PySide6.QtWidgets import QMainWindow, QStackedWidget

#  Project Libraries
from apps.main_menu.app import Main_Menu

class Main_Window( QMainWindow ):

    def __init__(self):
        super().__init__()

        #  Setup Main Page
        self.setWindowTitle( 'Terminus Geospatial Toolbox' )

        #  Primary Widget
        self.main_widget = QStackedWidget( self )
        self.setCentralWidget( self.main_widget )

        self.build_apps()

    def build_apps( self ):

        self.apps = []

        #  Create Main Menu
        self.apps.append( Main_Menu() )
        self.main_widget.addWidget( self.apps[-1] )
        
        
if __name__ == '__main__':
    main()