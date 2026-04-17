import random

user_score = 0
computer_score = 0

options = ["snake", "water", "gun"]

while True:
    choice = input("Choose snake, water, gun (or exit): ").lower()

    if choice == "exit":
        print("Game ended")
        print(f"Final Score → You: {user_score}, Computer: {computer_score}")
        break

    if choice not in options:
        print("Invalid choice")
        continue

    computer_choice = random.choice(options)
    print("Computer chose:", computer_choice)

    if choice == computer_choice:
        print("It's a tie!")

    elif (choice == "snake" and computer_choice == "water") or \
         (choice == "water" and computer_choice == "gun") or \
         (choice == "gun" and computer_choice == "snake"):
        print("You win!")
        user_score += 1

    else:
        print("Computer wins!")
        computer_score += 1

    print(f"Score → You: {user_score}, Computer: {computer_score}")
    