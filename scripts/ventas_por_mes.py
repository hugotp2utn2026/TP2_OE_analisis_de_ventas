import csv
with open("../datos/sales_sample_2024.csv", "r") as archivo:
    #Uso DictReader porque ignora la primera fila automaticamente.
    lector_dict = csv.DictReader(archivo)
    #Creo una variable con el total de cada mas, luego utilizo ese resultado como el value y el mes como la key, para saber que el me sea el correcto se usa string slicing
    # Este string slicing toma el mes.
    total_por_mes = dict()
    total_enero = 0
    total_febrero = 0
    total_marzo = 0
    total_abril = 0
    total_mayo = 0
    total_junio = 0
    total_julio = 0
    total_agosto = 0
    total_septiembre = 0
    total_octubre = 0
    total_noviembre = 0
    total_diciembre = 0
    for elemento in lector_dict:
      if elemento["sales_date"][5:7] == "01":
        total_enero += float(elemento["sales_amount"])
        total_por_mes["enero"] = total_enero
      elif elemento["sales_date"][5:7] == "02":
        total_febrero += float(elemento["sales_amount"])
        total_por_mes["febrero"] = total_febrero
      elif elemento["sales_date"][5:7] == "03":
        total_marzo += float(elemento["sales_amount"])
        total_por_mes["marzo"] = total_marzo
      elif elemento["sales_date"][5:7] == "04":
        total_abril += float(elemento["sales_amount"])
        total_por_mes["abril"] = total_abril
      elif elemento["sales_date"][5:7] == "05":
        total_mayo += float(elemento["sales_amount"])
        total_por_mes["mayo"] = total_mayo
      elif elemento["sales_date"][5:7] == "06":
        total_junio += float(elemento["sales_amount"])
        total_por_mes["junio"] = total_junio
      elif elemento["sales_date"][5:7] == "07":
        total_julio += float(elemento["sales_amount"])
        total_por_mes["julio"] = total_julio
      elif elemento["sales_date"][5:7] == "08":
        total_agosto += float(elemento["sales_amount"])
        total_por_mes["agosto"] = total_agosto
      elif elemento["sales_date"][5:7] == "09":
        total_septiembre += float(elemento["sales_amount"])
        total_por_mes["septiembre"] = total_septiembre
      elif elemento["sales_date"][5:7] == "10":
        total_octubre += float(elemento["sales_amount"])
        total_por_mes["octubre"] = total_octubre
      elif elemento["sales_date"][5:7] == "11":
        total_noviembre += float(elemento["sales_amount"])
        total_por_mes["noviembre"] = total_noviembre
      elif elemento["sales_date"][5:7] == "12":
        total_diciembre += float(elemento["sales_amount"])
        total_por_mes["diciembre"] = total_diciembre
    print(total_por_mes)

#Creo el archivo csv con los totales de las ventas de cada mes
with open("../resultados/resultados_ejemplo.csv", "w") as archivo:
  #Creo los headers de cada columna con un salto de linea al final
  archivo.write("mes,total\n")
  #cada fila es un mes con su valor correspondiente, esto utiliza el dictionary creado en la parte anterior del codigo, la key es el mes, el value el total por mes, y lo escribe siendo cada linea un mes
  for key,value in total_por_mes.items():
    archivo.write(f"{key},{value}\n")
