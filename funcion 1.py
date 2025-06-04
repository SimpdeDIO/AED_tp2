#Trate de meter todos los if en un for pero nose si esta bien, si lo pueden chequerar piola
def calcular_monto_base(codigo_iso, monto_nominal):
    monto_base = 0
    comision = comision()

    monedas = ("ARS", "USD", "EUR", "GBP", "JPY")
    tasas = (5, 7, 7, 9, 0)  # JPY tiene variables especiales con valores no enteros asi que no lo inclui aca

    monto_base = monto_nominal


def comision(codigo_iso, monto_nominal):
    comision = 0
    monto_fijo = 0

    monedas = ("ARS", "USD", "EUR", "GBP", "JPY")
    if codigo_iso == monedas[0]:
        comision = (9 / 100) * monto_nominal

    elif codigo_iso == monedas[1]:
        if monto_nominal < 50000:
            comision = 0

        elif 50000 <= monto_nominal < 80000:
            comision = (5 / 100) * monto_nominal

        elif monto_nominal >= 80000:
            comision = (7.8 / 100) * monto_nominal

    elif codigo_iso == monedas[2] or codigo_iso == monedas[3] :
        monto_fijo = 100
        if monto_nominal > 25000:
            pass

    elif codigo_iso == monedas[3]:
        comision = 9 / 100


def extraer_datos_linea(linea):
    nombre = linea[0:20]
    codigo_id = linea[20:30]
    codigo_orden = linea[30:40]
    monto_nominal = int(linea[40:50])
    alg_comision = int(linea[50:52])
    alg_impuesto = int(linea[52:54])

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
            
        elif not es_moneda(codigo_iso) and not es_destinatario(codigo_id):
            c_monedas_invalidas = contar(c_monedas_invalidas)

        elif not es_moneda(codigo_iso):
            c_monedas_invalidas = contar(c_monedas_invalidas)

        elif not es_destinatario(codigo_id):
            c_dest_invalidos = contar(c_dest_invalidos)

    archivo.close()

    print(' (r1) - Cantidad de ordenes invalidas - moneda no autorizada:', c_monedas_invalidas)
    print(' (r2) - Cantidad de ordenes invalidas - beneficiario mal identificado:', c_dest_invalidos)
    print(' (r3) - Cantidad de operaciones validas:', c_operaciones_validas)


principal()
