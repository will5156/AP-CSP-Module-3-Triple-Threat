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
    #genrates random number of plays
    min_plays:int = 1000
    max_plays:int = 5000
    num_plays: int = random.randint(min_plays,max_plays)
    #playing
    for _ in range(num_plays):
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
        profit: int = costtoplay - payout
        # output
        print(f"Casino collects: ${costtoplay}")
        print(f"Player rolls: {roll_1}-{roll_2}-{roll_3}")
        print(f"Casino payout: ${payout}")
        print(f"Profit: ${profit}")

if __name__ == "__main__":
    main()