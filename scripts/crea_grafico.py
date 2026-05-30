#Aca esta el grafico que pide la consigna
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../datos/sales_sample_2024.csv")
df["mes"] = df["sales_date"].str[5:7]
ventas_por_mes = df.groupby("mes")["sales_amount"].sum()
print(ventas_por_mes)
ventas_por_mes.plot(kind="bar")

plt.xlabel("Mes")
plt.ylabel("Ventas")
plt.title("Ventas por mes")
#Guardo el archivo como pdf en la carpeta de collab, despues comitear a github
plt.savefig("../resultados/ventas_por_mes.png")

plt.show()