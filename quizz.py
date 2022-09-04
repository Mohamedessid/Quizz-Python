print("Welcome to the quizz")

playing = input("Do you want to play? Yes/No  ").lower()

if playing != "yes":
    quit()

print("Let's play :)")

score = 0
answer = input("Which club has won the most Champions League titles? ")

if answer.lower() == "real madrid":
    print('correct')
    score += 1
else:
    print("incorrect!")

answer = input("Who is the only player to win the Champions League with three different clubs? ")

if answer.lower() == "seedorf":
    print('correct')
    score += 1
else:
    print("incorrect!")

answer = input("With 365 goals, who holds the record for top Bundesliga goalscorer of all time? ")

if answer.lower() == "muller":
    print('correct')
    score += 1
else:
    print("incorrect!")

answer = input("Messi has won a record number of Ballon d'Or awards - how many?  ")

if answer.lower() == "6":
    print('correct')
    score += 1
else:
    print("incorrect!")

print("You got " + str(score) + " question correct")