def greater(a, b, c):
    if a > b and a > c:
        return a
    elif c > a and c > b:
        return c
    else:
        return b


num1 = int(input("Enter 1st number : "))
num2 = int(input("Enter 2nd number : "))
num3 = int(input("Enter 3rd number : "))
bigger = greater(num1, num2, num3)
print(f"{bigger} is greater ")
