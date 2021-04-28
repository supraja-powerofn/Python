import random

options = ['rock','paper','scissor']
user_sc , comp_sc =  int(0),int(0)

while (user_sc != 5 or comp_sc != 5):
    comp_ch = random.choice(options)
    user_ch = input(str('Enter your choice: rock,paper or scissor ')).lower()
    if(user_ch == 'rock'):
        if(comp_ch == 'scissor'):
            print("Computer's choice is ",comp_ch)
            print("You win a point!")
            user_sc += 1
            continue
        elif(comp_ch == 'paper'):
            print("Computer's choice is ",comp_ch)
            print("Computer wins a point!")
            comp_sc += 1
            continue
        else:
            print("Computer's choice is ",comp_ch)
            print("It's a tie!")
            continue
    elif(user_ch == 'paper'):
        if(comp_ch == 'scissor'):
            print("Computer's choice is ",comp_ch)
            print("Computer wins a point!")
            comp_sc += 1
            continue
        elif(comp_ch == 'rock'):
            print("Computer's choice is ",comp_ch)
            print("You win a point!")
            user_sc += 1
            continue
        else:
            print("Computer's choice is ",comp_ch)
            print("It's a tie!")
            continue
    elif(user_ch == 'scissor'):
        if(comp_ch == 'rock'):
            print("Computer's choice is ",comp_ch)
            print("Computer wins a point!")
            comp_sc += 1
            continue
        elif(comp_ch == 'paper'):
            print("Computer's choice is ",comp_ch)
            print("You win a point!")
            user_sc += 1 
            continue
        else:
            print("Computer's choice is ",comp_ch)
            print("It's a tie!")
            continue
    else:
        print("Please enter a valid option")

print("Game over ")
if(user_sc == 5):
    print("You won the game")
else:
    print("You lost the game")

        