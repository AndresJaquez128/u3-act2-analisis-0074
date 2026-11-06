# Step 1: Import Libraries
import pandas as pd
import numpy as np

print("Analisis de datos Alumnos Jaquez Andres = 0074")
clientes = {
    "Cliente": ["Pedro", "Nava", "Alonso", "Angela", "Matias", "Andres"],
    "Antiguedad_Meses": [2, 36, 12, 5, 48, 1],
    "Gasto_Mensual": [29.99, 89.99, 59.99, 19.99, 110.00, 49.99],
    "Cancela_Servicio": [True, False, False, True, False, True]
}

df = pd.DataFrame(clientes)
print(df)

print(" -+-+-+-+ Agrupar por una sola columna -+-+-+")
agrupado = df.groupby("Antiguedad_Meses")
print(agrupado)

print(" +-+-+- por agrecacion -+-+-+-")
# gasto mensual promedio por mes
print(agrupado['Gasto_Mensual'].mean())
# antiguedad maxima por meses
print("+-+-+ Antiguedad de meses +-+-+-")
print(agrupado["Cancela_Servicio"].max())

