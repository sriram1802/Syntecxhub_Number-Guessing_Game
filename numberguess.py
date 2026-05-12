import random
best_score=None
while True:
    print("===== NUMBER GUESSING GAME =====")
    print("1.Easy (1-10)")
    print("2.Medium (1-50)")
    print("3.Hard (1-100)")
    print("4.Exit")
    choice=input("Choose difficulty: ")
    if choice=="1":
        limit=10
    elif choice=="2":
        limit=50
    elif choice=="3":
        limit=100
    elif choice=="4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice\n")
        continue
    number=random.randint(1,limit)
    attempts=0
    while True:
        try:
            guess=int(input(f"Guess a number between 1 and {limit}: "))
            attempts+=1
            if guess<number:
                print("Too low!\n")
            elif guess>number:
                print("Too high!\n")
            else:
                print(f"Correct! You guessed in {attempts} attempts.\n")
                if best_score is None or attempts<best_score:
                    best_score=attempts
                    print(f"New Best Score: {best_score}\n")
                break
        except:
            print("Enter a valid number\n")
    replay=input("Play again? (yes/no): ").lower()
    if replay!="yes":
        print("Thanks for playing!")
        break