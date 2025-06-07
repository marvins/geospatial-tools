#**************************** INTELLECTUAL PROPERTY RIGHTS ****************************#
#*                                                                                    *#
#*                           Copyright (c) 2025 Terminus LLC                          *#
#*                                                                                    *#
#*                                All Rights Reserved.                                *#
#*                                                                                    *#
#*          Use of this source code is governed by LICENSE in the repo root.          *#
#*                                                                                    *#
#**************************** INTELLECTUAL PROPERTY RIGHTS ****************************#

#  PySide6 Libraries
from PySide6.QtWidgets import QGridLayout, QLabel, QVBoxLayout, QWidget

#  Project Libraries
from header import Header
from footer import Footer

class App_Base(QWidget):

    def __init__( self ):

        #  Build Parent
        super().__init__()
        
        #  Primary Layout
        self.layout = QVBoxLayout(self)

        #  Create Header
        self.header = Header( self )
        self.layout.addWidget( self.header )

        #  Create Main Widget
        self.main_widget = self.create_main_widget()
        self.layout.addWidget( self.main_widget )

        #  Create Footer
        self.footer = Footer( self )
        self.layout.addWidget( self.footer )

    
    def create_buttons(self):
        pass
