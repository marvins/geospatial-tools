
#  Micropython Libraries
import os
import sys

#  Project Libraries
import colors
import picocalc
from picocalc import PicoDisplay


def main( cdir ):
    
    display = picocalc.PicoDisplay(320, 320)
    display.fill(0)

    # Draw 16 color bars
    for i in range(16):
        display.fill_rect( 0, i * 20, 320, 20, i)

    display.text("Hello PicoCalc!", 10, 310, 15)
    display.show()

#  Sort out what directory to start with
start_dir = os.getcwd()
if len(sys.argv) > 0:
    start_dir = sys.argv[0]

main( start_dir )