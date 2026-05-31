import random
randNum = random.randint(1, 100)

while True:
    userChoice = input("Guess the target or Quit :")

    if(userChoice == "Quit"):
        break

    try:
       userChoice = int(userChoice)
    except:
        print("Invalid Input!")
        continue

    if(userChoice == randNum):
        print("Success : Correct Guess!!")
        break
    elif(userChoice < randNum):
        print("your number was too small. Take a bigger guess...")
    else:
        print("your number was too big. Take a smaller guess...")

print("___GAME OVER___")  