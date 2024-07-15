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

def generate_secret_code():
    num = random.randint(1000, 9999)

    num_list = list(str(num))

    # checking duplicate_numbers
    for i in range(len(num_list)):
        if num_list[i] in num_list[i+1: ]:
            generate_secret_code()
    return num


def bulls_n_cows():

    secret_code = generate_secret_code()
    chances = 10

    print("Guess the 4-digit secret code.")

    while chances > 0:
        print("\nChances left: ", chances)
        user_guess = int(input("\nGuess => "))

        if user_guess > 9999 or user_guess < 1000:
            print("\n           -- Incorrect no. of digits. Pls enter only 4-digit number --")
            chances -= 1
            continue

        if user_guess != secret_code:
            bulls, cows = bull_cow_count(secret_code, user_guess)
            print(f"{bulls} bulls and {cows} cows")
            chances -= 1
            
            continue
        else:
            print("\nCorrect guess -- You win --")
            break
    
    print("\nOoh ! You ran out of chances.\n")

bulls_n_cows()
