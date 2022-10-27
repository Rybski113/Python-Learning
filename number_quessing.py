import random 

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print('Please type a number larger than 0 next time. ')
        quit()
else:
    print('Please type a number next')  
    quit()      

random_number = random.randint(1, top_of_range)

while True:
    user_quess = input("make a quess: ")
    if user_quess.isdigit():
       user_quess = int(user_quess)

    
    else:
       print('Please type a number next')  
    continue

    if user_quess == random_number:
        print("You got it!")
    else:
        print("You got it wrong!")    
