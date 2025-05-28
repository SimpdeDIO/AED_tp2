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
        operaciones_validas()

    archivo.close()



principal()
