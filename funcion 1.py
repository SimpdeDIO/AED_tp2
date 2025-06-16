# Trate de meter todos los if en un for pero nose si esta bien, si lo pueden chequerar piola
def actu_bene_prim_oper(nombre_actual, nombre_primera_operacion, cantidad_apariciones_beneficiario):
    if nombre_primera_operacion is None:
        nombre_primera_operacion = nombre_actual
    if nombre_actual == nombre_primera_operacion:
        cantidad_apariciones_beneficiario += 1
    return nombre_primera_operacion, cantidad_apariciones_beneficiario #Funcion de Actividad 5


def calcular_monto_base(monto_nominal, alg_comision):
    comision = calcular_comision(alg_comision, monto_nominal)
    monto_base = monto_nominal - comision
    return monto_base


def calcular_monto_final(monto_base, alg_impuesto):
    impuesto = calcular_impuesto(monto_base, alg_impuesto)
    monto_final = monto_base - impuesto

    return monto_final


def calcular_impuesto(monto_base, codigo):
    impuesto = 0
    if codigo == 1:
        if monto_base <= 300000:
            impuesto = 0
        elif monto_base > 300000:
            excedente = monto_base - 300000
            impuesto = (25 / 100) * excedente

    elif codigo == 2:
        if monto_base < 50000:
            impuesto = 50
        elif monto_base >= 50000:
            impuesto = 100

    elif codigo == 3:
        impuesto = (3 / 100) * monto_base

    return impuesto


def calcular_comision(codigo, monto_nominal):
    comision = 0

    if codigo == 1:
        comision = (9 / 100) * monto_nominal

    elif codigo == 2:
        if monto_nominal < 50000:
            comision = 0
        elif 50000 <= monto_nominal <= 80000:
            comision = (5 / 100) * monto_nominal
        elif monto_nominal > 80000:
            comision = (7.8 / 100) * monto_nominal

    elif codigo == 3:
        monto_fijo = 100
        if monto_nominal > 25000:
            comision = (6 / 100) * monto_nominal
            comision += monto_fijo
        else:
            comision = monto_fijo

    elif codigo == 4:
        if monto_nominal <= 100000:
            comision = 500
        elif monto_nominal > 100000:
            comision = 1000

    elif codigo == 5:
        if monto_nominal < 500000:
            comision = 0
        elif monto_nominal >= 500000:
            comision = (7 / 100) * monto_nominal

        if comision > 50000:
            comision = 50000

    return comision


def extraer_datos_linea(linea):
    nombre = linea[0:20]
    codigo_id = linea[20:30]
    codigo_orden = linea[30:40]
    monto_nominal = int(linea[40:50])
    alg_comision = int(linea[50:52])
    alg_impuesto = int(linea[52:54])
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


def contar(c):
    return c + 1


def principal():
    c_operaciones_validas = 0
    c_monedas_invalidas = 0
    c_dest_invalidos = 0
    suma_montos = 0


    #Actividad 5
    nombre_primera_operacion = None
    cantidad_apariciones_beneficiario = 0

    linea_1 = True
    archivo = open("ordenes25.txt", "r")
    for linea in archivo:
        if linea_1 is True:
            linea_1 = False
            continue

        nombre, codigo_id, codigo_iso, monto_nominal, alg_comision, alg_impuesto = extraer_datos_linea(linea)

        # act 1 y2
        if es_moneda(codigo_iso) and es_destinatario(codigo_id):
            c_operaciones_validas = contar(c_operaciones_validas)
            monto_base = calcular_monto_base(monto_nominal, alg_comision)
            monto_final = calcular_monto_final(monto_base, alg_impuesto)
            suma_montos += monto_final

        elif not es_moneda(codigo_iso) and not es_destinatario(codigo_id):
            c_monedas_invalidas = contar(c_monedas_invalidas)

        elif not es_moneda(codigo_iso):
            c_monedas_invalidas = contar(c_monedas_invalidas)

        elif not es_destinatario(codigo_id):
            c_dest_invalidos = contar(c_dest_invalidos)

        #Actividad 5:
        nombre_primera_operacion, cantidad_apariciones_beneficiario = actu_bene_prim_oper(nombre, nombre_primera_operacion, cantidad_apariciones_beneficiario)

    archivo.close()

    print(' (r1) - Cantidad de ordenes invalidas - moneda no autorizada:', c_monedas_invalidas)
    print(' (r2) - Cantidad de ordenes invalidas - beneficiario mal identificado:', c_dest_invalidos)
    print(' (r3) - Cantidad de operaciones validas:', c_operaciones_validas)
    print(' (r4) - Suma de montos finales de operaciones validas:', suma_montos)
    print(" (r13) - Nombre del primer beneficiario:", nombre_primera_operacion)
    print(" (r14) - Cantidad de veces que aparece:", cantidad_apariciones_beneficiario)


principal()
