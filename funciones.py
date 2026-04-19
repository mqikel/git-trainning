def saber_anyo_bisiesto(anyo:int) -> bool:
    bisiesto = False
    if anyo % 100 == 0  and anyo % 400 != 0:
        bisiesto = False
    elif anyo % 4 == 0:
        bisiesto = True
    return bisiesto
    

def calculo_precio_total(precio_absoluto:float, descuento:int) -> float:
    return precio_absoluto - precio_absoluto * descuento / 100


years = [2000, 1980, 2024, 2025]
product_price = 1052.34
for year in years:
    final_price = 0
    if saber_anyo_bisiesto(year) == True:
        final_price = calculo_precio_total(product_price, 22)
    else:
        final_price = calculo_precio_total(product_price, 10)
    
    final_price = round(final_price, 2)
    
    print(f"El precio de la TV en el año {year} es de {final_price}€")