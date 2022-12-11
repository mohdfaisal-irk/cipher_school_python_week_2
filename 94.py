# generate lists with range function
# something more about pop method
# index method
# pass list to a function

numbers = [1,2,3,4,5,6,7,8,9,10]
# print(numbers)

# pop method
# print(numbers.pop())
# popped_item = numbers.pop()
# print(numbers.index(3))

def negative_list(l):
    negative = []
    for i in l:
        negative.append(-i)
    return negative

print(negative_list(numbers))