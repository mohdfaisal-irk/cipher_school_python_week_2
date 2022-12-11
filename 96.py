# example
# [1,2,3,4]----> [4,3,2,1]
# ['word1','word2']----> ['word2','word1']

# def reverse_list(l):
#     l.reverse()
#     return l
#
# numbers = [1,2,3,4]
# popped_item = numbers.pop()
#
# print(reverse_list(numbers))

def reverse_list(l):
    r_list = []
    for i in range(1, len(l)):
        popped_item = l.pop()
        r_list.append(popped_item)
    return r_list
numbers = [1,2,3,4,5]

