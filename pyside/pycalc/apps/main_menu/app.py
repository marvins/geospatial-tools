
from PySide6.QtWidgets import QGridLayout, QWidget

#  Project Libraries
from apps.app_base import *

class Main_Menu(App_Base):

    def __init__( self ):

        #  Setup Parent
        super().__init__()

    
    def create_main_widget( self ):

        main_widget = QWidget( self )
        self.main_layout = QGridLayout( main_widget )

        #  Add Buttons
        self.create_buttons()
    
        return main_widget

    def create_buttons(self):

        pass
