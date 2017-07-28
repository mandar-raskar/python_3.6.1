name = input("Enter the name :")
love_num = int(input("enter the num you love :"))
num1 = int(input("enter 1st number"))
num2 = int(input("enter 2nd number"))

def person(love_num):
    if num1 + num2 == love_num:
        print("love")
    elif num1 - num2 == love_num:
        print("love")
    elif num2 - num1 == love_num:
        print("love")
    else:
        print("hate")
    return person

print(person(love_num))