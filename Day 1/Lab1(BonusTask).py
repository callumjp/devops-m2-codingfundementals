from time import sleep

print("Hello! Walcome to my extra special bonus task! :)")
print("Pausing for effect...")
sleep(2)

print("Please give me two numbers to add together")
no1 = input("Number 1: ")
no2 = input("Number 2: ")

no1 = int(no1)
no2 = int(no2)

sleep(2)

print("Right, now should we multiply, add, or subtract them?")
operation = input("What would you like to do?: ")

sleep(1)

if operation == "add":
    result = no1 + no2
    sleep(1)
    print("Result:",(result))
elif operation == "subtract":
    result = no1 - no2
    sleep(1)
    print("Result:",(result))
elif operation == "multiply":
    result = no1 * no2
    sleep(1)
    print("Result:",(result))
elif operation == "divide":
    result = no1 / no2 
    sleep(1)
    print("Congratulations! You found the secret answer. The answer is...",(result))
else:
    sleep(1)
    print("Hmmm... What does that mean...")
    sleep(3)
    print("Sorry, I don't understand")

sleep(1)
print("This is the end of my script I hope you liked it")