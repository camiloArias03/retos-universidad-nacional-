sindicato_s=""
sindicato_u=""
votos = ""
cadena_salida = ""
contadors = 0
contadoru = 0
resultados = ""

sindicato_s = input("Ingrese las letras de los sindicato S: ")
sindicato_s = sindicato_s.upper()
sindicato_u = input(("Ingrese las letras de los sindicato U: "))
sindicato_u = sindicato_u.upper()
votos=input("Ingrese los las letras de los sindicatos")
votos=votos.upper()


for resultados in votos:

    if (resultados in sindicato_s and resultados in sindicato_u):
        contadors = contadors +1
        contadoru = contadoru  +1
    elif (resultados in sindicato_s):
        contadors += 1
    elif (resultados in sindicato_u):
        contadoru += 1

    if (contadors > contadoru):
        cadena_salida= cadena_salida  + "S"
    elif (contadoru > contadors ):
        cadena_salida = cadena_salida +  "U"
    elif (contadoru == contadors ):
        cadena_salida =  cadena_salida + "N"

print(cadena_salida)