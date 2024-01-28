print("Welcome to my computer quiz!")

playing = input("Do you want to play a game?")

if playing.lower() != "yes":
    quit()

print("Okay! let's play :)")
score = 0

answer = input("What is the acronym for central processing unit? ")
if answer.lower() == "cpu":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is the acronym for graphics processing unit? ")
if answer.lower() == "gpu":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is the acronym for random access memory? ")
if answer.lower() == "ram":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is the acronym for power supply unit? ")
if answer.lower() == "psu":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")


print("You got " + str(score) + " questions correct!")
print("You got " + str((score/4) * 100) + "%")