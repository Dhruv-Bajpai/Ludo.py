
import random 

a = 50

print('its a TERMINAL LUDO type Y if you want to run OR N to break AND if anyone of both will get 50 in sum then he will win ')

computer_sum= 0 
user_sum=0

while user_sum <= a or computer_sum <=a:
    computer_choice= random.randint(1,6)
    print(f' computer chooses  {computer_choice}')
    computer_sum += computer_choice
    if computer_sum >= 50:
        print('computer won')
        break

    user=input('enter Y or N ')
    if user=='Y':
        user_choice=random.randint(1,6)
        print(f'user chooses : {user_choice}')
        user_sum += user_choice
        if user_sum >= 50:
            print('user wins')
            break
    else:
        break