
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
agrupado = df.groupby("Cancela_Servicio")
print(agrupado)

print(" +-+-+- por agregacion -+-+-+-")

# Gasto mensual promedio por tipo de cancelacion
print(agrupado['Gasto_Mensual'].mean())

# Antiguedad maxima por meses
print("+-+-+ Antiguedad maxima en meses +-+-+-")
print(agrupado["Antiguedad_Meses"].max())

print("+-+-+-+- SEGUNDA PARTE +-+-+-+- 0074 +-+-+-+-")
print("Agregaciones multiples")
print("mean --> promedio, sum --> suma")
print("max --> Maximo, min --> minimo")

resultado_agregado = agrupado["Gasto_Mensual"].agg(['mean', 'sum', 'max', 'min'])
print(resultado_agregado)

print("Agrupacion por varias columnas")
print("Agrega columna al dataframe")
print("Columna Team --> Equipo")

df['Equipo'] = ['A', 'B', 'A', 'B', 'A', 'B']

agrupado_múltiple = df.groupby(
    ["Cancela_Servicio", "Equipo"]
)["Antiguedad_Meses"].mean()

print(agrupado_múltiple)



