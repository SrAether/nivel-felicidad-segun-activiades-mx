import pandas as pd
import unicodedata

# Leer el archivo CSV
try:
    df = pd.read_csv("./dataset_limpio.csv", encoding="latin1")
except UnicodeDecodeError:
    print("Error de codificación, intenta con otro encoding como 'utf-8' o 'latin1'.")
    raise

# Función para eliminar acentos
def eliminar_acentos(texto):
    if isinstance(texto, str):
        return ''.join(c for c in unicodedata.normalize('NFKD', texto) if not unicodedata.combining(c))
    return texto

# Aplicar la función a todo el DataFrame
df_sin_acentos = df.applymap(eliminar_acentos)

# Guardar el resultado en un archivo CSV
df_sin_acentos.to_csv("dataset_final.csv", index=False, encoding="utf-8")

print("Archivo procesado y guardado como 'muestraFinal.csv'.")
print(df.head())
print(df_sin_acentos.head())
