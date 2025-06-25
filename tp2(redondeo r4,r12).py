# datos
def extraer_datos_linea(linea):
    nombre = linea[0:20]
    codigo_id = linea[20:30]
    codigo_orden = linea[30:40]
    monto_nominal = int(linea[40:50])
    alg_comision = int(linea[50:52])
    alg_impuesto = int(linea[52:54])
    return nombre, codigo_id, codigo_orden, monto_nominal, alg_comision, alg_impuesto


# act 1 (r1)
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


# (r2)
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


# act 2 (r3)
def contar(c):
    return c + 1


# act 3(r5,r9)
def obtener_moneda(codigo):
    for moneda in ["ARS", "USD", "EUR", "GBP", "JPY"]:
        if moneda in codigo:
            return moneda
    return None


# act 4 (r10,r12)
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

    if codigo == 4 or codigo == 5:
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
    if codigo == 6 or codigo == 8:
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

    elif codigo == 7:
        if monto_nominal <= 75000:
            comision = 3000
        elif monto_nominal >= 75000:
            comision = (monto_nominal - 75000) * 0.05

        if comision >= 10000:
            comision = 10000

    return comision


#el agregado de la actividad 4
def actualizar_max_diferencia(codigo_orden, monto_nominal, alg_comision, alg_impuesto, max_dif_act, cod_max, nom_max, final_max):
    monto_base = calcular_monto_base(monto_nominal, alg_comision)
    monto_final = calcular_monto_final(monto_base, alg_impuesto)
    diferencia = monto_nominal - monto_final
    if (max_dif_act is None) or (diferencia > max_dif_act):
        return diferencia, codigo_orden, monto_nominal, monto_final
    else:
        return max_dif_act, cod_max, nom_max, final_max

# act 5 (r13,r14)
def actu_bene_prim_oper(nombre_actual, nombre_primera_operacion, cantidad_apariciones_beneficiario):
    if nombre_primera_operacion is None:
        nombre_primera_operacion = nombre_actual
    if nombre_actual == nombre_primera_operacion:
        cantidad_apariciones_beneficiario += 1
    return nombre_primera_operacion, cantidad_apariciones_beneficiario


# funcion principal
def principal():
    # contadores
    cant_ARS = 0
    cant_USD = 0
    cant_EUR = 0
    cant_GBP = 0
    cant_JPY = 0
    moneda = 0
    max_diferencia = None #Si le pones 0 no arrancaba la funcion
    codigo_orden_max = None
    monto_nominal_max = None
    monto_final_max = None
    c_operaciones_validas = 0
    c_monedas_invalidas = 0
    c_dest_invalidos = 0
    suma_montos = 0
    nombre_primera_operacion = None
    cantidad_apariciones_beneficiario = 0
    ordenes_totales = 0
    c_operaciones_invalidas = 0
    suma_montos_ars = 0
    op_validas_ars = 0

    # salto de primera linea y lectura del archivo
    linea_1 = True
    archivo = open("ordenes25.txt")
    for linea in archivo:
        if linea_1 is True:
            linea_1 = False
            continue




        ordenes_totales += 1  # act 6
        nombre, codigo_id, codigo_iso, monto_nominal, alg_comision, alg_impuesto = extraer_datos_linea(linea)

        # act 1 y 2 (r1,r4)
        if es_moneda(codigo_iso) and es_destinatario(codigo_id):
            c_operaciones_validas = contar(c_operaciones_validas)
            monto_base = calcular_monto_base(monto_nominal, alg_comision)
            monto_final = calcular_monto_final(monto_base, alg_impuesto)
            suma_montos += monto_final



            if "ARS" in codigo_iso:
                suma_montos_ars += monto_final
                op_validas_ars = contar(op_validas_ars)


        elif not es_moneda(codigo_iso) and not es_destinatario(codigo_id):
            c_monedas_invalidas = contar(c_monedas_invalidas)
            c_operaciones_invalidas = contar(c_operaciones_invalidas)  # suma oeraciones invalidas act 6

        elif not es_moneda(codigo_iso):
            c_monedas_invalidas = contar(c_monedas_invalidas)
            c_operaciones_invalidas = contar(c_operaciones_invalidas)  # suma oeraciones invalidas act 6

        elif not es_destinatario(codigo_id):
            c_dest_invalidos = contar(c_dest_invalidos)
            c_operaciones_invalidas = contar(c_operaciones_invalidas)  # suma oeraciones invalidas act 6



        # act 3(r5,r9)
        moneda = obtener_moneda(codigo_iso)
        if moneda == "ARS":
            cant_ARS += 1
        elif moneda == "USD":
            cant_USD += 1
        elif moneda == "EUR":
            cant_EUR += 1
        elif moneda == "GBP":
            cant_GBP += 1
        elif moneda == "JPY":
            cant_JPY += 1

        #Actividad 4
        max_diferencia, codigo_orden_max, monto_nominal_max, monto_final_max = actualizar_max_diferencia(codigo_iso, monto_nominal, alg_comision, alg_impuesto, max_diferencia, codigo_orden_max, monto_nominal_max, monto_final_max)

        # Actividad 5:
        nombre_primera_operacion, cantidad_apariciones_beneficiario = actu_bene_prim_oper(nombre, nombre_primera_operacion,cantidad_apariciones_beneficiario)
    archivo.close()


    # Act 6 (r15)
    if ordenes_totales > 0:
        porcentaje_invalidas = (c_operaciones_invalidas * 100) // ordenes_totales
    else:
        porcentaje_invalidas = 0

    # act 7 (r16)
    if op_validas_ars > 0:
        monto_promedio = suma_montos_ars // op_validas_ars
    else:
        monto_promedio = 0


    # No borren los comentarios che
    # Total no afectan, los sacamos recien para la entrega noma
    print(' (r1) - Cantidad de ordenes invalidas - moneda no autorizada:', c_monedas_invalidas)
    print(' (r2) - Cantidad de ordenes invalidas - beneficiario mal identificado:', c_dest_invalidos)
    print(' (r3) - Cantidad de operaciones validas:', c_operaciones_validas)
    print(' (r4) - Suma de montos finales de operaciones validas:', round(suma_montos))
    print(' (r5) - Cantidad de ordenes para moneda ARS:', cant_ARS)
    print(' (r6) - Cantidad de ordenes para moneda USD:', cant_USD)
    print(' (r7) - Cantidad de ordenes para moneda EUR:', cant_EUR)
    print(' (r8) - Cantidad de ordenes para moneda GBP:', cant_GBP)
    print(' (r9) - Cantidad de ordenes para moneda JPN:', cant_JPY)
    print('(r10) - Codigo de la orden de pago con mayor diferencia nominal - final:', codigo_orden_max)
    print('(r11) - Monto nominal de esa misma orden:', monto_nominal_max)
    print('(r12) - Monto final de esa misma orden:', round(monto_final_max))
    print('(r13) - Nombre del primer beneficiario del archivo', nombre_primera_operacion)
    print('(r14) - Cantidad de veces que apareció ese mismo nombre:', cantidad_apariciones_beneficiario)
    print('(r15) - Porcentaje de operaciones inválidas sobre el total:', porcentaje_invalidas)
    print('(r16) - Monto final promedio de las ordenes validas en moneda ARS:', int(monto_promedio))

principal()
