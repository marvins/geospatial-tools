
from config import Configuration
from ui     import UI

def main():

    config = Configuration()
    ui = UI( config )

    ui.show()

main()
