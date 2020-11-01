import math

def inputInt(message):
    number = input(message)
    if number.isdigit():
        return int(number)
    else:
        if number.startswith('-'):
            print("\nNumber must be positive.")
            return -1 # error code
        elif '.' in number:
            print("\nMust be a whole number.")
            return -1
        else:
            print("\nContains inappropriate characters.")
            return -1

def inputCorrect(message):
    while True:
        num = inputInt(message)
        if num != -1:
            return num
    
q = "y"

print("Hi Manager-nim!")
print("Let's calculate the number of gems you need to get an event card.")
print("For each question, type your answer and press Enter to confirm.")

while q == "y":
    items = [90,95,100,105,110]
    print("------------------------------------------------")
    goal = inputCorrect("\nNumber of items needed: ")
    cur = inputCorrect("\nCurrent number of items: ")      
    for n in range(2, 7):
        bonus = inputCorrect("\nNumber of bonus items for mission {}: ".format(n))
        items[n-2] += bonus
    while True:
        remdays = inputCorrect("\nHow many days left (maximum 14)?\n If you played all missions 3 times today,\n type the number of remaining days\n that appears on the event menu.\n Otherwise, add this number by 1. ")
        if remdays > 14:
            print("\nMaximum number of days left is 14.")
        else:
            break 
            
    bestMission = items.index(max(items)) + 2
    daily = 3*sum(items) # how many items can be acquired per day
    perReplay = 3*max(items) # how many items per 15 gems spent
    final = cur + remdays*daily # how many items if spend no gem
    rem = goal - final # remaining number of items
    print("\nYou will have {} items at the end of the event.".format(final))
    if rem <= 0:
        print("\nYou don't need to spend any gem. Yay!♥")
    else:
        nbreplays = math.ceil(rem/perReplay)
        print("{} items to go. Fighting!♥".format(rem))
        print("\nYou need {} gems. Replay mission {} {} times.".format(nbreplays*15, bestMission, nbreplays))
    q = input("Try again? (y)es/(n)o\n")
