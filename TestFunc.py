# 关于一些内部函数的调用，和自定义函数的编写
# abs()函数为绝对值函数
import math

print(abs(123))
print(abs(-1))
# 练习使用hex()函数得出某整数的16进制
n1 = 255
n2 = 1000
print(str(hex(n1)))
print(str(hex(n2)))

# 自定义函数
def my_func(x):
     if x >= 0:
         return x
     else:
         return -x

print(my_func(1))
print(my_func(-2))

# 空函数  pass 关键字为一个占位符，同时可以让某一进程直接通过，让程序运行正常。
def blank():
    pass

# 如果想要返回多个值

def my_func2(x, y, step, angle = 0):
    nx = x + step*math.cos(angle)
    ny = y + step*math.sin(angle)
    return nx,ny
print(my_func2(2,-3,6,90))

# 总结：
# 定义函数时，需要确定函数名和参数个数；
#
# 如果有必要，可以先对参数的数据类型做检查；
#
# 函数体内部可以用return随时返回函数结果；
#
# 函数执行完毕也没有return语句时，自动return None。
#
# 函数可以同时返回多个值，但其实就是一个tuple。

# 练习： 计算一元二次方程式 ax^2 + bx + c = 0

def quadratic(a, b, c):
    if not isinstance(a, (int)):
        raise TypeError('bad operand type')
    if not isinstance(b, (int)):
        raise TypeError('bad operand type')
    if not isinstance(c, (int)):
        raise TypeError('bad operand type')
    x1 = (-b + math.sqrt(b**2 - 4*a*c))/2*a
    x2 = (-b - math.sqrt(b**2 - 4*a*c))/2*a
    return x1, x2
print(quadratic(2,3,1))
# test success
