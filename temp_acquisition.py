# Get temperature from Sense Hat Board

import time
from sense_hat import SenseHat

def main():
    board = SenseHat()

    while(True):
        temp = board.get_temperature()
        print(temp)
        time.sleep(3)

if __name__=="__main__":
    main()

