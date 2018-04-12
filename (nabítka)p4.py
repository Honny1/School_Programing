#Jan Rodák
#nabítka
print("++++++  vyber matematickou operaci  ++++++++++\n")     
print("+ scítani")
print("- odcitani")
print("* nasobeni")
print("/ deleni")
print("\n")	                                    
a=int(input("zadej cislo A : "))
b=int(input("zadej cislo B : "))
x=input("vyber matematickou operaci : ")  	 
if x=="+":
	print("soucet:",a+b)
elif x=="-":
	print("rozdil je:",a-b)
elif x=="*":
	print("soucin je:",a*b)	
elif x=="/":
	print("dodil je:",a/b)

else:
	print("chybne zadana matematicka operace")
