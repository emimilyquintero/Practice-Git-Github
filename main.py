



B= "suma"
C = "resta"
D= "division"
E="multiplicación"
t = input("ingrese el tipo ")
f= "este es el resultado de la ocperacion {} {} {} = {}"

if t == B :
  ta= int(input ("Ingrese sus numero "))
  ts= int (input("Ingrese sus numero "))
  Result= ta+ts
  txt= "Resultado es {:.2f}"
  print  (txt.format(Result))

elif t==C :
  ta= int(input ("Ingrese sus numero "))
  ts= int (input("Ingrese sus numero "))
  Result= ta-ts
  txt= "Resultado es {:.2f}"
  print  (txt.format(Result))
elif t==D :
  ta= int(input ("Ingrese sus numero "))
  ts= int (input("Ingrese sus numero "))
  Result= ta/ts
  txt= "Resultado es {:.2f}"
  print  (txt.format(Result))
elif t== E :
  ta= int(input ("Ingrese sus numero "))
  ts= int (input("Ingrese sus numero "))
  Result= ta*ts
  txt= "Resultado es {:.2f}"
  print  (txt.format(Result))
else :
  print ("Error")