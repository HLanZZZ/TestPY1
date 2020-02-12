# 练习使用dict字典的使用,也就是其他语言中的map

dict = {'laozhu': 75, 'huazai': 0.1, 'conger': 213}
# 添加key-value
print(dict)
# 判断是否存在某个key
print('tomas' in dict)
# 通过dict提供的get()方法，如果key不存在，可以返回None，或者自己指定的value
dict.get('laozhu')
print(dict)
# 通过pop(key)删除某一个key的值
dict.pop('huazai')
print(dict)

# python中同样存在set和java中set的特性一致，无序不重复
s = set([1,2,1,2,3,4])
print(s)

# test: (1,2,3) 和 (1,[2,3]) 放进tuple和set中去
tup = (1,2,3,1,[2,3])
print(tup)
# unhashable type: 'list'
# se = set([1,2,3,1,[2,3]])
se2 = set([1,2,3,1])
# print(se)
print(se2)
