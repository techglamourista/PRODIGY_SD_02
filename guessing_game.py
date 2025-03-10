import random

number=random.randint(1,100)
attempts=0

print("Welcome to the Guessing Game")
print("Try to guess the number between 1 to 100.")
print("I've chosen a secret number. Time to test your psychic abilities!")

while True:
    guess=int(input("Enter your guess!:"))
    attempts+=1
    
    if guess > number:
        print(" Whoa, Too Highh! Try Again Maybe you should aim lower? 😜")
    
    elif guess<number:
        print("Oops, Too Low! :( Aim higher, the sky is the limit! In this case, it's until 100! 🚀")
    
    else:
        print("YAYY 🎉 You guessed the number",number,"It took you",attempts,"attempts! Well done, genius! 🧠✨!!!!")
        break
