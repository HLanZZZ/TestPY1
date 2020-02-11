# 计算题，熟练使用数组以及while条件判断
from pip._vendor.distlib.compat import raw_input

i = int(raw_input('净利润:'))
arr = [1000000,600000,400000,200000,100000,0]
rat = [0.01,0.015,0.03,0.05,0.075,0.1]
r = 0
while (i >= arr[0]):
    r = i*rat[0]
    break
while (i >= arr[1]):
    r = i * rat[1]
    break
while (i >= arr[2]):
    r = i * rat[2]
    break
while (i >= arr[3]):
    r = i * rat[3]
    break
while (i >= arr[4]):
    r = i * rat[4]
    break
while (i >= arr[5]):
    r = i * rat[5]
    break
print (r)