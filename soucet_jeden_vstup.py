Int=[]
x=input("Zadej čisla(odděluj ;):")
str=x.split(";")
for i in range (len(str)):
    Int.append((int(str[i])))
print("sočet",sum(Int))