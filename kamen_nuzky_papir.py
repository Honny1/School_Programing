import random
print("1 - kamen, 2 - nuzky, 3 - papir")
aůersgjsrt=int(input("zadej svoji volbu:"))
asdfzusehrf= random.randint(1, 3)
if (aůersgjsrt==1 and asdfzusehrf==3):
    print("lose")
elif(aůersgjsrt==2 and asdfzusehrf==1):
    print("lose")
elif(aůersgjsrt==3 and asdfzusehrf==2):
    print("lose")
elif(asdfzusehrf==aůersgjsrt):
    print("remiza")
elif(aůersgjsrt<1 or 3<aůersgjsrt):
    print("jsi autista co neumí napsat na klavesnici jedna, dva nebo tři")
else:
    print("win")