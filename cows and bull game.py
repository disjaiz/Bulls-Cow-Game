import random

def bull_cow_count(code, guess):
    code = str(code)
    guess = str(guess)
    bulls = 0
    cows = 0

    for i in range(0,len(code)):
        if code[i] == guess[i]:
            bulls +=1
        
        elif guess[i] in code and guess[i] != code[i]:
            cows +=1

    return bulls, cows


def bulls_n_cows():
    secret_code = random.randint(1000, 9999)
    
    print("Guess the 4-digit secret code.")

    while True:
        user_guess = int(input("\nGuess => "))

        if user_guess > 9999 or user_guess < 1000:
            print("\n           -- Incorrect no. of digits. Pls enter only 4-digit number --")
            continue

        if user_guess != secret_code:
            bulls, cows = bull_cow_count(secret_code, user_guess)
            print(f"{bulls} bulls and {cows} cows")
            continue
        else:
            print("\nCorrect guess -- You win --")
            break

bulls_n_cows()