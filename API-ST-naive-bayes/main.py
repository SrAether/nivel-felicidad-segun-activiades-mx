import pandas as pd  # Importamos la librería pandas para trabajar con dataframes
import datos.manejo as manejo
import os  # Importamos la librería os para limpiar la pantalla
import pyfiglet
import numpy as np

from modelos.naive_bayes import modelo_naive_bayes
from modelos.naive_bayes import evaluar_naive_bayes

from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem,
    QHeaderView
)
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt

# Función para mostrar un DataFrame en una ventana de PyQt
def mostrar_dataframe_en_qt(df: pd.DataFrame, titulo: str):
    ventana = QWidget()
    ventana.setWindowTitle(titulo)
    ventana.setGeometry(100, 100, 800, 600)
    
    layout = QVBoxLayout()
    
    # Crear tabla
    tabla = QTableWidget()
    tabla.setRowCount(len(df))
    tabla.setColumnCount(len(df.columns))
    tabla.setHorizontalHeaderLabels(df.columns)
    
    # Establecer fuente más grande
    tabla.setFont(QFont("Arial", 12))
    
    # Ajustar encabezados
    header = tabla.horizontalHeader()
    header.setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
    
    # Insertar filas
    for i, fila in df.iterrows():
        for j, valor in enumerate(fila):
            tabla.setItem(i, j, QTableWidgetItem(str(valor)))
    
    layout.addWidget(tabla)
    ventana.setLayout(layout)
    
    ventana.show()
    return ventana


# VARIABLES GLOBALES PARA COLORES ANSI
RESET = "\033[0m"
NEGRO = "\033[30m"
ROJO = "\033[31m"
VERDE = "\033[32m"
AMARILLO = "\033[33m"
AZUL = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
BLANCO = "\033[37m"
NEGRITA = "\033[1m"
SUBRAYADO = "\033[4m"

# Función para limpiar la pantalla según el sistema operativo
def limpiar_pantalla():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# Función para mostrar los datos actuales
def mostrar_datos_actuales(ruta_dataset=None, dataset=None, tam_dataset_prueba=None, clase=None):
    """Muestra los datos agregados al programa."""
    if any([ruta_dataset, dataset, tam_dataset_prueba, clase]):
        print(CYAN + NEGRITA + "DATOS ACTUALMENTE AGREGADOS" + RESET)
        if ruta_dataset:
            print(MAGENTA + "Ruta dataset: " + RESET, ruta_dataset)
        if dataset is not None:
            print(MAGENTA + "Dataset cargado." + RESET)
        if tam_dataset_prueba:
            print(MAGENTA + "Tamaño dataset prueba: " + RESET, tam_dataset_prueba)
        if clase:
            print(MAGENTA + "Clase seleccionada: " + RESET, clase)
    else:
        print(AMARILLO + "No hay datos agregados." + RESET)

# Función para cargar los datos
def cargar_datos():
    """Carga un dataset en formato CSV."""
    limpiar_pantalla()
    while True:
        print(AZUL + NEGRITA + "CARGAR DATOS" + RESET)
        ruta_dataset = input("Ingrese la ruta del dataset: ")
        try:
            dataset = manejo.cargar_datos(ruta_dataset)
            return ruta_dataset, dataset
        except Exception as e:
            limpiar_pantalla()
            print(ROJO + "Error al cargar el dataset" + RESET)
            print(AMARILLO + str(e) + RESET)

# Función para seleccionar el tamaño del dataset de prueba
def seleccionar_tam_dataset_prueba():
    """Selecciona el tamaño del dataset de prueba."""
    limpiar_pantalla()
    while True:
        try:
            print(AZUL + NEGRITA + "TAMAÑO DEL DATASET DE PRUEBA" + RESET)
            print("Por ejemplo, si se selecciona 0.2, el 20% del dataset se usará para pruebas.")
            tam_dataset_prueba = float(input("Ingrese el tamaño del dataset de prueba (entre 0 y 1): "))
            if 0 < tam_dataset_prueba < 1:
                return tam_dataset_prueba
            else:
                limpiar_pantalla()
                print(ROJO + "El valor debe estar entre 0 y 1" + RESET)
        except ValueError:
            limpiar_pantalla()
            print(ROJO + "Error: Debe ingresar un número válido entre 0 y 1." + RESET)

# Función para mostrar opciones del menú principal
def mostrar_menu_principal():
    """Muestra el menú principal del programa."""
    print(AZUL + NEGRITA + "MENU PRINCIPAL" + RESET)
    print(VERDE + "1. Cargar datos")
    print("2. Porcentaje del dataset para pruebas")
    print("3. Seleccionar clase")
    print("4. Evaluar Modelo")
    print("5. Salir" + RESET)
    return input("Seleccione una opción: ")

       
# Función para seleccionar la clase
def seleccionar_clase(dataset):
    """Función para seleccionar la clase."""
    limpiar_pantalla()
    if dataset is None:
        raise ValueError("No se ha cargado ningún dataset.")
    print(AZUL + NEGRITA + "SELECCIONAR CLASE" + RESET)
    print(AMARILLO + "Columnas disponibles:" + RESET)
    contador = 1
    for columna in dataset.columns:
        print(f"{contador}. {columna}")
        contador += 1
    seleccion = int(input("Seleccione una columna: "))
    return dataset.columns[seleccion - 1]     

