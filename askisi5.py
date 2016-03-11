Imerominia=raw_input("Parakalw dwste imerominia me tin eksis morfi dd/mm/yyyy").split('/')
mera=int(imerominia[0])
minas=int(imerominia[1])
etos=int(imerominia[2])
minas = (minas + 9) % 12
etos = etos - minas/10
mera= 365*etos + etos/4 - etos/100 + etos/400 + (minas*306 + 5)/10 + ( mera - 1 )
h = mera%7
if h==1:
   print = "Kyriaki"  
 elif h==2:
   print = "Deytera"
 elif h==3:
    print = "Triti"
 elif h==4:
   print = "Tetarti"
 elif h==5:
    print = "Pempti"
 elif h==6:
    print = "Paraskeyh"
 else:
    print = "Savvato"