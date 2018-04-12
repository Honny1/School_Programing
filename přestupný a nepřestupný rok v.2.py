#IF ELS
#rodak jan

print("přestupnýv2") 
rok=int(input("zadej rok: "))

if (rok%100==0):
    if(rok%400==0):
         print("rok",rok,"je přestupný ")
    else:
        print("rok",rok,"nenípřestupný ")
else:
    if(rok%4==0):
        print("rok",rok,"je přestupný ")
    else:
        print("rok",rok,"nepřestupný ")
input()
