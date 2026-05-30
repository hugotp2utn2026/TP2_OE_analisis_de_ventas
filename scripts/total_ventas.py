#Se cambio el nombre de variable "iterador" por "suma_total"
import csv
#Promedio total de ventas
#Lee el archivo con csv.DictReader para saltearme la primera fila sin hacer next
with open("../datos/sales_sample_2024.csv", "r") as archivo:
    lector_dict = csv.DictReader(archivo)
#la variable suma_total almacena la suma de todos los elementos de la columna "sales_amount" y lo printea en consola
    suma_total = 0
    for elemento in lector_dict:
      suma_total = suma_total + float(elemento["sales_amount"])
    print(f"El total de ventas del año 2024 es {suma_total}")

#Creo el archivo con el resultado y lo guardo en la carpeta resultados, con el nombre ventas_totales_2024.csv, con dos columnas: año y ventas_totales, y escribo el resultado de la suma total en la fila correspondiente al año 2024
with open("../resultados/ventas_totales_2024.csv", "w") as archivo:
   archivo.write(f"año,ventas_totales\n")
   archivo.write(f"2024, {suma_total}")
input("Presione Enter para cerrar el archivo")

