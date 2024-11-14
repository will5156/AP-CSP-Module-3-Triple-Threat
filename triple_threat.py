"""
Triple threat simulation game for AP Computer Science Principles.
Monarch High School - Boulder Valley School District
Name - Month Year
"""

import random

def main() -> None:
    #varibles
    costtoplay: int = 1
    baseprize: int = 10
    meganumber: int = 6
    megamultiplyer: int = 10
    #rolls
    roll_1:int = random.randint(1,6) 
    roll_2:int = random.randint(1,6) 
    roll_3:int = random.randint(1,6) 
    # checking  
    payout:int = 0
    if roll_1 == roll_2 and roll_1 == roll_3:
        if roll_1 == meganumber:
            payout = baseprize * megamultiplyer
        else:
            payout = baseprize * roll_1
    # output
    print("Casino collects: ${costtopay}")
    print("Player rolls: {roll_1}-{roll_2}-{roll_3}")
    print("")
    print("")

if __name__ == "__main__":
    main()