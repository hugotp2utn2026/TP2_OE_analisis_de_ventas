import pandas as pd
import matplotlib.pyplot as plt

#Lee el archivo y lo almacena en una variable dataframe
df = pd.read_csv("../datos/sales_sample_2024.csv")
#Hace string slicing para extraer solamente el mes de la fecha
df["mes"] = df["sales_date"].str[5:7]
#Agrupa filas por mes y suma los valores para tener el total por mes
ventas_por_mes = df.groupby("mes")["sales_amount"].sum()
print(ventas_por_mes)
#Genera un grafica de barras
ventas_por_mes.plot(kind="bar")

#Establezco el eje x, y, el titulo y guardo el resultado como un archivo .png en la carpeta resultados
plt.xlabel("Mes")
plt.ylabel("Ventas")
plt.title("Ventas por mes")
plt.savefig("../resultados/ventas_por_mes.png")

plt.show()