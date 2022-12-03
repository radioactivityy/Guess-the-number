import random

give_number = int(
    input(" What do you think the number will be?\n "))
guess_number = 1
guessList = []
guessList.append(give_number)

number = random.randint(1, 10)
while give_number != number:
    if give_number > number:
        give_number = int(
            input("Sorry, that answer is too high! Try again!\n "))
        #guess_number = guess_number + 1
        if give_number not in guessList:
            guessList.append(give_number)
    if give_number < number:
        give_number = int(
            input("Sorry, that answer is too low! Try again!\n "))
        #guess_number = guess_number + 1
        if give_number not in guessList:
            guessList.append(give_number)

if give_number not in guessList:
    guessList.append(give_number)
print("Congratulations, you were right, the answer was {}! It took you {} tries.".format(
    number, len(guessList)))
