import random
lst=[1,2,3]
computer_count=0
user_count=0
i=0
while i!=10:
    choice = random.choice(lst)
    #user input
    select=int(input("\npress 1. for Rock\n 2. for paper\n 3. for scissor'\n"))
    #if input is invalid
    if 0> select or select >3:
        print("invalid input")
        continue
    #when computer selects stone
    if choice==1:
        print("compputer selected rock")
        if select==1:
            print("same choice")
            i+=1
        elif select==2:
            print("you won!")
            user_count+=1
            i+=1
        else:
            print("computer won!")
            computer_count+=1
            i+=1
    #when computer selects paper
    elif choice==2:
        print(f"computer selected paper")
        if select==2:
            print("same choice")
            i+=1
        elif select==3:
            print("you won!")
            user_count+=1
            i+=1
        else:
            print("computer won!")
            computer_count+=1
            i+=1
    #when computer selects scissor
    else:
        print(f"compputer selected scissor")
        if select==3:
            print("same choice")
            i+=1
        elif select==1:
            print("you won!")
            user_count+=1
            i+=1
        else:
            print("computer won!")
            computer_count+=1
            i+=1
#whole round result
print(f" you won {user_count} times and computer won {computer_count} times")
if computer_count>user_count:
    print("computer won the round.")
elif user_count>computer_count:
    print("you won the round!")
else:
    print("round tie!")
