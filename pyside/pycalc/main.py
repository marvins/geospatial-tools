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
import sys

#  PySide Libraries
from PySide6.QtWidgets import QApplication

#  Project Libraries
from main_window import Main_Window

def main():

    #  Setup Core Application
    app = QApplication()

    main_window = Main_Window()

    main_window.show()

    sys.exit( app.exec() )

if __name__ == '__main__':
    main()