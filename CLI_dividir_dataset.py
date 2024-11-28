import pandas as pd
import random
import os
import pyfiglet
import encodings

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

def mostrar_datos_actuales(ruta_dataset: str, dataset: pd.DataFrame):
    if any([ruta_dataset, dataset]):
        if ruta_dataset:
            print(MAGENTA + "Ruta dataset: " + RESET, ruta_dataset)
        if dataset is not None:
            print(MAGENTA + "Dataset cargado." + RESET)
    else:
        print(AMARILLO + "No hay datos agregados." + RESET)
        
def mostrar_menu_principal(limpiar_pantalla_activado):
    """Muestra el menú principal del programa"""
    print(MAGENTA + NEGRITA + "MENU PRINCIPAL" + RESET)
    print(VERDE + "1. Cargar datos")
    print("2. Tipo de particionado")
    print("3. Particionar")
    if limpiar_pantalla_activado:
        print(AMARILLO + "4. Desactivar limpieza de pantalla")
    else:
        print(AMARILLO + "4. Activar limpieza de pantalla")
    print(VERDE + "5. Guardar datasets resultantes")
    print(ROJO + "0. Salir" + RESET)
    
    
    return input(AZUL + NEGRITA + "Seleccione una opción: " + RESET)

# Función para mostrar los encodings disponibles
def mostrar_encodings_disponibles():
    """Muestra encodings disponibles en páginas, destacando los comunes en la primera página."""
    encodings_comunes = ['utf-8', 'latin-1', 'ascii', 'utf-16', 'cp1252']
    encodings_disponibles = list(encodings.aliases.aliases.keys())
    encodings_disponibles = [e for e in encodings_disponibles if e not in encodings_comunes]
    
    # Insertar los encodings comunes al principio
    encodings_disponibles = encodings_comunes + encodings_disponibles
    tamanio_pagina = 10
    total_paginas = (len(encodings_disponibles) + tamanio_pagina - 1) // tamanio_pagina

    pagina_actual = 0
    while True:
        limpiar_pantalla()
        print(f"{MAGENTA}{NEGRITA}ENCODINGS DISPONIBLES{RESET}")
        inicio = pagina_actual * tamanio_pagina
        fin = inicio + tamanio_pagina
        
        # Mostrar la página actual
        print(f"{CYAN}{NEGRITA}Página {pagina_actual + 1} de {total_paginas}:{RESET}")
        for i, encoding in enumerate(encodings_disponibles[inicio:fin], start=1):
            # Encodings comunes resaltados
            if encoding in encodings_comunes:
                print(f"{VERDE}{NEGRITA}{inicio + i}. {encoding}{RESET}")
            else:
                print(f"{BLANCO}{inicio + i}. {encoding}{RESET}")

        # Opciones para la navegación
        print(f"\n{AMARILLO}{NEGRITA}Opciones:{RESET}")
        print(f"{AZUL}[n]{RESET} Siguiente página")
        print(f"{AZUL}[p]{RESET} Página anterior")
        print(f"{AZUL}[q]{RESET} Salir")
        print(f"O elige un {SUBRAYADO}número{RESET} para seleccionar un encoding.")

        opcion = input(f"\n{CYAN}Elige una opción: {RESET}").strip().lower()
        if opcion == 'n' and pagina_actual < total_paginas - 1:
            pagina_actual += 1
        elif opcion == 'p' and pagina_actual > 0:
            pagina_actual -= 1
        elif opcion == 'q':
            print(f"{ROJO}Saliendo...{RESET}")
            return None
        else:
            try:
                eleccion = int(opcion)
                if inicio + 1 <= eleccion <= min(fin, len(encodings_disponibles)):
                    encoding_elegido = encodings_disponibles[eleccion - 1]
                    print(f"{VERDE}Has elegido: {NEGRITA}{encoding_elegido}{RESET}")
                    return encoding_elegido
                else:
                    print(f"{ROJO}Número inválido. Por favor, elige un número de la lista.{RESET}")
            except ValueError:
                print(f"{ROJO}Entrada inválida. Por favor, intenta de nuevo.{RESET}")

