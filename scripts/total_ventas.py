
import csv
#Promedio total de ventas
with open("../datos/sales_sample_2024.csv", "r") as archivo:
    lector_dict = csv.DictReader(archivo)

    iterador = 0
    
    for elemento in lector_dict:
      iterador = iterador + float(elemento["sales_amount"])
    print(f"El total de ventas del año 2024 es {iterador}")

with open("../resultados/ventas_totales_2024.csv", "w") as archivo:
   archivo.write(f"año,ventas_totales\n")
   archivo.write(f"2024, {iterador}")
input("Presione Enter para cerrar el archivo")

