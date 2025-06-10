
import PySide6.QtCore  as QtCore
from PySide6.QtGui     import QKeySequence
from PySide6.QtWidgets import QHBoxLayout, QToolButton, QWidget


class Footer(QWidget):

    #  Override this with layout_map parameter
    default_button_layout = { 'ESC':  QKeySequence( QtCore.Qt.Key.Key_Escape ),
                              'F1' :  QKeySequence( QtCore.Qt.Key.Key_F1 ),
                              'F2' :  QKeySequence( QtCore.Qt.Key.Key_F2 ),
                              'F3' :  QKeySequence( QtCore.Qt.Key.Key_F3 ),
                              'F4' :  QKeySequence( QtCore.Qt.Key.Key_F4 ),
                              'F5' :  QKeySequence( QtCore.Qt.Key.Key_F5 ) }

    def __init__( self, *args, **kwargs ):
        
        super().__init__()

        #  Setup Layout
        if 'button_layout' in kwargs.keys():
            self.button_layout = kwargs['button_layout']
        else:
            self.button_layout = self.default_button_layout

        #  Setup layout
        layout = QHBoxLayout()
        self.setLayout( layout )

        #  Setup Buttons
        for item in self.button_layout:

            button = QToolButton()
            button.setText( item )
            button.setShortcut( self.button_layout[item] )
            layout.addWidget( button, 1 )


