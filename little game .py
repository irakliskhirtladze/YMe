import sys
import random

#first we define a function called start(), which asks for user name and game password
def start():
    print('To enter the system we need your name and password')
    n = input('Enter your name: ')       #here program waits for the user's name
    p = input('''Hi "''' + str.title(n) + '''", now enter your password: ''')     
    #here program waits for the game password       

    while p != '12345' and p != 'toor':
        print('Sorry ' + str(n) + ', password is wrong. Enter it again:')
        p = input()   #while input is neither '12345', nor 'toor' program keeps asking for password 

    while p == '12345':
        print("C'mon " + str(n) + ", are you that stupid?")
        print('Enter the fucking password!!!')
        p = input()              
        #while input is '12345', program is telling the user that this is a stupid idea and asks for password 

        while p != 'toor':       #another loop inside previous loop
            print('Wrong again. correct password please:')
            p = input()          #while input is not 'toor', program insists to try entering the right password

            if p == 'toor':      #and finally if input is 'toor', loop will end .....
                break

    print('Welcome ' + str(n) + '!')      #....and user will see 'access granted' message



#here we define the game function itself
def game():
    print('''Let's play a numbers game. I am thinking of a number
from 1 to 20 and you have to guess it. You can try 6 times.''')
    secret = random.randint(1, 21)
    print('Enter the number: ')

    for number in range(1, 7):
        try:
            num = input()
            if int(num) < secret:
                print('Too low, try again')
            elif int(num) > secret:
                print('Too high, try again')
            else:
                break
        except ValueError:
            print('Enter an integer')
            continue
    if int(num) == secret:
        print('Well done. you guessed the number in ' + str(number) + ' guesses')
    else:
        print('Eeeehh, the number was: ' + str(secret))


#this is the function of game end options
def over():
    global resp     #here we define variable resp as global variable
    resp = input('''Game is over.
type 'Yes' to exit, 'No' to stay and 'Out' to log out: ''')  #then wait for the user input
    while resp != 'Yes' and resp != 'No' and resp!='Out':  #while user input is not none of the three options...
        print("could not understand the command. type 'Yes' or 'No' please")
        resp = input()           #...program asks for input again 
    if resp == 'Yes':
        sys.exit()               #if input is 'Yes', program terminates 
    elif resp == 'No':
        print('Ok, lets play the game again')  
        #if input becomes 'No' program will print to 'play the game again'
        

#This is where the code execution actually starts...
start()        
game()
over()        #... and we call these three functions
while resp == 'No':   
    game()
    over()
while resp=='Out':
    start()
    game()
    over()    #I think everything is clear here
