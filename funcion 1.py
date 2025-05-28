def calcular_monto_final(codigo_iso, monto_nominal):
    # Inicializar variables
    mensaje = ""
    monto_base = 0
    monto_final = 0
    
    if codigo_iso == codigo_identificacion[0]:  # ARS
        mensaje = "Moneda valida"
        comision = round((monto_nominal * 5) / 100, 2)
        monto_base = monto_nominal - comision

    elif codigo_iso == codigo_identificacion[1]:  # USD
        mensaje = "Moneda valida"
        comision = round((monto_nominal * 7) / 100, 2)
        monto_base = monto_nominal - comision

    elif codigo_iso == codigo_identificacion[2]:  # EUR
        mensaje = "Moneda valida"
        comision = round((monto_nominal * 7) / 100, 2)
        monto_base = monto_nominal - comision

    elif codigo_iso == codigo_identificacion[3]:  # GBP
        mensaje = "Moneda valida"
        comision = round((monto_nominal * 9) / 100, 2)
        monto_base = monto_nominal - comision

    elif codigo_iso == codigo_identificacion[4]:  # JPY
        if monto_nominal >= 15000:
            if monto_nominal <= 500000:
                mensaje = "Moneda valida"
                comision = round((monto_nominal * 9) / 100, 2)
                if comision > 950000:
                    comision = 950000
                monto_base = monto_nominal - comision
            elif monto_nominal <= 1500000:
                mensaje = "Moneda valida"
                comision = round((monto_nominal * 7.8) / 100, 2)
                if comision > 950000:
                    comision = 950000
                monto_base = monto_nominal - comision
            elif monto_nominal <= 10000000:
                mensaje = "Moneda valida"
                comision = round((monto_nominal * 5.5) / 100, 2)
                if comision > 950000:
                    comision = 950000
                monto_base = monto_nominal - comision
            else:
                mensaje = "Moneda valida"
                comision = round((monto_nominal * 5) / 100, 2)
                if comision > 950000:
                    comision = 950000
                monto_base = monto_nominal - comision
        else:
            mensaje = "Monto minimo para JPY no alcanzado"
            monto_base = 0
    else:
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

def operacioes_validas(monto_final):
    c1 = suma_monto_final = 0
    c1 += 1
    suma_monto_finales += monto_final
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
    valides = None
    letras_encontradas = 0
    for car in codigo_id:
        if car != "-" or letras_encontradas != 0:
            letras_encontradas = 1
            if "A" <= car <= "Z" or "0" <= car <= "9" or car == "-":
                valides = True

            else:
                valides = False
        else:
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

def principal():

    linea_1 = True
    archivo = open("ordenes25.txt", "r")
    for linea in archivo:
        if linea_1 == True:
            linea_1 = False
            continue

        nombre, codigo_id, codigo_iso, monto_nominal, alg_comision, alg_impuesto = extraer_datos_linea(linea)

    if es_moneda(codigo_iso):
        monto_final = calcular_monto_final()
        operaciones_validas(monto_final)

    archivo.close()



principal()
