#!/usr/bin/env python
# coding: utf-8

# In[139]:


import random


def get_random_number():
    # Helper Function - 지우지 말 것
    # 100부터 999까지 수를 램덤하게 반환함
    return random.randrange(100, 1000)


def is_digit(user_input_number):
    return user_input_number.isdigit()


def is_between_100_and_999(user_input_number):
    return True if (100<=int(user_input_number)<1000) else False


def is_duplicated_number(three_digit):
    if len(set(three_digit)) < len(three_digit):
        return True
    else:
        return False

def is_validated_number(user_input_number):
    if is_digit(user_input_number) and is_between_100_and_999(user_input_number) and not is_duplicated_number(user_input_number):
        return True
    else:
        return False


def get_not_duplicated_three_digit_number():
    while 1:
        num = get_random_number()
        if not is_duplicated_number(str(num)):
            return num


def get_strikes_or_ball(user_input_number, random_number):
    strikes, ball = 0, 0
    if user_input_number == random_number:
        strikes = 3
    else:
        for num in user_input_number:
            if num in random_number:
                if user_input_number.index(num) == random_number.index(num):
                    strikes += 1
                else:
                    ball += 1
    return strikes, ball
    


def is_yes(one_more_input):
    while 1:
        temp = one_more_input.lower()
        if temp == 'y' or temp == 'yes':
            return True
        elif temp == 'n' or temp == 'no':
            return False
        else:
            print("Wrong Input, Input again")
            one_more_input = input("You win, one more(Y/N) ?")
            



def is_no(one_more_input):
    while 1:
        temp = one_more_input.lower()
        if temp == 'n' or temp == 'no':
            return True
        elif temp == 'y' or temp == 'yes':
            return False
        else:
            print("Wrong Input, Input again")
            one_more_input = input("You win, one more(Y/N) ?")
    


def main():
    print("Play Baseball")
    user_input = 999
    
    while 1:
        random_number = str(get_not_duplicated_three_digit_number())
        print("Random Number is : ", random_number)
        breaker = False
        while 1:
            user_input = input('Input guess number : ')
            if is_validated_number(user_input):
                strikes, ball = get_strikes_or_ball(user_input, random_number)
                print(f"Strikes : {strikes} , Balls : {ball}")
                if strikes == 3:
                    ans = input("You win, one more(Y/N) ?")
                    if is_no(ans):
                        break
                    else:
                        breaker = True
                        break

            else:
                print("Wrong Input, Input again")
        if not breaker:
            break
    
    print("Thank you for using this program")
    print("End of the Game")

if __name__ == "__main__":
    main()

