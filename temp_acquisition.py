# Get temperature from Sense Hat Board

import time
from sense_hat import SenseHat

def main():
    board = SenseHat()
    board.show_message("SenseHat")

if __name__=="__main__":
    main()

