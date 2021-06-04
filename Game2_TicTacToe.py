
theboard = {'1':' ','2':' ','3':' ',
             '4':' ','5':' ','6':' ',
             '7':' ','8':' ','9':' '}

boardkeys =[]

for key in theboard:
    boardkeys.append(key)

def printboard(board):
    print("     " + board['1'] + "  |" + board['2'] + " |" + board['3'])
    print("     ---+--+---")
    print("     " + board['4'] + "  |" + board['5'] + " |" + board['6'])
    print("     ---+--+---")
    print("     " + board['7'] + "  |" + board['8'] + " |" + board['9'])
    print("     ---+--+---")

def game():
    turn = 'X'
    count = 0

    for i in range(10):

        printboard(theboard)
        print("It is turn of " + turn + " specify the place:")
       
        move = input()

        if theboard[move] == ' ':
            theboard[move] = turn
            count +=1
        
        else:
            print("This place is filled. \nChoose anothe one.")
            continue

        if count >=5:

            if theboard['7'] == theboard['8'] == theboard['9'] != ' ':
                printboard(theboard)
                print("\nGame Over")
                print("Player " + turn + " won the game")
                break

            elif theboard['4'] == theboard['5'] == theboard['6'] != ' ':
                printboard(theboard)
                print("\nGame Over")
                print("Player " + turn + " won the game")
                break

            elif theboard['1'] == theboard['2'] == theboard['3'] != ' ':
                printboard(theboard)
                print("\nGame Over")
                print("Player " + turn + " won the game")
                break

            elif theboard['7'] == theboard['4'] == theboard['1'] != ' ':
                printboard(theboard)
                print("\nGame Over")
                print("Player " + turn + " won the game")
                break

            elif theboard['8'] == theboard['5'] == theboard['2'] != ' ':
                printboard(theboard)
                print("\nGame Over")
                print("Player " + turn + " won the game")
                break

            elif theboard['9'] == theboard['6'] == theboard['3'] != ' ':
                printboard(theboard)
                print("\nGame Over")
                print("Player " + turn + " won the game")
                break

            elif theboard['7'] == theboard['5'] == theboard['3'] != ' ':
                printboard(theboard)
                print("\nGame Over")
                print("Player " + turn + " won the game")
                break

            elif theboard['1'] == theboard['5'] == theboard['9'] != ' ':
                printboard(theboard)
                print("\nGame Over")
                print("Player " + turn + " won the game")
                break

        if count == 9:
            print("\nGame Over")
            print("The game is Tie")    
            break

        if turn == "X":
            turn = "O"
        else:
            turn = "X"

    printboard(theboard)       

    restart = input("Do you want to restart the game? (y/n)") 

    if restart == 'y' or restart == 'Y': 
        for key in boardkeys:
            theboard[key] = ' '
        
        game()

if __name__ == "__main__" :
    game()




