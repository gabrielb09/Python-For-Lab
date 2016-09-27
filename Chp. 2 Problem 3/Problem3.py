#INSTRUCTION: Run the program, input the equatons you would like to have answered by typing a single character "a" "b" or "c", you can also type "quit" to abort the program
import math
#solves equation A
eqA = (2+math.exp(2.8))/(math.sqrt(13)-2)
#solves equation B
eqB = (1-(1+math.log(2))**(-3.5))/(1+math.sqrt(5))
#solves equation C
eqC = math.sin((2-math.sqrt(2))/(2+math.sqrt(2)))
#defines a varable for the string "a"
a = "a"
#defines a varaiable for the string "b"
b = "b"
#defines a variable for the string "c"
c = "c"
#predefines a varaible choice to later accept the input of the user
choice = "a"
#loops until the user decides to quit
while choice != "quit":
    #request the user slecet the question they want to print
    choice = raw_input("would you like to answer equation a, b, c, or quit?")
    #prints the users selection
    if choice == a:
        print(eqA)
    if choice == b:
        print(eqB)
    if choice == c:
        print(eqC)
