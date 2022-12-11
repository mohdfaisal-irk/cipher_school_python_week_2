def reverse_elements(l):
    element = []
    for i in l:
        element.append(i[::-1])
    return element

word = ['abc','tuv','xyz']
print(reverse_elements(word))


