import random


print("Welcome to the number-guesser game!")
print("Try to guess a number from 1 to 100 in just 7 attemps.")
print("Type \"q\" at any moment to quit.")


    
def principal():
    i = 1
    num = random.randint(1,100)

    while i < 8:
        a = input("Try: ")

        if "." in a:
            print("Only hole number please!")
        elif "," in a:
            print("Only hole number please!")
        elif "-" in a:
            print("Only positive numbers please!")
            
        elif a == "q":
            quit()
            
        elif a == "Q":
            quit()
            
        elif "a" in a or "b" in a or "c" in a or "d" in a or "e" in a or "f" in a or "g" in a or "h" in a or "i" in a or "j" in a or "k" in a or "l" in a or "m" in a or "n" in a or "o" in a or "p" in a or "r" in a or "s" in a or "t" in a or "u" in a or "v" in a or "w" in a or "x" in a or "y" in a or "z" in a or "ñ" in a:
            print("Please type only numbers or \"q\" to quit!")
            print("Starting a new game...")
            print("________________")
            principal()
            
            
        elif "A" in a or "B" in a or "C" in a or "D" in a or "E" in a or "F" in a or "G" in a or "H" in a or "I" in a or "J" in a or "K" in a or "L" in a or "M" in a or "N" in a or "O" in a or "P" in a or "R" in a or "S" in a or "T" in a or "U" in a or "V" in a or "W" in a or "X" in a or "Y" in a or "Z" in a or "Ñ" in a:
            print("Please type only numbers or \"q\" to quit!")
            print("Starting a new game...")
            print("________________")
            principal()
            
        elif int(a) > num:
            print("The number is lower")
            i = i+1

        elif int(a) < num:
            print("The number is bigger")
            i = i+1
            
        
            
        elif int(a) == num:
            print("Well done!")
            print("You needed", i, "attemps to guess the number")
            print("________________")
            print("New game:")
#            print("\n")
            principal()
    
        

    print("You lost!")
    print("It was the number", num, "!")

principal()

