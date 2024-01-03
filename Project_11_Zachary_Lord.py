#!/usr/bin/env python3

#Zachary Lord
PLAYERS =  {
        "Joel": [32, 14, 17],
        "Elizabeth": [41, 3, 22],
        "Mike": [8, 19, 11]
    }
def display_names(players):
    codes = list(PLAYERS.keys())
    codes.sort()
    print('ALL PLAYERS:')
    for code in codes:
        print(code)

def players_stats():
    name= input("Enter a player's name: ")
    name = name.capitalize()
    wins = PLAYERS[name][0]
    losses = PLAYERS[name][1]
    ties= PLAYERS[name][2]
    print('Wins:  {}'.format(wins))
    print('Losses: {}'.format(losses))
    print('Ties: {}'.format(ties))
    



def main():
    print("Game Stats program")
    print()

    display_names(PLAYERS)
    while True:
        players_stats()
        prompt =  input('Continue? (y/n):')

        if prompt.lower()== 'n':
            print('Bye!')
            break
         
             
        
    
if __name__ == "__main__":
    main()
