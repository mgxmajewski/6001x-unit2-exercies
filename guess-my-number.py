print('Please think of a number between 0 and 100!')
answer = False
high = 100
low = 0
while not answer:
    check = int(low+((high-low)/2))
    print("Is your secret number " + str(int(check)) + '?')
    user_input = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    if user_input == 'h':
        high = check
    elif user_input == 'l':
        low = check
    elif user_input == 'c':
        print("Game over. Your secret number was: " + str(int(check)))
        answer = True
    else:
        print('Sorry, I did not understand your input.')