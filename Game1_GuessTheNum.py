import random

start = 1
end = 100
value = random.randint(start,end)
print("Chose a number between ",start," and ",end)
guess = None
while guess != value:
    
    text=input("Guess the number:")
    guess = int(text)
    
    if guess < value:
        print("The number is higher:")
        
    elif guess > value:
        print("The number is lower:")

print("Congratulations you guessed the number")