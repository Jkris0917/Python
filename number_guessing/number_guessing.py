# import random

# secret = random.randint(1,100)
# attempts = 0
# max_attempts = 5
# round = 1
# percentage = 100
# scores = []

# print("""==Welcome to Guessing Game!==\nGuess the secret number from 1 up to 100,""")
# print(f"You have {max_attempts} attempts only")
# print(secret)

# while True:

#     guess = input("Enter Number or (type 'quit'): ").lower()
#     if guess == 'quit':
#         break
#     elif not guess.isdigit():
#         print("Must be a Number")
#         continue
#     else:
#         guess = int(guess)
#     attempts += 1
#     used_attempts = max_attempts - 1

#     if guess > secret:
#         print(f"Too High, Your {abs(secret-guess)} away, {used_attempts} attempts left.")
#     elif guess < secret:
#         print(f"Too Low!, Your {abs(secret-guess)} away, {used_attempts} attempts left.")
    
#     if guess == secret:
#         print(f'Congratulations!, You Guess it in {attempts} attempts.')
        
#         try_again = input('Wanna Try Again? (Yes/No): ').lower()
#         if not try_again in ['yes','no']:
#             print('Yes or No only!')
#             try_again = input('Wanna Try Again? (Yes/No): ').lower()
#         elif try_again == 'yes':
#             scores.append(((max_attempts - attempts)/max_attempts) * 100)
#             attempts = 0
#             max_attempts = 5
#             secret = random.randint(1,100)
#             print(secret)
#             continue
#         else:
#             scores.append(((max_attempts - attempts)/max_attempts) * 100)
#             break
    
#     if used_attempts == 0:
#         print(f"\nYou have {used_attempts} left, Better luck next time")
#         break

# print("==All Your Scored ==")
# for index, score in enumerate(scores, start=1):
#     print(f"Round {index}: {score}")

#Correct Version

import random

secret = random.randint(1, 100)
attempts = 0
max_attempts = 5
scores = []

print("== Welcome to Guessing Game! ==")
print(f"Guess the secret number from 1 to 100.")
print(f"You have {max_attempts} attempts only.\n")

while True:
    guess = input("Enter number or type 'quit': ").lower()

    if guess == 'quit':
        break
    elif not guess.isdigit():
        print("Must be a number!")
        continue

    guess = int(guess)
    attempts += 1
    used_attempts = max_attempts - attempts  # ✅ fixed

    if guess == secret:
        score = ((max_attempts - attempts) / max_attempts) * 100
        scores.append(score)
        print(f"\nCongratulations! You guessed it in {attempts} attempt(s)!")
        print(f"Score this round: {score:.1f}%")

        while True:
            try_again = input('\nWanna try again? (Yes/No): ').lower()
            if try_again in ['yes', 'no']:
                break
            print('Yes or No only!')

        if try_again == 'yes':
            secret = random.randint(1, 100)
            attempts = 0
            print(f"\n--- New round! ---\n")
            continue
        else:
            break

    elif guess > secret:
        print(f"Too high! You're {abs(secret - guess)} away. {used_attempts} attempt(s) left.")
    else:
        print(f"Too low! You're {abs(secret - guess)} away. {used_attempts} attempt(s) left.")

    if used_attempts == 0:  # ✅ now triggers correctly
        print(f"\nOut of attempts! The secret number was {secret}.")
        break

print("\n== Your Scores ==")
if scores:
    for i, score in enumerate(scores, start=1):
        print(f"  Round {i}: {score:.1f}%")
    print(f"  Average: {sum(scores)/len(scores):.1f}%")
else:
    print("  No completed rounds.")