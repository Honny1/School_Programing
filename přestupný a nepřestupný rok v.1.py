#IF ELS
#rodak jan

print("p�estupn�")       
 	
rok=int(input("zadej rok: "))    
if(rok%100==0):
   if(rok%400==0):
         print("rok", rok," je p�estupn� ")
   else:
       print("rok", rok," je nep�estupn� ")
else:
   if(rok%4==0):
      print("rok", rok," je p�estupn� ")
   else:
      print("rok", rok," je nep�estupn� ")

input()      
