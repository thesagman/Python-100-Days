# Day 2 - 100 Days of Code : Input and Variables


# Taking User Input

# input("What's your Name?")
# This message appears and the console waits for the user to type and press enter


# Need for Variables

# Now What the problem in the above line of code is that yeah you might be 
# putting something in the console and as soon as you would press enter
# the file would have executed and what you wrote would be forgotten
# thus here comes the need of variables
myName = input("What's your Name? : ")
myAge = input("How old are you? : ")
print("Gee, that's REALLY OLD")
replit = input( "Do you like Replit? : ")
print("OF COURSE YOU DO")
print()
# Variables are like containers



# Printing a Variable
print("So you are")
print(myName)
print("and are the ripe old age of")
print(myAge)
print("and clearly think that replit is")
print(replit)


# Common Coding Errors

1.  # my variable = input("who goes there?")
    # Note :- Syntax errors()

2.  # myGrandma = input("Hows your Grandma Doing? ")
    # print(mygrandma)
    # NameError: name 'mygrandma' is not defined.
    
    
    
3.  # myLunch = input( "What are you having for lunch? ")
    # print("Hmm, it sounds like you really should just order")
    # print("myLunch")
    # print("as soon as")
    # Logical error as you weren't printing the variable instead you wrote it in the quotes
    # and i hope you remember what happens when you write something in quotes
    
# DO REMEMBER : There can be more kinds of error that you will know when you will keep experimenting



########################################################################################


# Day 2 - Challenge

# Problem : Ask some things from the user and get the data printed as the way the Replit guy wanted 

# Solution

print("Getting to know you!")
print()
myName = input("What's your name?: ")
FavFood = input("What's your favourite food?: ")
FavMusic = input("What's your favourite music?: ")
Youlive = input("Where do you live?: ")
print()
print("You are")
print(myName)
print("You're probably hungry for")
print(FavFood)
print("and you're definitely getting your groove on to")
print(FavMusic)
print("living in the amazing")
print(Youlive)


