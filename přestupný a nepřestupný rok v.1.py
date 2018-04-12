#IF ELS
#rodak jan

print("pøestupný")       
 	
rok=int(input("zadej rok: "))    
if(rok%100==0):
   if(rok%400==0):
         print("rok", rok," je pøestupný ")
   else:
       print("rok", rok," je nepøestupný ")
else:
   if(rok%4==0):
      print("rok", rok," je pøestupný ")
   else:
      print("rok", rok," je nepøestupný ")

input()      
