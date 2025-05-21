def es_vocal(car):
    if car.lower() in "aeiou":
        return True

    return False


#carga de archivo
archivo = open("Texto.txt", "rt")
contenido = archivo.read()  #lectura del archivo

#contador de letras
cl = 0
clt = 0
pa = 0
cv = 0

#contador de palabras
cp = 0
cpv = 0


for car in contenido:
    if car == "." or car == " " :
        if cl > 0:
            cp += 1
        # 4 fin de palabra

        #5 reiniciar contadores
        if cl > pa:
            pa = cl

        if cv > 2:
            cpv += 1


        cl = cv = 0


    else:
        cl += 1
        clt += 1

        if es_vocal(car):
           cv += 1

        # 3 dentro de la palabra

#calcular y mostrar resultado
promedio = 0

if cp != 0:
    promedio = clt // cp


print("cantidad de palabras: ", cp)
print("cantidad de letras promedio: ", promedio)
print("longitud de la palabra mas larga: ", pa)
print("palabras con mas de 2 vocales ", cpv)