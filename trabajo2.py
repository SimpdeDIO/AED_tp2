arch = open('ordenes.txt', 'rt')
texto = arch.read()

nombre_destinatario = str(input('ingrese su nombres y apellidos:'))

codigo_identificacion = ('ARS', 'USD', 'EUR', 'GBP', 'JPY')

def cantidad_operaciones(ARS, USD, EUR, GBP, JPY):
    if texto

codigo_iso = str(input('ingrese tipo de moneda:'))

monto_nominal = int(input('ingrese cuanto quiere recibir:'))

if codigo_identificacion[0] in codigo_iso:
    mensaje = "Moneda valida"
    comision = (monto_nominal * 5) / 100
    comision = round(comision, 2)
    monto_base = monto_nominal - comision

elif codigo_identificacion[1] in codigo_iso:
    mensaje = "Moneda valida"
    comision = (monto_nominal * 7) / 100
    comision = round(comision, 2)
    monto_base = monto_nominal - comision

elif codigo_identificacion[2] in codigo_iso:
    mensaje = "Moneda valida"
    comision = (monto_nominal * 7) / 100
    comision = round(comision, 2)
    monto_base = monto_nominal - comision

elif codigo_identificacion[3] in codigo_iso:
    mensaje = "Moneda valida"
    comision = (monto_nominal * 9) / 100
    comision = round(comision, 2)
    monto_base = monto_nominal - comision

elif codigo_identificacion[4] in codigo_iso:

    if monto_nominal >= 15000:
        if monto_nominal <= 500000:

            mensaje = "Moneda valida"
            comision = (monto_nominal * 9) / 100
            comision = round(comision, 2)
            if comision > 950000:
                comision = 950000
            monto_base = monto_nominal - comision


        elif monto_nominal > 500000 and monto_nominal <= 1500000:

            mensaje = "Moneda valida"
            comision = (monto_nominal * 7.8) / 100
            comision = round(comision, 2)
            if comision > 950000:
                comision = 950000
            monto_base = monto_nominal - comision

        elif monto_nominal > 1500000 and monto_nominal <= 10000000:

            mensaje = "Moneda valida"
            comision = (monto_nominal * 5.5) / 100
            comision = round(comision, 2)
            if comision > 950000:
                comision = 950000

            monto_base = monto_nominal - comision


        elif monto_nominal > 10000000:

            mensaje = "Moneda valida"
            comision = (monto_nominal * 5) / 100
            comision = round(comision, 2)
            if comision > 950000:
                comision = 950000

            monto_base = monto_nominal - comision


    else:
        monto_base = 0
        mensaje = "Monto minimo para JPY no alcanzado"

else:
    mensaje = "Moneda no autorizada"
    monto_base = 0

if monto_base > 500000:
    impuesto = (monto_base * 21) / 100
    monto_final = monto_base - impuesto
else:
    monto_final = monto_base

print("Beneficiario:", nombre_destinatario)
print("Moneda:", mensaje)
print("Monto base (descontadas las comisiones):", monto_base)
print("Monto final (descontados los impuestos):", monto_final)