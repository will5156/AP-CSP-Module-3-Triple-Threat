"""
Triple threat simulation game for AP Computer Science Principles.
Monarch High School - Boulder Valley School District
william Goble - November 2024
"""

import random

def main() -> None:
    #varibles
    costtoplay: int = 2
    baseprize: int = 10
    meganumber: int = 6
    megamultiplyer: int = 10

    #genrates random number of plays
    min_plays:int = 1000
    max_plays:int = 5000
    num_days:int = 10
    print("Games Played,Total Collected,Total Paid Out,Profit")
    for _ in range(num_days):
        #number geration 
        num_plays: int = random.randint(min_plays,max_plays)
        total_colected: int = 0
        total_payout: int = 0
        total_profit: int =0
        
        #playing
        for _ in range(num_plays):
            #total varibles
            
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
            #total adding
            total_colected += costtoplay
            total_payout += payout
            total_profit += profit
            #output

        print(f"{num_plays},{total_colected},{total_payout},{total_profit}")

if __name__ == "__main__":
    main()