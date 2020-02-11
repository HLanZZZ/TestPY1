# 练习使用list

classmates = ['laozhu', 'huazai', 'laoluo']

print(classmates[-1])

classmates.append('conger')
print(classmates)
classmates.reverse()
print(classmates)
classmates.remove('laozhu')
print(classmates)
classmates.insert(3, 'laozhu')
print(classmates)
# 要删除指定位置的元素可以通过使用pop(i)方法pop()默认删除最后一个元素
classmates.pop()
print(classmates)
# list里面的元素也可以不同
L = ['laozhu', 22, 174.8, True]
# list中元素也可以是list
l = ['laozhu', 22, ['huazai', 12], 10.2]


# 另外还有一种有序列表叫元组 -- tuple -- tuple和list非常相似，区别在于tuple里面的元素不可变
classmates2 = ('laozhu', 'laozhang', 'huazai', 'luoyong')



