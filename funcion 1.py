#Trate de meter todos los if en un for pero nose si esta bien, si lo pueden chequerar piola
def calcular_monto_final(codigo_iso, monto_nominal):
    mensaje = ""
    monto_base = 0
    monto_final = 0
    
    # no sabia si tenia que repetir la tupla asi que la deje
    monedas = ("ARS", "USD", "EUR", "GBP", "JPY")
    tasas = (5, 7, 7, 9, 0)  # JPY tiene variables especiales con valores no enteros asi que no lo inclui aca

    # Procesar las primeras 4 monedas (no JPY)
    for i in range(4):  # Las primeras 4 monedas tienen procesamiento simple
        if codigo_iso == monedas[i]:
            mensaje = "Moneda valida"
            comision = round((monto_nominal * tasas[i]) / 100, 2) #NOTA 2: che el 2 ese que esta en cada comision pora que era, seguro que hiba¿? (Ulises)
            monto_base = monto_nominal - comision
            break

    # Caso especial para JPY (índice 4 en la tupla)
    if codigo_iso == monedas[4]:
        if monto_nominal >= 15000:
            mensaje = "Moneda valida"
            # Usar un for para determinar la tasa según el monto
            rangos_monto = (500000, 1500000, 10000000, float('inf'))
            tasas_jpy = (9, 7.8, 5.5, 5)

            for j in range(len(rangos_monto)):
                if monto_nominal <= rangos_monto[j]:
                    comision = round((monto_nominal * tasas_jpy[j]) / 100, 2)
                    if comision > 950000:
                        comision = 950000
                    monto_base = monto_nominal - comision
                    break
        else:
            mensaje = "Monto minimo para JPY no alcanzado"
            monto_base = 0
    elif mensaje == "":  # Si no se encontró ninguna moneda válida
        mensaje = "Moneda no autorizada"
        monto_base = 0

    if monto_base > 500000:
        impuesto = (monto_base * 21) / 100
        monto_final = monto_base - impuesto
    else:
        monto_final = monto_base
    
    # Retornar monto_final solo si moneda es válida y monto_base > 0
    if mensaje == "Moneda valida" and monto_base > 0:
        return monto_final
    else:
        return 0

def operaciones_validas(monto_final):
    c1 = suma_monto_final = 0
    c1 += 1
    suma_monto_final += round(monto_final, 2) #Agrege el redondeo a la suma
    return c1, suma_monto_final


def extraer_datos_linea(linea):
    nombre = linea[0:20]
    codigo_id = linea[20:30]
    codigo_orden = linea[30:40]
    monto_nominal = linea[40:50]
    alg_comision = linea[50:52]
    alg_impuesto = linea[52:54]

    return nombre, codigo_id, codigo_orden, monto_nominal, alg_comision, alg_impuesto


def es_destinatario(codigo_id):
     valides = False
    letras = 0
    guiones = 0

    for car in codigo_id:
        if car == " ":
            continue

        letras += 1

        if "A" <= car <= "Z" or "0" <= car <= "9":
            valides = True
            continue

        if car == "-":
            guiones += 1
            continue

        else:
            valides = False
            break
    if guiones == letras:
        valides = False

    return valides

def es_moneda(codigo):
    existe = None
    monedas_encontradas = 0

    codigo_iso = ("ARS", "USD", "EUR", "GBP", "JPY")
    for moneda in codigo_iso:
        if moneda in codigo:
            if existe is None:
                existe = moneda
                monedas_encontradas = 1

            elif existe != moneda:
                monedas_encontradas += 1

    if monedas_encontradas != 1:
        return False

    else:
        return True


def cantidad_operaciones(valides):
    ct1 = ct2 = ct3 = ct4 = ct5 = 0
    if valides == ('ARS' or 'USD' or 'EUR' or 'GBP' or 'JPY'):
        if valides == 'ARS':
            ct1 += 1
        if valides == 'USD':
            ct2 += 1
        if valides == 'EUR':
            ct3 += 1
        if valides == 'GBP':
            ct4 += 1
        if valides == 'JPY':
            ct5 += 1
        print('moneda valida')
        return
    else:
        print('moneda invalida')


def principal():
    
    c_monedas_invalidas = 0
    c_dest_invalidos = 0

    linea_1 = True
    archivo = open("ordenes25.txt", "r")
    for linea in archivo:
        if linea_1 is True:
            linea_1 = False
            continue

        nombre, codigo_id, codigo_iso, monto_nominal, alg_comision, alg_impuesto = extraer_datos_linea(linea)

#me parece que hay una forma de simplifcar esto pero ya estoy muy quemado chicos im going insane

        if not es_moneda(codigo_iso) and not es_destinatario(codigo_id):

            c_monedas_invalidas = contar(c_monedas_invalidas)

        elif not es_moneda(codigo_iso):
            c_monedas_invalidas = contar(c_monedas_invalidas)

        if not es_destinatario(codigo_id):
            c_dest_invalidos = contar(c_dest_invalidos)

    archivo.close()

    print(' (r1) - Cantidad de ordenes invalidas - moneda no autorizada:', c_monedas_invalidas)
    print(' (r2) - Cantidad de ordenes invalidas - beneficiario mal identificado:', c_dest_invalidos)


principal()
