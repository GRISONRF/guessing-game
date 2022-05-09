import random

#random number, range 1-100.
#store in a variable.
ram = random.randint(1,100)
#print(ram)


print ("Howdy, what's your name? ")
input_name = input("(type in your name)" )
print (f"{input_name}, I'm thinking of a number between 1 and 100. Try to guess my number.")
input_number = int(input("Your guess? "))
count = 1 


while input_number != ram:
    if input_number < ram:
        print("Your guess is too low, try again.")
    elif input_number > ram:
        print("Your guess is too high, try again.")  
    input_number = int(input("Your guess? "))
    count += 1
if input_number == ram:
    print(f"Well done, {input_name}! You found my number in {count} tries!")