import random

def main():
    attempts = 0
    number_to_guess = random.randint(1, 100)
    print("Welcome to the number guessing game!")
    print("I have chosen a number between 1 and 100.")
    print("Try to guess it in as few attempts as possible.")
    
    while True:
        try:
            user_guess = int(input("Enter your guess: "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 100.")
            continue
        
        attempts += 1
        
        if user_guess == number_to_guess:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break
        elif user_guess < number_to_guess:
            print("Your guess is too low. Try again.")
        else:
            print("Your guess is too high. Try again.")

if __name__ == "__main__":
    main()