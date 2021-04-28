import random

n = random.randint(0,100)
tries  = 10
while(tries > 0):
    user_ip = int(input(str('Guess the number : ')))
    if( n > user_ip):
        print("Number is greater than ",user_ip)
    elif( n < user_ip):
        print("Number is lesser than ",user_ip)
    elif( n == user_ip):
        print("Number matched!")
        exit()
    tries -= 1
    
print("Nice try!")
