# fromkeys
# d = {'name' : 'unknown', 'age': 'unknown'}

d = dict.fromkeys(['name','age'],['unknown','unknown'])
# print(d)
#
# # get methode(useful)
d = {'name': 'deepa das','age':'17'}
# # print(d['name'])
# print(d.get('age'))
#
# if d.get('age'):
#     print('present')
# else:
#     print('not present')
d1 = d.copy()
print(d1)
print(d1.popitem())

# print(d1 is d)

