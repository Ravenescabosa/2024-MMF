# function goes here

# check that  user response is not blank
def not_blank(question):
    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"

        elif response == "no" or response == "n":
            return "no"

        else:
            print("Please enter yes or no")


# main routine  goes here
while True:
    name = not_blank("Please enter your name or 'xxx' to quit: ")
    if name == "xxx":
        break

print("We are done")
