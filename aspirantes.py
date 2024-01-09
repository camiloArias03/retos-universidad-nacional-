grupoa=""
grupob=""
herramientas=""
contadorb=0
contadora=0
cadena_salida=""
numero=0
numeroa=0
numerob=0

grupoa=input("Ingrese cuatro herramientas para el grupo A :")
grupoa=grupoa.upper()
grupob=input("Ingrese cuatro herramientas para el grupo B :")
grupob=grupob.upper()
herramientas=input("Ingrese las iniciales de las herramientas con mayor expereincia de cada uno de los aspirantes :")
herramientas=herramientas.upper()



def cad(contadora,contadorb):
 global cadena_salida
 if(contadora>contadorb):
  cadena_salida= "A"+cadena_salida
 elif(contadora<contadorb):
  cadena_salida= "B"+cadena_salida

 else:
  cadena_salida="E"+cadena_salida
 return cadena_salida
def comparar(comparara,compararb):
  global numero
  if contadora<contadorb:
   numero=contadorb
  elif contadora>contadorb:
   numero=contadora
  return numero
for i in herramientas:
 
 if(i in grupoa and i in grupob):
  contadora=contadora+1
  contadorb=contadorb+1
 elif(i in grupoa):
  contadora +=1

 elif(i in grupob):
  contadorb +=1

 else:
   comparar(contadora,contadorb)

 numeroa=numero+contadora
 numerob=numero+contadorb 
  

 cadena_salida=cad(numeroa,numerob)

print(cadena_salida[::-1])









