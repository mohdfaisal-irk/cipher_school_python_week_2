# function inside a function
# greater (a,b) ----> a or b
# greater (a or b, c) ------> greatest
def greater(a, b):
    if a > b:
        return a
    else:
        return b


def new_greatest(a, b, c):
    bigger = greater(a, b)
    return greater(bigger, c)


num1 = int(input("Enter 1st number : "))
num2 = int(input("Enter 2nd number : "))
num3 = int(input("Enter 3rd number : "))
print(new_greatest(num1, num2, num3))

# kiss ---> Keep It simple stupid
