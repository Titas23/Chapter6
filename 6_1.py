import util

# util.help()


# x = 23

# print("23".endswith("3"))

# infile = open("Textese.tx", 'r')



# my_list = [1, 2, 3, 4, 5 ]

# not_exist= my_list[3]

# print(not_exist)

# y = "2,3,4".split(",")
# x = len(y)

# print(x)

# print(6/2)

# print(1/0)

prompt = "Enter number of dependents: "

try:
    num_dependents = int(input(prompt))
    print(num_dependents)
except ValueError as err:
    print(err)
    print("You need to type in a number")

