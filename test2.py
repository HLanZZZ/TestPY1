# 列出2到100之间的素素

i = 2
while (i < 100):
    j = 2
    while (j <= (i/j)):
        if not(i%j): break
        j = j +1
    if (j > i/j): print(str(i)+'是素数')
    i = i +1

print('hh')