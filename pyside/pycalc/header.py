
from PySide6.QtWidgets import QHBoxLayout, QLabel, QWidget


class Header(QWidget):


    def __init__( self, *args, **kwargs ):
        
        super().__init__()

        #  Setup layout
        layout = QHBoxLayout()
        self.setLayout( layout )

        #  Setup Titlebar
        self.title_bar = QLabel()
        self.title_bar.setText( 'Main Menu' )
        layout.addWidget( self.title_bar )

