print("**** cely soub:**********************")
f=open("poznamka.txt","r")         
soubor = f.read()                
print(soubor)                    
f.close()                     

f=open("novy.txt","w")        
text=input("Zadejte text: ")
f.write(text+"\n")                                    
text=input("Zadejte text: ")
f.write(text+"\n")
f.close()   


f=open("velky.txt","w")          
x=open("poznamka.txt","r")
soubor = x.read()                
velke=str.upper(soubor)         
f.write(velke)                   
f.close()  
x.close()

d=0
f=open("poznamka.txt","r")  
for radek in f:                 
    d+=1
f.close()    
print("poet radku:",d)

f=open("velky.txt","a")
text=input("Zadejte text: ")
f.write(text+"\n") 
f.close()


f=open("velky.txt","a")
x=open("novy.txt","r")
soubor = x.read()
f.write(soubor)
f.close()
x.close()