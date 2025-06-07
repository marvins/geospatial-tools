
from PySide6.QtWidgets import QHBoxLayout, QToolButton, QWidget


class Footer(QWidget):


    def __init__( self, *args, **kwargs ):
        
        super().__init__()

        #  Setup layout
        layout = QHBoxLayout()
        self.setLayout( layout )

        #  Setup Buttons
        button_esc = QToolButton()
        button_esc.setText( 'ESC' )
        layout.addWidget( button_esc )

        button_f1 = QToolButton()
        button_f1.setText( 'F1' )
        layout.addWidget( button_f1 )

        button_f2 = QToolButton()
        button_f2.setText( 'F1' )
        layout.addWidget( button_f2 )

        button_f3 = QToolButton()
        button_f3.setText( 'F1' )
        layout.addWidget( button_f3 )

        button_f4 = QToolButton()
        button_f4.setText( 'F4' )
        layout.addWidget( button_f4 )

        button_f5 = QToolButton()
        button_f1.setText( 'F5' )
        layout.addWidget( button_f5 )

