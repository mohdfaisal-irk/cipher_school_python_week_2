# add and delete
user_info = {
    'name' : 'deepa',
    'age' : 24,
    'fav_movie': ['coco','kimi no na wa'],
    'fav_tunes':['awakening','fairy tale'],
}
# how to add data
# user_info['fav_songs'] = ['song1','song2']
# print(user_info)

# pop method
user_info.pop('fav_tunes')
print("popped item is {popped_item}")
print(user_info)
# popitem method
popped_item = user_info.popitem()
print(user_info)
print(popped_item)