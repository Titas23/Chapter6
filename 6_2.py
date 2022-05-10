import random



# elements = [
#     "earth",
#     "air", 
#     "fire", 
#     "water"]
# print(random.choice(elements))
# print(random.sample(elements, 2))
# random.shuffle(elements)
# print(elements)
# print(random.randint(1,5))


# def main():
#     bankroll = int(input("Enter the amount of the bankroll: "))
#     (amount, times_played) = play_double_or_nothing(bankroll)
#     print("Ending bankroll:", amount, "dollars")
#     print("Number of games played:", times_played)

# def is_odd(n):
#     if(1 <= n <= 36) and (n % 2):
#         return True
#     else:
#         return False

# def profit(n):
#     if is_odd(n): 
#         return 1
#     else:
#         return -1

# def play_double_or_nothing(bankroll):
#     amount = bankroll
#     times_played = 0 
#     while 0 < amount < 2 * bankroll:
#         n = random.randint(0, 37)
#         times_played += 1 
#         amount += profit(n)
#     return (amount, times_played)

# main()

def main():
    for i in range(0, 3):
        spin()
    

def spin():
    rand_num = random.randint(1, 20)
    output = ""
    if (rand_num > 15):
        output = "Cherries"
    elif(rand_num > 10):
        output = "Orange"
    elif(rand_num > 5):
        output = "Plum"
    elif(rand_num > 2):
        output = "Melon"
    elif(rand_num > 1):
        output = "Bell"
    else:
        output = "Bar"

    print(output, end=" ")

main()