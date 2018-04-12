import random
import string


opak=1 
while (opak==1):
  tazena=[]
  zadane=[]
  shod=0
  dodatkovesedi=0

  tazena=(random.sample(range(1,50), 7))
  dodatkove=tazena[6]
  tazena.pop()
  
  print (tazena) #pouze pro overeni funkcnosti programu
   
  
  print (dodatkove) #take pouze pro overeni
  asd=int(input("Zadej cislo 1-49: "))
  while (asd>49 or asd<1):
    asd=int(input("Zadej nove cislo: "))
  zadane.append(asd)
  for z in range(5):    
    zadavani=(int(input("Zadej cislo 1-49: ")))
    f=z+1
    for j in range(f):
      xx=True
      while(xx):
            if zadane[j]==zadavani:
              zadavani=(int(input("Zadej nove cislo: ")))
            elif zadavani>49:
              zadavani=(int(input("Zadej nove cislo: ")))
            elif zadavani<1:
              zadavani=(int(input("Zadej nove cislo: ")))
            else:
              xx=False
    zadane.append(zadavani)
          
    

  print (zadane)
            
  
  for a in range(6):
    for b in range(6):
      if zadane[a]==tazena[b]:
        shod=shod+1
  
  if (shod==6):
    print ("Uhodnul jsi 6 cisel a vyhral jsi prvni cenu!")
  elif (shod==5):
    for c in range(6):
      if zadane[c]==dodatkove:
        dodatkovesedi=1
        
    if dodatkovesedi==1:
      print ("Uhodnul jsi 5 cisel + dodatkove a vyhravas druhou cenu!")
    else:
      print ("Uhodnul jsi 5 cisel a vyhravas treti cenu!")
      
  elif (shod==4):
    print ("Uhodnul jsi 4 cisla a vyhral jsi ctvrtou cenu!")
  elif (shod==3):
    print ("Uhodnul jsi 3 cisla a vyhral jsi patou cenu!")
  else:
    print ("Uhodnul jsi malo cisel, a tak jsi nic nevyhral!")
  
  opak=input("Chces opakovat? 1/0: ")

  
    
   
   
  