# Función para evaluar el modelo (vacía)
def evaluar_modelo(dataset: pd.DataFrame, tam_dataset_prueba, clase):
    """Función para evaluar el modelo (A implementar)."""
    # Verificamos si se han cargado los datos correctamente
    if dataset.empty:
        raise ValueError("El dataset está vacío o no se ha cargado.")
    if tam_dataset_prueba is None or not (0 < tam_dataset_prueba < 1):
        raise ValueError("El tamaño del dataset de prueba no es válido o no ha sido seleccionado.")
    if not clase:
        raise ValueError("No se ha especificado la clase a predecir.")
    print(AZUL + NEGRITA + "EVALUAR MODELO" + RESET) 
    
    # Preguntamos si desea continuar
    continuar = input("¿Desea continuar con la evaluación del modelo? (s/n): ")
    if continuar.lower() != "s" and continuar.lower() != "si" and continuar.lower() != "y":
        return
    # Pedimos el número de iteraciones
    while True:
        try:
            iteraciones = int(input("Ingrese el número de iteraciones: "))
            break
        except ValueError:
            print(ROJO + "Error: Debe ingresar un número válido." + RESET)
    # Evaluamos el modelo
    arregloResultados = []
    arregloPrediccionExitosa = []
    arregloPrueba = []
    for i in range(iteraciones):
        datos_entrenamiento, datos_prueba = manejo.generador_de_subconjuntos(dataset, tam_dataset_prueba, i)
        modelo = modelo_naive_bayes(datos_entrenamiento, clase)
        #print(f"Modelo Naive Bayes: {modelo}")
        resultado = evaluar_naive_bayes(modelo, datos_prueba)
        arregloResultados.append(resultado)
        # Calcular la precisión del modelo usando los datos de prueba
        prediccion_exitosa = datos_prueba[clase] == resultado
        precision = prediccion_exitosa.sum() / len(prediccion_exitosa)
        arregloPrediccionExitosa.append(precision)
        print(f"Precisión: {precision}")
        # Guardar los datos de prueba de la clase
        arregloPrueba.append(datos_prueba[clase])
        
    # presione cualquier tecla para continuar
    input("Presione cualquier tecla para continuar...")
    return arregloPrediccionExitosa
    

# Ciclo principal del programa
def main():
    # Variables locales
    ruta_data_set = None
    dataset = None
    tam_dataset_prueba = None
    clase = None
    
    # Limpiar pantalla inicial
    limpiar_pantalla()
    
    # Ciclo principal del menú
    while True:
        try:
            # Mostrar datos actuales
            mostrar_datos_actuales(ruta_data_set, dataset, tam_dataset_prueba, clase)
            
            # Mostrar menú y obtener la opción seleccionada
            seleccion = mostrar_menu_principal()
            
            # Procesar la selección del usuario
            if seleccion == "1":
                ruta_data_set, dataset = cargar_datos()
                limpiar_pantalla()

            elif seleccion == "2":
                tam_dataset_prueba = seleccionar_tam_dataset_prueba()
                limpiar_pantalla()
                
            elif seleccion == "3":
                clase = seleccionar_clase(dataset)
                limpiar_pantalla()

            elif seleccion == "4":
                limpiar_pantalla()
                mostrar_datos_actuales(ruta_data_set, dataset, tam_dataset_prueba, clase)
                #evaluar_modelo(dataset, tam_dataset_prueba, modelo_selec, clase)
                predicciones = evaluar_modelo(dataset, tam_dataset_prueba, clase)
                # creamos un DataFrame con los resultados
                df = pd.DataFrame(predicciones, columns=["Precisión"])
                desviacion_estandar = np.std(predicciones)
                # agregamos la desviación estándar al DataFrame como una columna nueva
                df["Desviación estándar"] = desviacion_estandar
                # Agregar la interpretación basada en criterios
                if desviacion_estandar < 0.01:
                    interpretacion = "Muy estable"
                elif 0.01 <= desviacion_estandar <= 0.02:
                    interpretacion = "Moderadamente estable"
                else:
                    interpretacion = "Inestable"

                df["Interpretación"] = interpretacion
                
                # Mostramos el DataFrame en una ventana de PyQt
                app = QApplication([])
                ventana = mostrar_dataframe_en_qt(df, "Resultados de las iteraciones")
                app.exec()
                limpiar_pantalla()

            elif seleccion == "5":
                print(AMARILLO + "Saliendo..." + RESET)
                ascii_art = pyfiglet.figlet_format("Desarrollado por:")
                print(ROJO + ascii_art + RESET)
                ascii_art = pyfiglet.figlet_format("Aether")
                print(CYAN + ascii_art + RESET)
                break

            else:
                limpiar_pantalla()
                print(ROJO + "Opción no válida" + RESET)

        except Exception as e:
            # En caso de cualquier excepción, limpiamos la pantalla y mostramos un error legible
            limpiar_pantalla()
            print(ROJO + "Informe de error" + RESET)
            print(str(e))  # Convertimos la excepción a cadena para mostrarla correctamente

    return 0


# Iniciar programa
if __name__ == "__main__":
    main()