# Función para cargar los datos
def cargar_datos():
    """Carga un dataset en formato CSV."""
    limpiar_pantalla()
    while True:
        print(AZUL + NEGRITA + "CARGAR DATOS" + RESET)
        ruta_dataset = input("Ingrese la ruta del dataset: ")
        encoding = mostrar_encodings_disponibles()
        if encoding is None:
            print(ROJO + "No se ha seleccionado un encoding. Por favor, intenta de nuevo." + RESET)
            input("Presione Enter para continuar...")
            return None, None
        try:
            dataset = pd.read_csv(ruta_dataset, encoding=encoding)
            return ruta_dataset, dataset, encoding
        except Exception as e:
            limpiar_pantalla()
            print(ROJO + "Error al cargar el dataset" + RESET)
            print(AMARILLO + str(e) + RESET)
            
def menu_tipo_particionado():
    """Menú para seleccionar el tipo de particionado."""
    limpiar_pantalla()
    print(AZUL + NEGRITA + "TIPO DE PARTICIONADO" + RESET)
    print(VERDE + "1. División por porcentaje")
    print("2. División por k-folds")
    print("3. División por leave-one-out")
    print("4. Tomar muestra aleatoria de tamaño determinado")
    return int(input(AZUL + NEGRITA + "Seleccione el tipo de particionado: " + RESET))

def particionar_dataset(dataset, tipo_particionado):
    """Realiza el particionado del dataset según el tipo seleccionado."""
    # arreglo de datasets retornados
    datasets = []
    if dataset is None:
        print(ROJO + "No se ha cargado ningún dataset." + RESET)
        input("Presione Enter para continuar...")
        return
    
    if tipo_particionado == 1:
        # División por porcentaje
        porcentaje = float(input("Ingrese el porcentaje de entrenamiento (0-100): "))
        train = dataset.sample(frac=porcentaje / 100, random_state=42)
        test = dataset.drop(train.index)
        print(f"{VERDE}Dataset dividido: {len(train)} entrenamiento y {len(test)} prueba.{RESET}")
        datasets.append(train)
        datasets.append(test)
    elif tipo_particionado == 2:
        # División por k-folds
        from sklearn.model_selection import KFold
        k = int(input("Ingrese el número de folds (k): "))
        kf = KFold(n_splits=k, shuffle=True, random_state=42)
        for fold, (train_index, test_index) in enumerate(kf.split(dataset), start=1):
            print(f"Fold {fold}: {len(train_index)} entrenamiento y {len(test_index)} prueba.")
            train = dataset.iloc[train_index]
            test = dataset.iloc[test_index]
            datasets.append(train)
            datasets.append(test)
    elif tipo_particionado == 3:
        # División por leave-one-out
        from sklearn.model_selection import LeaveOneOut
        loo = LeaveOneOut()
        for train_index, test_index in loo.split(dataset):
            print(f"Entrenamiento: {len(train_index)}, Prueba: {len(test_index)}")
            train = dataset.iloc[train_index]
            test = dataset.iloc[test_index]
            datasets.append(train)
            datasets.append(test)
    elif tipo_particionado == 4:
        # Muestra aleatoria de tamaño determinado
        print (VERDE + "Tomar muestra aleatoria de tamaño determinado" + RESET)
        print (AMARILLO + "El tamaño de la muestra debe ser menor o igual a " + str(len(dataset)) + RESET)
        tamanio_muestra = int(input("Ingrese el tamaño de la muestra: "))
        # verificamos que el tamaño de la muestra sea menor o igual al tamaño del dataset   
        if tamanio_muestra < len(dataset):
            muestra = dataset.sample(n=tamanio_muestra, random_state=42)
            print(f"{VERDE}Muestra tomada: {len(muestra)} elementos.{RESET}")
        else:
            print(ROJO + "El tamaño de la muestra debe ser menor o igual al tamaño del dataset." + RESET)
        datasets.append(muestra)
            
    else:
        print(ROJO + "Tipo de particionado no válido." + RESET)

    input("Presione Enter para continuar...")
    return datasets

