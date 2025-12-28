import random
target=random.randint(1,100)
while True:
    userchoice=input("Gauss the target :")
    if(userchoice=="Quit"):
        break
    userchoice=int(userchoice)
    if(userchoice==target):
        print("Success : Correct Guess!!")
        break
    elif(userchoice<target):
        print("Yiur number was too small.Take a bigger guess....")
    else:
        print("your number is was too big.Take a smaller guess....")

print("==========GAME OVER============")
       
