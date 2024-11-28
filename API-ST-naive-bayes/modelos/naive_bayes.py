import pandas as pd
import numpy as np
from concurrent.futures import ThreadPoolExecutor, as_completed
import time

def calcular_probabilidad_gaussiana(x, mean, std):
    if std == 0:
        return 1 if x == mean else 0
    exponent = np.exp(-((x - mean) ** 2) / (2 * (std ** 2)))
    return (1 / (np.sqrt(2 * np.pi) * std)) * exponent

def calcular_probabilidades_categoricas(datos: pd.DataFrame, columna: str, clase: str = None):
    if columna not in datos.columns:
        raise ValueError(f"La columna '{columna}' no se encuentra en el DataFrame.")
    if clase is None:
        return datos[columna].value_counts(normalize=True).to_dict()
    tabla_frecuencias = datos.groupby([clase, columna]).size().unstack(fill_value=0)
    tabla_probabilidades = tabla_frecuencias.div(tabla_frecuencias.sum(axis=1), axis=0)
    if (tabla_probabilidades == 0).any().any():
        tabla_frecuencias += 1
        tabla_probabilidades = tabla_frecuencias.div(tabla_frecuencias.sum(axis=1) + len(tabla_frecuencias.columns), axis=0)
    return tabla_probabilidades.to_dict()

def calcular_probabilidades_numericas(datos: pd.DataFrame, columna: str, clase: str):
    if columna not in datos.columns or clase not in datos.columns:
        raise ValueError(f"Columna '{columna}' o '{clase}' no encontrada.")
    return datos.groupby(clase)[columna].agg(["mean", "std"]).to_dict()

def modelo_naive_bayes(datos: pd.DataFrame, clase: str):
    if clase not in datos.columns:
        raise ValueError(f"La columna '{clase}' no se encuentra en el DataFrame.")

    start_time = time.perf_counter()

    # Cálculo de la probabilidad a priori (rápido, un solo hilo)
    with ThreadPoolExecutor(max_workers=1) as executor:
        probabilidad_clase_future = executor.submit(calcular_probabilidades_categoricas, datos, clase, None)
        probabilidad_clase = probabilidad_clase_future.result()

    # Cálculo de probabilidades numéricas (máximo 10 hilos)
    start_numeric = time.perf_counter()
    probabilidades_numericas_futures = {}
    with ThreadPoolExecutor(max_workers=10) as executor:
        for columna in datos.select_dtypes(include=["number"]).columns:
            if columna != clase:
                probabilidades_numericas_futures[columna] = executor.submit(calcular_probabilidades_numericas, datos, columna, clase)

    probabilidades_numericas = {columna: future.result() for columna, future in probabilidades_numericas_futures.items()}
    end_numeric = time.perf_counter()

    # Cálculo de probabilidades categóricas (rápido, un solo hilo)
    start_categorical = time.perf_counter()
    probabilidades_categoricas_futures = {}
    with ThreadPoolExecutor(max_workers=1) as executor:
        for columna in datos.select_dtypes(include=["object"]).columns:
            probabilidades_categoricas_futures[columna] = executor.submit(calcular_probabilidades_categoricas, datos, columna, clase)

    probabilidades_categoricas = {columna: future.result() for columna, future in probabilidades_categoricas_futures.items()}
    end_categorical = time.perf_counter()

    end_time = time.perf_counter()

    # Impresión de tiempos
    # print(f"Tiempo total: {end_time - start_time:.2f} segundos")
    # print(f"Tiempo en cálculos numéricos: {end_numeric - start_numeric:.2f} segundos")
    # print(f"Tiempo en cálculos categóricos: {end_categorical - start_categorical:.2f} segundos")

    modelo = {
        "clase": clase,
        "probabilidad_clase": probabilidad_clase,
        "probabilidades_numericas": probabilidades_numericas,
        "probabilidades_categoricas": probabilidades_categoricas
    }
    return modelo


def evaluar_naive_bayes(modelo, prueba: pd.DataFrame):
    """Evaluar el modelo Naive Bayes en un conjunto de prueba."""
    clase = modelo["clase"]
    probabilidad_clase = modelo["probabilidad_clase"]
    probabilidades_numericas = modelo["probabilidades_numericas"]
    probabilidades_categoricas = modelo["probabilidades_categoricas"]
    columnas_categoricas = prueba.select_dtypes(include=["object"]).columns
    columnas_numericas = prueba.select_dtypes(include=["number"]).columns
    
    # Función para evaluar cada fila
    def evaluar_fila(fila):
        prob_clases = {}

        for c, prob_c in probabilidad_clase.items():
            prob_total = np.log(prob_c)

            for columna, prob_columna in probabilidades_categoricas.items():
                if columna in columnas_categoricas:
                    valor = fila[columna]
                    if valor in prob_columna.get(c, {}):
                        prob_total += np.log(prob_columna[c].get(valor, 1e-6))
                    else:
                        prob_total += np.log(1e-6)
                
                elif columna in columnas_numericas:
                    valor = fila[columna]
                    if c in prob_columna:
                        mean = prob_columna[c]["mean"]
                        std = prob_columna[c]["std"]
                        prob_total += np.log(calcular_probabilidad_gaussiana(valor, mean, std))

            prob_clases[c] = prob_total

        return max(prob_clases, key=prob_clases.get)
    
    # Cronometrar el tiempo de evaluación de todas las filas
    start_time = time.perf_counter()
    
    # Usar multihilos para evaluar cada fila
    with ThreadPoolExecutor() as executor:
        predicciones = list(executor.map(evaluar_fila, [fila for _, fila in prueba.iterrows()]))
    
    end_time = time.perf_counter()

    # Imprimir el tiempo total de evaluación
    #print(f"Tiempo de evaluación: {end_time - start_time:.4f} segundos")
    
    return predicciones





if __name__ == "__main__":
    # Datos de entrenamiento
    datos_entrenamiento = pd.DataFrame({
        "Outlook": ["overcast", "overcast", "rainy", "rainy", "rainy", "rainy", "sunny", "sunny", "sunny", "sunny",
                    "overcast", "overcast", "rainy", "sunny"],
        "Temp": [64, 81, 70, 65, 75, 71, 85, 72, 69, 75, 83, 72, 68, 80],
        "Humidity": [65, 75, 96, 70, 80, 91, 85, 95, 70, 70, 86, 90, 80, 90],
        "Windy": [True, False, False, True, False, True, False, False, False, True, False, True, False, True],
        "Play": ["No", "Yes", "Yes", "Yes", "No", "Yes", "Yes", "Yes", "Yes", "No", "No", "Yes", "No", "Yes"]
    })

    # Datos de prueba
    datos_prueba = pd.DataFrame({
        "Outlook": ["rainy", "rainy", "sunny", "sunny"],
        "Temp": [75, 71, 85, 72],
        "Humidity": [80, 91, 85, 95],
        "Windy": [False, True, False, False]
    })
    
    # Entrenar el modelo
    modelo = modelo_naive_bayes(datos_entrenamiento, "Play")
    
    # Evaluar el modelo
    predicciones = evaluar_naive_bayes(modelo, datos_prueba)
    print("Predicciones:", predicciones)
