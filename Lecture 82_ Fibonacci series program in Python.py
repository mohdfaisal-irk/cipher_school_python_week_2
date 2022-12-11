# Fibonacci series
# 0,1,1,2,3,,5,8,13,21,24

# for i in range(1, 11):
#     print(i)
#
# for i in range(1, 11):
#     print(i, end=" ")
def fibonacci_seq(n):
    a = 0 #first number
    b = 1 #second number
    if n ==1:
        print(a)
    elif n==2:
        print(a,b) #a,b,0
    else:
        print(a,b ,end=" ")
        for i in range(n-2):
            c=a+b
            a = b
            b = c
            print(b, end=" ")

fibonacci_seq(100)