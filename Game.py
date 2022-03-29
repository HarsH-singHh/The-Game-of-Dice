import sys
import random

def printCurrRankings(playersScore):  # function for printing current rankings
        print("***** Current Rankings *****")                       
        ranks = list(playersScore.items())
        ranks.sort(key = lambda x: x[0])
        ranks.sort(key = lambda x: x[1], reverse=True)
    
        for player, score in ranks:
            if score<target:
                print(f'Player_{player} : {score}')
        print("****************************")

def rollDice(index,playerNum,target,playersStats,playersScore,finalRanks):  # function to simulate rolling a dice
    roll = int(random.randrange(1,7))                                       # generating random number between 1-6
    print("Roll result :", roll)
    print()
    playersStats[index][1]+=roll                                            # adding points in total score in playerStats list
    playersScore[playersStats[index][0]]+=roll                              # adding points in playersScore dictionary 
    
    if playersScore[playersStats[index][0]] >= target:                      # adding player in finalRanks list if target points are achieved
        finalRanks.append((playersStats[index][0], playersStats[index][1]))
        print(f'player_{playerNum} completes the game with {len(finalRanks)} Rank.')
        print()
    
    return roll

############## Driver code ##############    

totalPlayers= input("Enter no. of players (greater than 0) - ")  # no. of players
if not totalPlayers.isnumeric():                                 # checking for valid no. of players 
    print("Invalid number")
    sys.exit()                                                   # script will terminate if input isn't a number
else:
    totalPlayers = int(totalPlayers)
    
target= input("Enter target score (greater than 0) - ")          # points to accumulate
print()
if not target.isnumeric():                                       # checking for valid points
    print("Invalid number")
    sys.exit()                                                   # script will terminate if input isn't a number
else:
    target = int(target)           


if totalPlayers and target and totalPlayers>0 and target>0:   # checking if no. of players and target points are valid
    finalRanks=[]
    players = [int(i) for i in range(1,totalPlayers+1)]       # list of players
    
    random.shuffle(players)                                   # shuffling order of players
    playersStats=[[i,0,0,False] for i in players]             # keeping last die roll points and total points
    
    playersScore = {}                                         # dictionary to store player number and respective points
    for i in range(1,totalPlayers+1):
        playersScore[i]=0
    
    print()
    
    Rounds=1
    
    while len(finalRanks)!=totalPlayers:                       # running loop till all players have accumulated target points
        print(f'-----------Round {Rounds}-----------')                            
        for index, playerNum in enumerate(players):            # loop to roll dice for remaining players 
            roll = 0
            if len(finalRanks)==totalPlayers:                  # to break for loop when all players have attained minimum points
                break
            if not playersStats[index][3] and playersStats[index][1]<target:   # to skip players who acquired minimum points
                print(f'player_{playerNum} its your turn (press ''r'' to roll the dice)')
                inputText = input()
                
                if inputText!='r':                             # skipping the current player's chance if input isn't 'r'
                    print("Invalid entry next player chance.")
                    print()
                else:
                    roll = rollDice(index,playerNum,target,playersStats,playersScore,finalRanks)
                    
                    if playersStats[index][2]==1 and roll==1:  # if player throws two consecutive 1's
                        print("Oops you rolled '1' twice, your next chance will be skipped.")
                        print()
                        playersStats[index][3]=True
                    
                    if roll == 6 and playersScore[playersStats[index][0]]<target:  # if player throws 6 dice is rolled again
                        print(f'player_{playerNum} you rolled a 6.')
                        print('Its your turn again (press ''r'' to roll the dice)')
                        inputText = input()
                    
                        if inputText!='r':
                            print("Invalid entry next player chance.")
                            print()
                        else:
                            roll = rollDice(index,playerNum,target,playersStats,playersScore,finalRanks)

                playersStats[index][2]=roll    # storing current roll points
            
            else:                              # else will execute if two 1's are rolled
                if playersStats[index][3]: 
                    print(f'Your chance is skipped player{playersStats[index][0]}')
                    print()
                    playersStats[index][2]=0
                    playersStats[index][3]=False
            
            if len(finalRanks)!=totalPlayers and roll>0:  # printing rankings after each player roll
                printCurrRankings(playersScore)
            print()
        
        Rounds+=1   # incrementing rounds

    print("***** Final Rankings *****")   # final rankings
    for rank in range(totalPlayers):
        print(f'Rank {rank+1} - Player{finalRanks[rank][0]}')
    print("Thank you for playing.")
else:                                     # for edge cases if no. of players or target is negative or not a number
    print("Invalid no. of players or invalid target")