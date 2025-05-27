#Esta es la parte del tp1 pasada a una funcion nomas
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
    
#Leer archivo y aclarar las tuplas
archivo = open('archivo.txt', 'r')
texto = archivo.read()
archivo.close()
codigo_identificacion = ('ARS', 'USD', 'EUR', 'GBP', 'JPY')
#Codigo base creo yo xd