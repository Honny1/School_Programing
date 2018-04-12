#Jan Rodák
print("++++++  spojeni retezcu  ++++++\n")    
print("\n")	                               
a="sedmikraska" 
b="" 
c="kvete"
d=" "
print("delky retezce A", len(a),"\ndelky retezce B", len(b),"\ndelky retezce C", len(c),"\ndelky retezce D",len(d),"\n\n",a+d+c,"\n",a+d+a+d+c+d+c+d+c,"\n\nobsahují retezce C znaky A=","a" in c,"G=","g" in c,"\nobsahují retezce B znaky A=","a" in b,"G=","g" in b,"\n\ntreti znak retezce a",a[3],"\npaty znak retezce a:", a[5],"\nprvni znak retezce:",c[0],"\npredposledni znak retezce:", c[:len(c)-2],"\n\n","èasti:""\ndo 5. znaku:",a[0:5],"\nod 3 do 7:",a[3:7],"\nod 2. do konce:",a[2:],"\nbez poslednich 4:",a[:len(a)-4])