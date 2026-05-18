import random

secret = random.randint(1,100)
attempts = 0
max_attempts = 5
round = 1
percentage = 100
round = []
score = []

print("""==Welcome to Guessing Game!==\nGuess the secret number from 1 up to 100,""")
print(f"You have {max_attempts} attempts only")
print(secret)

while True:

    guess = input("Enter Number or (type 'quit'): ").lower()
    if guess == 'quit':
        break
    elif not guess.isdigit():
        print("Must be a Number")
        continue
    else:
        guess = int(guess)
    attempts += 1
    used_attempts = max_attempts - 1

    if guess > secret:
        print(f"Too High, Your {abs(secret-guess)} away, {used_attempts} attempts left.")
    elif guess < secret:
        print(f"Too Low!, Your {abs(secret-guess)} away, {used_attempts} attempts left.")
    
    if guess == secret:
        print(f'Congratulations!, You Guess it in {attempts} attempts.')
        
        try_again = input('Wanna Try Again? (Yes/No): ').lower()
        if not try_again in ['yes','no']:
            print('Yes or No only!')
            try_again = input('Wanna Try Again? (Yes/No): ').lower()
        elif try_again == 'yes':
            round.append(1)
            score.append(((max_attempts - attempts)/max_attempts) * 100)
            attempts = 0
            max_attempts = 5
            secret = random.randint(1,100)
            print(secret)
            continue
        else:
            score.append(((max_attempts - attempts)/max_attempts) * 100)
            break
    
    if used_attempts == 0:
        print(f"\nYou have {used_attempts} left, Better luck next time")
        break
print(score)
print(round)
    
    
    
    


