###### Guess Alphabet with Histogram Display

import random

#### step 1. use ASCII to represent each lowercase alphabet (97 to 122)

# 97 means "a" ; 122 means "z"
alphabetic = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
ASCII_lowercase = [i for i in range(97,123)]
answer = random.randint(97,122)

#### step 2. ensure the user input the valid parameter
def get_valid_alpha() :  

    while True :
        alpha = input("Guess the lowercase alphabet : ")
        if alpha.islower() :
            if len(alpha) == 1 :
                break
            else :
                print("Please enter the \'single\' alphabet!")
                print()
                continue
        else :
            print("Please enter a lowercase alphabet.")
            print()
            continue
    
    # turn the guess alphabet into ASCII
    guess = 97 + alphabetic.index(alpha)
    
    return guess

#### step 3. compare the answer and user's guess

def compare_alpha_and_guess(answer,guess) :
    # store the user's guess alpha (ASCII)
    store_guess_alpha = []
    # 紀錄是第幾次輸入
    count = 1

    # every time the user input, we need to check the guess is low, high, equal ; by get_valid_alpha() function
    while True :
        if answer > guess :
            print("The alphabet you are looking for is alphabetically higher.")
            store_guess_alpha.append(guess)
            guess = get_valid_alpha()
            count += 1

        elif answer < guess :
            print("The alphabet you are looking for is alphabetically lower.")
            store_guess_alpha.append(guess)
            guess = get_valid_alpha()
            count += 1

        else :
            print("Congratulations! You guessed the alphabet \'%s'\ in %d tries."%(guess,count))
            print()
            store_guess_alpha.append(guess)
            break

    return store_guess_alpha

#### step 4. calculate the frequency, and then display the histogram
def display_histogram(store_guess_alpha) :
    print("Guess Histogram : ")

    # determine the number of asterisk
    frequency = [0 for _ in range(7)]
    for i in store_guess_alpha :
        j = 0
        while j < 26 :

            if j <= (i-97) <= j + 3 :
                frequency[(i-97)//4] += 1
            j += 4
    
    j = 0
    while j < 26 :
        asterisk = "*"*frequency[(j//4)]
        if j < 24 :
            print("%s-%s: %s"%(alphabetic[j],alphabetic[j+3],asterisk))
        else :
            print("y-z: %s"%(asterisk))
        
        j += 4

#### the execution of main program
if __name__ == "__main__" :
    guess = get_valid_alpha()

    store_guess_alpha = compare_alpha_and_guess(answer,guess)
    display_histogram(store_guess_alpha)
        
