def saber_anyo_bisiesto(anyo:int) -> bool:
    bisiesto = False
    if anyo % 100 == 0  and anyo % 400 != 0:
        bisiesto = False
    elif anyo % 4 == 0:
        bisiesto = True
    return bisiesto
    

print(saber_anyo_bisiesto(2000))
print(saber_anyo_bisiesto(2400))
print(saber_anyo_bisiesto(1900))


def calculo_precio_total(precio_absoluto:float, descuento:int) -> float:
    return precio_absoluto - precio_absoluto * descuento / 100

print(calculo_precio_total(100, 15))
