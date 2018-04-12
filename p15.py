#Jan Rodák
#znaky 
z=input("zadej znak : ")
if((z>="a")and(z<="z")):
    print("male pismeno")
elif((z>="A")and(z<="Z")):
    print("velke pismeno")
elif((z>="0")and(z<="9")):
    print("cislice")
else:
    print("jiny znak")