def guardar_datasets_resultantes(datasets_resultantes, tipo_particionado, codificacion):
    print(AMARILLO + "Guardar datasets resultantes" + RESET)
    if not datasets_resultantes:
        print(ROJO + "No hay datasets para guardar." + RESET)
        input("Presione Enter para continuar...")
        return
    if tipo_particionado == 1:
        # División por porcentaje
        train, test = datasets_resultantes
        train.to_csv("train.csv", index=False, encoding=codificacion)
        test.to_csv("test.csv", index=False, encoding=codificacion)
        print(f"{VERDE}Datasets guardados: train.csv y test.csv{RESET}")
    elif tipo_particionado == 2:
        # División por k-folds
        for i, dataset in enumerate(datasets_resultantes, start=1):
            if i % 2 == 1:
                dataset.to_csv(f"train_fold_{i}.csv", index=False, encoding=codificacion)
            else:
                dataset.to_csv(f"test_fold_{i}.csv", index=False, encoding=codificacion)
            #dataset.to_csv(f"fold_{i}.csv", index=False)
        print(f"{VERDE}Datasets guardados: fold_1.csv, fold_2.csv, ...{RESET}")
    elif tipo_particionado == 3:
        # División por leave-one-out
        for i, dataset in enumerate(datasets_resultantes, start=1):
            dataset.to_csv(f"leave_one_out_{i}.csv", index=False, encoding=codificacion)
        print(f"{VERDE}Datasets guardados: leave_one_out_1.csv, leave_one_out_2.csv, ...{RESET}")
    elif tipo_particionado == 4:
        # Muestra aleatoria de tamaño determinado
        muestra = datasets_resultantes[0]
        muestra.to_csv("muestra.csv", index=False, encoding=codificacion)
        print(f"{VERDE}Muestra guardada: muestra.csv{RESET}")
   

if __name__ == "__main__":
    limpiar_pantalla_activado = True
    ruta_data_set = None
    dataset = None
    codificacion = None
    tipo_particionado = None
    datasets_resultantes = []
    while True:
        try:
            if limpiar_pantalla_activado:
                limpiar_pantalla()
            print(AZUL + NEGRITA + "Bienvenido " + os.getlogin() + "!")
            mostrar_datos_actuales(ruta_data_set, dataset)
            seleccion = int(mostrar_menu_principal(limpiar_pantalla_activado))
            if seleccion == 1:
                ruta_data_set, dataset, codificacion = cargar_datos()
            elif seleccion == 2:
                tipo_particionado = menu_tipo_particionado()
            elif seleccion == 3:
                datasets_resultantes = particionar_dataset(dataset, tipo_particionado)
                input("Presione Enter para continuar...")
            elif seleccion == 4:
                limpiar_pantalla_activado = not limpiar_pantalla_activado
            elif seleccion == 5:
                guardar_datasets_resultantes(datasets_resultantes, tipo_particionado, codificacion)
            elif seleccion == 0:
                limpiar_pantalla()
                print(AMARILLO + "Saliendo..." + RESET)
                ascii_art = pyfiglet.figlet_format("Desarrollado por:")
                print(ROJO + ascii_art + RESET)
                ascii_art = pyfiglet.figlet_format("Aether")
                print(CYAN + ascii_art + RESET)
                break
            else:
                print(ROJO + "Opción inválida" + RESET)
        except Exception as e:
            limpiar_pantalla()
            print(ROJO + "Informe de error" + RESET)
            print(str(e))
            input("Presione Enter para continuar...")