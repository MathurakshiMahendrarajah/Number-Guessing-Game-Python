import random

def GuessGame():
    while True: #to play again easily
        num=random.randint(1,100) #random number generation between 1 to 100
        attempt=1
        print("Welcome to the Number Guessing Game!")
        print("I have selected a number between 1 and 100.")
        print("You have 5 attempts to guess it.")

        while attempt <= 5 :
            try:
                userInput = int(input(f"\nAttempt {attempt} - Enter your guess: "))
            except ValueError:
                    print("⚠️ Invalid input! Please enter a number.")
                    continue #skip the loop 
            
            difference = abs(num - userInput)  
            
            if userInput == num:
                    print("🎉 Congratulations! You guessed it right!")
                    print(f"You found it in {attempt} attempts.")
                    break
            elif userInput < num:  # too low
                if difference > 50:
                    print("Too low.. Go up!")
                elif difference > 25:
                    print("Low.. A bit up!")
                elif difference > 10:
                    print("Slightly low.. Just a bit up!")
                else:
                    print("Very close! Just a little higher!")
            else:  # too high
                if difference > 50:
                    print("Too high.. Go down!")
                elif difference > 25:
                    print("High.. A bit down!")
                elif difference > 10:
                    print("Slightly high.. Just a bit down!")
                else:
                    print("Very close! Just a little down!")

            attempt += 1

        if attempt > 5 and userInput != num:
            print("😞 You've used all attempts! The number is: " + str(num))
        
        # replay option
        again = input("\nDo you want to play again? (y/n): ").lower()
        if again != 'y':
            print("👋 Thanks for playing! Goodbye!")
            break
        
#Run the game
GuessGame()