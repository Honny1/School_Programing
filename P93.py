import math
def delka(x, x1, y, y1):
    a= ((x-x1)**2)+((y-y1)**2)
    math.sqrt(a)
    return a

x=int(input("zadej souøadnici x bodu 1: "))
x1=int(input("zadej souøadnici y bodu 1: "))
y=int(input("zadej souøadnici x bodu 2: "))
y1=int(input("zadej souøadnici y bodu 2: "))
a=delka(x, y, x1, y1)
print("vzdálenost bodù od sebe je:",a)