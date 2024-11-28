import sys
import pandas as pd
import numpy as np
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

# Diccionario original
ruta_diccionario_original = "./conjunto_de_datos_enut_2019_csv/conjunto_de_datos_enut_2019/conjunto_de_datos_tmodulo_enut_2019/diccionario_de_datos/diccionario_datos_tmodulo_enut_2019.csv"
# Ruta dataset
ruta_dataset = "./conjunto_de_datos_enut_2019_csv/conjunto_de_datos_enut_2019/conjunto_de_datos_tmodulo_enut_2019/conjunto_de_datos/conjunto_de_datos_tmodulo_enut_2019.csv"
# Rutas de catalogos
ruta_catalogo_sexo = "./conjunto_de_datos_enut_2019_csv/conjunto_de_datos_enut_2019/conjunto_de_datos_tsdem_enut_2019/catalogos/sexo.csv"
ruta_catalogo_permiso_enfermedad_maternidad = "./conjunto_de_datos_enut_2019_csv/conjunto_de_datos_enut_2019/conjunto_de_datos_tmodulo_enut_2019/catalogos/p5_6_1.csv"
ruta_catalogo_trabajo_al_menos_1_hora = "./conjunto_de_datos_enut_2019_csv/conjunto_de_datos_enut_2019/conjunto_de_datos_tmodulo_enut_2019/catalogos/p5_1.csv"
ruta_catalogo_permiso_vacaciones = "./conjunto_de_datos_enut_2019_csv/conjunto_de_datos_enut_2019/conjunto_de_datos_tmodulo_enut_2019/catalogos/p5_6_2.csv"
ruta_catalogo_derecho_jubilacion = "./conjunto_de_datos_enut_2019_csv/conjunto_de_datos_enut_2019/conjunto_de_datos_tmodulo_enut_2019/catalogos/p5_6_3.csv"
ruta_catalogo_derecho_servicios_medicos = "./conjunto_de_datos_enut_2019_csv/conjunto_de_datos_enut_2019/conjunto_de_datos_tmodulo_enut_2019/catalogos/p5_6_6.csv"
ruta_catalogo_sentimiento_quehaceres_hogar = "./conjunto_de_datos_enut_2019_csv/conjunto_de_datos_enut_2019/conjunto_de_datos_tmodulo_enut_2019/catalogos/p7_1_1.csv"
ruta_catalogo_sentimiento_estudio = "./conjunto_de_datos_enut_2019_csv/conjunto_de_datos_enut_2019/conjunto_de_datos_tmodulo_enut_2019/catalogos/p7_1_2.csv"
ruta_catalogo_sentimiento_trabajo = "./conjunto_de_datos_enut_2019_csv/conjunto_de_datos_enut_2019/conjunto_de_datos_tmodulo_enut_2019/catalogos/p7_1_3.csv"
ruta_catalogo_sentimiento_cuidado_apoyo_familiares = "./conjunto_de_datos_enut_2019_csv/conjunto_de_datos_enut_2019/conjunto_de_datos_tmodulo_enut_2019/catalogos/p7_1_4.csv"
ruta_catalogo_sentimiento_ocio_convivencia = "./conjunto_de_datos_enut_2019_csv/conjunto_de_datos_enut_2019/conjunto_de_datos_tmodulo_enut_2019/catalogos/p7_1_5.csv"
ruta_catalogo_sentimiento_traslado = "./conjunto_de_datos_enut_2019_csv/conjunto_de_datos_enut_2019/conjunto_de_datos_tmodulo_enut_2019/catalogos/p7_1_6.csv"
ruta_catalogo_sentimiento_tramites_pagos = "./conjunto_de_datos_enut_2019_csv/conjunto_de_datos_enut_2019/conjunto_de_datos_tmodulo_enut_2019/catalogos/p7_1_7.csv"
ruta_catalogo_sentimiento_vida_general = "./conjunto_de_datos_enut_2019_csv/conjunto_de_datos_enut_2019/conjunto_de_datos_tmodulo_enut_2019/catalogos/p7_2_1.csv"
ruta_catalogo_sentimiento_vida_familiar = "./conjunto_de_datos_enut_2019_csv/conjunto_de_datos_enut_2019/conjunto_de_datos_tmodulo_enut_2019/catalogos/p7_2_2.csv"
ruta_catalogo_sentimiento_vida_afectiva = "./conjunto_de_datos_enut_2019_csv/conjunto_de_datos_enut_2019/conjunto_de_datos_tmodulo_enut_2019/catalogos/p7_2_3.csv"
ruta_catalogo_sentimiento_vida_social = "./conjunto_de_datos_enut_2019_csv/conjunto_de_datos_enut_2019/conjunto_de_datos_tmodulo_enut_2019/catalogos/p7_2_4.csv"
ruta_catalogo_sentimiento_situacion_economica = "./conjunto_de_datos_enut_2019_csv/conjunto_de_datos_enut_2019/conjunto_de_datos_tmodulo_enut_2019/catalogos/p7_2_5.csv"
ruta_catalogo_sentimiento_vivienda = "./conjunto_de_datos_enut_2019_csv/conjunto_de_datos_enut_2019/conjunto_de_datos_tmodulo_enut_2019/catalogos/p7_2_6.csv"
ruta_catalogo_sentimiento_felicidad_general = "./conjunto_de_datos_enut_2019_csv/conjunto_de_datos_enut_2019/conjunto_de_datos_tmodulo_enut_2019/catalogos/p7_3.csv"

def main():
    # Crear la aplicación una sola vez
    app = QApplication(sys.argv)
    
    # Cargar el diccionario original y mostrarlo en una ventana
    diccionario_original = pd.read_csv(ruta_diccionario_original)
    ventana1 = mostrar_dataframe_en_qt(diccionario_original, "Diccionario Original")
    
    # Cargar el dataset original
    dataset = pd.read_csv(ruta_dataset)
    
    # creamos un nuevo dataframe vacío
    dataset_limpio = pd.DataFrame()
    
    # eliminamos los valores nulos 
    dataset = dataset.fillna(0)  # Reemplaza NaN con 0 
    
    # Eliminamos los valores 99999 para la pregunta P5_7 (Salario)
    dataset = dataset[dataset["P5_7"] != 99999]
    dataset.reset_index(drop=True, inplace=True)

    
    
    # creamos un nuevo dataframe vacío
    dataset_limpio = pd.DataFrame()
    
    dataset_limpio["Entidad"] = dataset["ENT"]
    
    # Pregunta Sexo
    dataset_limpio["Sexo"] = dataset["SEXO"]
    catalogo_sexo = pd.read_csv(ruta_catalogo_sexo)
    dataset_limpio["Sexo"] = dataset_limpio["Sexo"].replace(catalogo_sexo.set_index("cve").to_dict()["descrip"])
    
    # Pregunta Edad
    dataset_limpio["Edad"] = dataset["EDAD_V"]
    
    # Pregunta P5_1
    dataset_limpio["TrabajoAlMenos1Hora"] = dataset["P5_1"]
    catalogo_trabajo_al_menos_1_hora = pd.read_csv(ruta_catalogo_trabajo_al_menos_1_hora, encoding="latin-1")
    dataset_limpio["TrabajoAlMenos1Hora"] = dataset_limpio["TrabajoAlMenos1Hora"].replace(catalogo_trabajo_al_menos_1_hora.set_index("cve").to_dict()["descrip"])
    
    # ESTA EN HORAS TOTALES
    dataset_limpio["TiempoTrabajoLV"] = dataset["P5_3_1"] + (dataset["P5_3_2"] / 60)
    # ESTA EN HORAS TOTALES
    dataset_limpio["TiempoTrabajoSD"] = dataset["P5_3_3"] + (dataset["P5_3_4"] / 60)
    # ESTA EN HORAS TOTALES
    dataset_limpio["TiempoTrasladoLV"] = dataset["P5_4_1"] + (dataset["P5_4_2"] / 60)
    # ESTA EN HORAS TOTALES
    dataset_limpio["TiempoTrasladoSD"] = dataset["P5_4_3"] + (dataset["P5_4_4"] / 60)
    
    
    
    # Pregunta P5_7 (Salario) 
    # lo hacemos anual
    dataset["P5_7"] = dataset.apply(lambda fila: fila['P5_7'] * 52 if fila['P5_7A'] == 1 else fila['P5_7'] * 26 if fila['P5_7A'] == 2 else fila['P5_7'] * 12 if fila['P5_7A'] == 3 else fila['P5_7'] * 1 if fila['P5_7A'] == 4 else 0, axis=1)
    
    dataset_limpio["Salario"] = dataset["P5_7"]
    
    # Pregunta P5_6_1 
    dataset_limpio["PermisoEnfermedadMaternidadAccidente"] = dataset["P5_6_1"]
    catalogo_permiso_enfermedad_maternidad = pd.read_csv(ruta_catalogo_permiso_enfermedad_maternidad, encoding="latin-1")
    dataset_limpio["PermisoEnfermedadMaternidadAccidente"] = dataset_limpio["PermisoEnfermedadMaternidadAccidente"].replace(catalogo_permiso_enfermedad_maternidad.set_index("cve").to_dict()["descrip"])
    
    # Pregunta P5_6_2
    dataset_limpio["PermisoVacaciones"] = dataset["P5_6_2"]
    catalogo_permiso_vacaciones = pd.read_csv(ruta_catalogo_permiso_vacaciones, encoding="latin-1")
    dataset_limpio["PermisoVacaciones"] = dataset_limpio["PermisoVacaciones"].replace(catalogo_permiso_vacaciones.set_index("cve").to_dict()["descrip"])
    
    # Pregunta P5_6_3
    dataset_limpio["DerechoJubilación"] = dataset["P5_6_3"]
    catalogo_derecho_jubilacion = pd.read_csv(ruta_catalogo_derecho_jubilacion, encoding="latin-1")
    dataset_limpio["DerechoJubilación"] = dataset_limpio["DerechoJubilación"].replace(catalogo_derecho_jubilacion.set_index("cve").to_dict()["descrip"])
    
    # Pregunta P5_6_6
    dataset_limpio["DerechoServiciosMedicos"] = dataset["P5_6_6"]
    catalogo_derecho_servicios_medicos = pd.read_csv(ruta_catalogo_derecho_servicios_medicos, encoding="latin-1")
    dataset_limpio["DerechoServiciosMedicos"] = dataset_limpio["DerechoServiciosMedicos"].replace(catalogo_derecho_servicios_medicos.set_index("cve").to_dict()["descrip"])
    
    # Pregunta P6_1_1_1, P6_1_1_2, P6_1_1_3, P6_1_1_4
    dataset_limpio["TiempoDedicadoADormirLV"] = dataset["P6_1_1_1"] + (dataset["P6_1_1_2"] / 60)
    dataset_limpio["TiempoDedicadoADormirSD"] = dataset["P6_1_1_3"] + (dataset["P6_1_1_4"] / 60)
    
    # Pregunta P6_1_2_1, P6_1_2_2, P6_1_2_3, P6_1_2_4
    dataset_limpio["TiempoDedicadoAComerLV"] = dataset["P6_1_2_1"] + (dataset["P6_1_2_2"] / 60)
    dataset_limpio["TiempoDedicadoAComerSD"] = dataset["P6_1_2_3"] + (dataset["P6_1_2_4"] / 60)
    
    # Pregunta P6_1_3_1, P6_1_3_2, P6_1_3_3, P6_1_3_4
    dataset_limpio["TiempoDedicadoAAseoPersonalLV"] = dataset["P6_1_3_1"] + (dataset["P6_1_3_2"] / 60) + dataset["P6_6A_5_1"] + (dataset["P6_6A_5_2"] / 60)
    dataset_limpio["TiempoDedicadoAAseoPersonalSD"] = dataset["P6_1_3_3"] + (dataset["P6_1_3_4"] / 60) + dataset["P6_6A_5_3"] + (dataset["P6_6A_5_4"] / 60)
    
    # Pregunta P6_2_1, P6_2_2, P6_2_3
    dataset_limpio["TiempoDedicadoAActividadesEstudioLV"] = dataset["P6_2A_1_1"] + (dataset["P6_2A_1_2"] / 60) + dataset["P6_2A_2_1"] + (dataset["P6_2A_2_2"] / 60)
    dataset_limpio["TiempoDedicadoAActividadesEstudioSD"] = dataset["P6_2A_1_3"] + (dataset["P6_2A_1_4"] / 60) + dataset["P6_2A_2_3"] + (dataset["P6_2A_2_4"] / 60)
    
    # Pregunta P6_2_4, P6_2_5
    dataset_limpio["TiempoDedicadoATrasladarEstudianteLV"] = dataset["P6_2A_3_1"] + (dataset["P6_2A_3_2"] / 60)
    dataset_limpio["TiempoDedicadoATrasladarEstudianteSD"] = dataset["P6_2A_3_3"] + (dataset["P6_2A_3_4"] / 60)
    
    # Pregunta P6_4_1, P6_4_2, P6_4_3, P6_4_4, P6_5_1, P6_5_2, P6_5_3, P6_5_4, P6_6_1, P6_6_2, P6_6_3, P6_6_4, P6_10_5, P6_10_6, P6_3_7
    dataset_limpio["QuehaceresDomésticosLV"] = dataset["P6_4A_1_1"] + (dataset["P6_4A_1_2"] / 60) + dataset["P6_4A_2_1"] + (dataset["P6_4A_2_2"] / 60) + dataset["P6_4A_3_1"] + (dataset ["P6_4A_3_2"] / 60) + dataset["P6_4A_4_1"] + (dataset["P6_4A_4_2"] / 60) + dataset["P6_5A_1_1"] + (dataset["P6_5A_1_2"] / 60) + dataset["P6_5A_2_1"] + (dataset["P6_5A_2_2"] / 60) + dataset["P6_5A_3_1"] + (dataset["P6_5A_3_2"] / 60) + dataset["P6_5A_4_1"] + (dataset["P6_5A_4_2"] / 60) + dataset["P6_5A_5_1"] + (dataset["P6_5A_5_2"] / 60) + dataset["P6_6A_1_1"] + (dataset["P6_6A_1_2"] / 60) + dataset["P6_6A_2_1"] + (dataset["P6_6A_2_2"] / 60) + dataset["P6_6A_3_1"] + (dataset["P6_6A_3_2"] / 60) + dataset["P6_6A_4_1"] + (dataset["P6_6A_4_2"] / 60) + dataset["P6_10A_5_1"] + (dataset["P6_10A_5_2"] / 60) + dataset["P6_10A_6_1"] + (dataset["P6_10A_6_2"] / 60) + dataset["P6_3A_7_1"] + (dataset["P6_3A_7_2"] / 60)
    dataset_limpio["QuehaceresDomésticosSD"] = dataset["P6_4A_1_3"] + (dataset["P6_4A_1_4"] / 60) + dataset["P6_4A_2_3"] + (dataset["P6_4A_2_4"] / 60) + dataset["P6_4A_3_3"] + (dataset ["P6_4A_3_4"] / 60) + dataset["P6_4A_4_3"] + (dataset["P6_4A_4_4"] / 60) + dataset["P6_5A_1_3"] + (dataset["P6_5A_1_4"] / 60) + dataset["P6_5A_2_3"] + (dataset["P6_5A_2_4"] / 60) + dataset["P6_5A_3_3"] + (dataset["P6_5A_3_4"] / 60) + dataset["P6_5A_4_3"] + (dataset["P6_5A_4_4"] / 60) + dataset["P6_5A_5_3"] + (dataset["P6_5A_5_4"] / 60) + dataset["P6_6A_1_3"] + (dataset["P6_6A_1_4"] / 60) + dataset["P6_6A_2_3"] + (dataset["P6_6A_2_4"] / 60) + dataset["P6_6A_3_3"] + (dataset["P6_6A_3_4"] / 60) + dataset["P6_6A_4_3"] + (dataset["P6_6A_4_4"] / 60) + dataset["P6_10A_5_3"] + (dataset["P6_10A_5_4"] / 60) + dataset["P6_10A_6_3"] + (dataset["P6_10A_6_4"] / 60) + dataset["P6_3A_7_3"] + (dataset["P6_3A_7_4"] / 60)
    
    # ordenamos de mayor a menor
    dataset_limpio = dataset_limpio.sort_values(by="QuehaceresDomésticosLV", ascending=False)
    
    dataset_limpio["TiempoGanaderíaAutoconsumoLV"] = dataset["P6_3A_1_1"] + (dataset["P6_3A_1_2"] / 60)
    dataset_limpio["TiempoGanaderíaAutoconsumoSD"] = dataset["P6_3A_1_3"] + (dataset["P6_3A_1_4"] / 60)
    dataset_limpio["TiempoActividadesRecolecciónLV"] = dataset["P6_3A_2_1"] + (dataset["P6_3A_2_2"] / 60) + dataset["P6_3A_3_1"] + (dataset["P6_3A_3_2"] / 60) + dataset["P6_3A_5_1"] + (dataset["P6_3A_5_2"] / 60)
    dataset_limpio["TiempoActividadesRecolecciónSD"] = dataset["P6_3A_2_3"] + (dataset["P6_3A_2_4"] / 60) + dataset["P6_3A_3_3"] + (dataset["P6_3A_3_4"] / 60) + dataset["P6_3A_5_3"] + (dataset["P6_3A_5_4"] / 60)
    
    dataset_limpio["TiempoAgriculturaAutoconsumoLV"] = dataset["P6_3A_4_1"] + (dataset["P6_3A_4_2"] / 60)
    dataset_limpio["TiempoAgriculturaAutoconsumoSD"] = dataset["P6_3A_4_3"] + (dataset["P6_3A_4_4"] / 60)
    
    # pregunta p6_3_6
    # para la p6_3a_6_1, p6_3a_6_2, p6_3a_6_3, p6_3a_6_4
    dataset_limpio["TiempoConfecciónCaseraLV"] = dataset["P6_3A_6_1"] + (dataset["P6_3A_6_2"] / 60)
    dataset_limpio["TiempoConfecciónCaseraSD"] = dataset["P6_3A_6_3"] + (dataset["P6_3A_6_4"] / 60)
    
    # pregunta p6_3_8, p6_3_9, p6_7_1, p6_7_2, p6_7_3, p6_7_4
    # para la p6_3a_7_1, p6_3a_7_2, p6_3a_7_3, p6_3a_7_4, p6_3a_8_1, p6_3a_8_2, p6_3a_8_3, p6_3a_8_4, p6_3a_9_1, p6_3a_9_2, p6_3a_9_3, p6_3a_9_4, p6_3a_10_1, p6_3a_10_2, p6_3a_10_3, p6_3a_10_4
    dataset_limpio["TiempoMantenimientoHogarLV"] = dataset["P6_3A_8_1"] + (dataset["P6_3A_8_2"] / 60) + dataset["P6_3A_9_1"] + (dataset["P6_3A_9_2"] / 60) + dataset["P6_7A_1_1"] + (dataset["P6_7A_1_2"] / 60) + dataset["P6_7A_2_1"] + (dataset["P6_7A_2_2"] / 60) + dataset["P6_7A_3_1"] + (dataset["P6_7A_3_2"] / 60) + dataset["P6_7A_4_1"] + (dataset["P6_7A_4_2"] / 60)
    dataset_limpio["TiempoMantenimientoHogarSD"] = dataset["P6_3A_8_3"] + (dataset["P6_3A_8_4"] / 60) + dataset["P6_3A_9_3"] + (dataset["P6_3A_9_4"] / 60) + dataset["P6_7A_1_3"] + (dataset["P6_7A_1_4"] / 60) + dataset["P6_7A_2_3"] + (dataset["P6_7A_2_4"] / 60) + dataset["P6_7A_3_3"] + (dataset["P6_7A_3_4"] / 60) + dataset["P6_7A_4_3"] + (dataset["P6_7A_4_4"] / 60)
    
    # pregunta p6_8_1, p6_8_2, p6_8_3
    # para la p6_8a_1_1, p6_8a_1_2, p6_8a_1_3, p6_8a_1_4, p6_8a_2_1, p6_8a_2_2, p6_8a_2_3, p6_8a_2_4, p6_8a_3_1, p6_8a_3_2, p6_8a_3_3, p6_8a_3_4
    dataset_limpio["TiempoComprasDelHogarLV"] = dataset["P6_8A_1_1"] + (dataset["P6_8A_1_2"] / 60) + dataset["P6_8A_2_1"] + (dataset["P6_8A_2_2"] / 60) + dataset["P6_8A_3_1"] + (dataset["P6_8A_3_2"] / 60)
    dataset_limpio["TiempoComprasDelHogarSD"] = dataset["P6_8A_1_3"] + (dataset["P6_8A_1_4"] / 60) + dataset["P6_8A_2_3"] + (dataset["P6_8A_2_4"] / 60) + dataset["P6_8A_3_3"] + (dataset["P6_8A_3_4"] / 60)
    
    # pregunta p6_9_1, p6_9_3
    # para la p6_9a_1_1, p6_9a_1_2, p6_9a_1_3, p6_9a_1_4, p6_9a_3_1, p6_9a_3_2, p6_9a_3_3, p6_9a_3_4
    dataset_limpio["TiempoTramitesPagosLV"] = dataset["P6_9A_1_1"] + (dataset["P6_9A_1_2"] / 60) + dataset["P6_9A_3_1"] + (dataset["P6_9A_3_2"] / 60)
    dataset_limpio["TiempoTramitesPagosSD"] = dataset["P6_9A_1_3"] + (dataset["P6_9A_1_4"] / 60) + dataset["P6_9A_3_3"] + (dataset["P6_9A_3_4"] / 60) 
    
    # pregunta p6_9_2, p6_10_7
    # para la p6_9a_2_1, p6_9a_2_2, p6_9a_2_3, p6_9a_2_4, p6_10a_7_1, p6_10a_7_2, p6_10a_7_3, p6_10a_7_4
    dataset_limpio["TiempoOrganizaciónHogarLV"] = dataset["P6_9A_2_1"] + (dataset["P6_9A_2_2"] / 60) + dataset["P6_10A_7_1"] + (dataset["P6_10A_7_2"] / 60)
    dataset_limpio["TiempoOrganizaciónHogarSD"] = dataset["P6_9A_2_3"] + (dataset["P6_9A_2_4"] / 60) + dataset["P6_10A_7_3"] + (dataset["P6_10A_7_4"] / 60)
    
    # Tiempo de mantenimiento del hogar
    # pregunta p6_10_1, p6_10_2, p6_10_3
    # para la p6_10a_1_1, p6_10a_1_2, p6_10a_1_3, p6_10a_1_4, p6_10a_2_1, p6_10a_2_2, p6_10a_2_3, p6_10a_2_4, p6_10a_3_1, p6_10a_3_2, p6_10a_3_3, p6_10a_3_4, p6_10a_5_1, p6_10a_5_2, p6_10a_5_3, p6_10a_5_4
    dataset_limpio["TiempoMantenimientoHogarTercerosLV"] = dataset["P6_10A_1_1"] + (dataset["P6_10A_1_2"] / 60) + dataset["P6_10A_2_1"] + (dataset["P6_10A_2_2"] / 60) + dataset["P6_10A_3_1"] + (dataset["P6_10A_3_2"] / 60)
    dataset_limpio["TiempoMantenimientoHogarTercerosSD"] = dataset["P6_10A_1_3"] + (dataset["P6_10A_1_4"] / 60) + dataset["P6_10A_2_3"] + (dataset["P6_10A_2_4"] / 60) + dataset["P6_10A_3_3"] + (dataset["P6_10A_3_4"] / 60)
    
    # Tiempo cuidados especiales para otra persona
    # preguntas p6_11_01, p6_11_02, p6_11_03, p6_11_04, p6_11_05, p6_11_06, p6_11_07, p6_11_08, p6_11_09, p6_11_10, p6_11_11
    # para la p6_11a_01_1, p6_11a_01_2, p6_11a_01_3, p6_11a_01_4, p6_11a_02_1, p6_11a_02_2, p6_11a_02_3, p6_11a_02_4, p6_11a_03_1, p6_11a_03_2, p6_11a_03_3, p6_11a_03_4, p6_11a_04_1, p6_11a_04_2, p6_11a_04_3, p6_11a_04_4, p6_11a_05_1, p6_11a_05_2, p6_11a_05_3, p6_11a_05_4, p6_11a_06_1, p6_11a_06_2, p6_11a_06_3, p6_11a_06_4, p6_11a_07_1, p6_11a_07_2, p6_11a_07_3, p6_11a_07_4, p6_11a_08_1, p6_11a_08_2, p6_11a_08_3, p6_11a_08_4, p6_11a_09_1, p6_11a_09_2, p6_11a_09_3, p6_11a_09_4, p6_11a_10_1, p6_11a_10_2, p6_11a_10_3, p6_11a_10_4, p6_11a_11_1, p6_11a_11_2, p6_11a_11_3, p6_11a_11_4
    dataset_limpio["TiempoCuidadosEspecialesOtraPersonaLV"] = dataset["P6_11A_01_1"] + (dataset["P6_11A_01_2"] / 60) + dataset["P6_11A_02_1"] + (dataset["P6_11A_02_2"] / 60) + dataset["P6_11A_03_1"] + (dataset["P6_11A_03_2"] / 60) + dataset["P6_11A_04_1"] + (dataset["P6_11A_04_2"] / 60) + dataset["P6_11A_05_1"] + (dataset["P6_11A_05_2"] / 60) + dataset["P6_11A_06_1"] + (dataset["P6_11A_06_2"] / 60) + dataset["P6_11A_07_1"] + (dataset["P6_11A_07_2"] / 60) + dataset["P6_11A_08_1"] + (dataset["P6_11A_08_2"] / 60) + dataset["P6_11A_09_1"] + (dataset["P6_11A_09_2"] / 60) + dataset["P6_11A_10_1"] + (dataset["P6_11A_10_2"] / 60) + dataset["P6_11A_11_1"] + (dataset["P6_11A_11_2"] / 60)
    dataset_limpio["TiempoCuidadosEspecialesOtraPersonaSD"] = dataset["P6_11A_01_3"] + (dataset["P6_11A_01_4"] / 60) + dataset["P6_11A_02_3"] + (dataset["P6_11A_02_4"] / 60) + dataset["P6_11A_03_3"] + (dataset["P6_11A_03_4"] / 60) + dataset["P6_11A_04_3"] + (dataset["P6_11A_04_4"] / 60) + dataset["P6_11A_05_3"] + (dataset["P6_11A_05_4"] / 60) + dataset["P6_11A_06_3"] + (dataset["P6_11A_06_4"] / 60) + dataset["P6_11A_07_3"] + (dataset["P6_11A_07_4"] / 60) + dataset["P6_11A_08_3"] + (dataset["P6_11A_08_4"] / 60) + dataset["P6_11A_09_3"] + (dataset["P6_11A_09_4"] / 60) + dataset["P6_11A_10_3"] + (dataset["P6_11A_10_4"] / 60) + dataset["P6_11A_11_3"] + (dataset["P6_11A_11_4"] / 60)
    
    # Tiempo Crianza de menores 0-5
    # preguntas p6_12_1, p6_12_2, p6_12_3
    # para la p6_12a_1_1, p6_12a_1_2, p6_12a_1_3, p6_12a_1_4, p6_12a_2_1, p6_12a_2_2, p6_12a_2_3, p6_12a_2_4, p6_12a_3_1, p6_12a_3_2, p6_12a_3_3, p6_12a_3_4
    dataset_limpio["TiempoCrianzaMenores0a5LV"] = dataset["P6_12A_1_1"] + (dataset["P6_12A_1_2"] / 60) + dataset["P6_12A_2_1"] + (dataset["P6_12A_2_2"] / 60) + dataset["P6_12A_3_1"] + (dataset["P6_12A_3_2"] / 60)
    dataset_limpio["TiempoCrianzaMenores0a5SD"] = dataset["P6_12A_1_3"] + (dataset["P6_12A_1_4"] / 60) + dataset["P6_12A_2_3"] + (dataset["P6_12A_2_4"] / 60) + dataset["P6_12A_3_3"] + (dataset["P6_12A_3_4"] / 60)
    
    # Tiempo Crianza de menores 0-14
    # preguntas p6_13_1, p6_13_2, p6_13_3, p6_13_4, p6_13_5, p6_13_6
    # para la p6_13a_1_1, p6_13a_1_2, p6_13a_1_3, p6_13a_1_4, p6_13a_2_1, p6_13a_2_2, p6_13a_2_3, p6_13a_2_4, p6_13a_3_1, p6_13a_3_2, p6_13a_3_3, p6_13a_3_4, p6_13a_4_1, p6_13a_4_2, p6_13a_4_3, p6_13a_4_4, p6_13a_5_1, p6_13a_5_2, p6_13a_5_3, p6_13a_5_4, p6_13a_6_1, p6_13a_6_2, p6_13a_6_3, p6_13a_6_4
    dataset_limpio["TiempoCrianzaMenores0a14LV"] = dataset["P6_13A_1_1"] + (dataset["P6_13A_1_2"] / 60) + dataset["P6_13A_2_1"] + (dataset["P6_13A_2_2"] / 60) + dataset["P6_13A_3_1"] + (dataset["P6_13A_3_2"] / 60) + dataset["P6_13A_4_1"] + (dataset["P6_13A_4_2"] / 60) + dataset["P6_13A_5_1"] + (dataset["P6_13A_5_2"] / 60) + dataset["P6_13A_6_1"] + (dataset["P6_13A_6_2"] / 60)
    dataset_limpio["TiempoCrianzaMenores0a14SD"] = dataset["P6_13A_1_3"] + (dataset["P6_13A_1_4"] / 60) + dataset["P6_13A_2_3"] + (dataset["P6_13A_2_4"] / 60) + dataset["P6_13A_3_3"] + (dataset["P6_13A_3_4"] / 60) + dataset["P6_13A_4_3"] + (dataset["P6_13A_4_4"] / 60) + dataset["P6_13A_5_3"] + (dataset["P6_13A_5_4"] / 60) + dataset["P6_13A_6_3"] + (dataset["P6_13A_6_4"] / 60)
    
    # Tiempo Acompañamiento familiar 15 - 59
    # preguntas p6_4_5, p6_14_1, p6_14_2, p6_14_3
    # para la p6_4a_5_1 p6_4a_5_2, p6_4a_5_3, p6_4a_5_4, p6_14a_1_1, p6_14a_1_2, p6_14a_1_3, p6_14a_1_4, p6_14a_2_1, p6_14a_2_2, p6_14a_2_3, p6_14a_2_4, p6_14a_3_1, p6_14a_3_2, p6_14a_3_3, p6_14a_3_4
    dataset_limpio["TiempoAcompañamientoFamiliar15a59LV"] = dataset["P6_4A_5_1"] + (dataset["P6_4A_5_2"] / 60) + dataset["P6_14A_1_1"] + (dataset["P6_14A_1_2"] / 60) + dataset["P6_14A_2_1"] + (dataset["P6_14A_2_2"] / 60) + dataset["P6_14A_3_1"] + (dataset["P6_14A_3_2"] / 60)
    dataset_limpio["TiempoAcompañamientoFamiliar15a59SD"] = dataset["P6_4A_5_3"] + (dataset["P6_4A_5_4"] / 60) + dataset["P6_14A_1_3"] + (dataset["P6_14A_1_4"] / 60) + dataset["P6_14A_2_3"] + (dataset["P6_14A_2_4"] / 60) + dataset["P6_14A_3_3"] + (dataset["P6_14A_3_4"] / 60)
    
    # Tiempo Acompañamiento familiar 60
    # preguntas p6_15_1, p6_15_2, p6_15_3, p6_15_4
    # para la p6_15a_1_1, p6_15a_1_2, p6_15a_1_3, p6_15a_1_4, p6_15a_2_1, p6_15a_2_2, p6_15a_2_3, p6_15a_2_4, p6_15a_3_1, p6_15a_3_2, p6_15a_3_3, p6_15a_3_4, p6_15a_4_1, p6_15a_4_2, p6_15a_4_3, p6_15a_4_4
    dataset_limpio["TiempoAcompañamientoFamiliar60LV"] = dataset["P6_15A_1_1"] + (dataset["P6_15A_1_2"] / 60) + dataset["P6_15A_2_1"] + (dataset["P6_15A_2_2"] / 60) + dataset["P6_15A_3_1"] + (dataset["P6_15A_3_2"] / 60) + dataset["P6_15A_4_1"] + (dataset["P6_15A_4_2"] / 60)
    dataset_limpio["TiempoAcompañamientoFamiliar60SD"] = dataset["P6_15A_1_3"] + (dataset["P6_15A_1_4"] / 60) + dataset["P6_15A_2_3"] + (dataset["P6_15A_2_4"] / 60) + dataset["P6_15A_3_3"] + (dataset["P6_15A_3_4"] / 60) + dataset["P6_15A_4_3"] + (dataset["P6_15A_4_4"] / 60)
    
    # Tiempo Apoyo a otro hogar
    # preguntas p6_16_1, p6_16_2, p6_16_3, p6_16_4, p6_16_5, p6_16_6
    # para la p6_16a_1_1, p6_16a_1_2, p6_16a_1_3, p6_16a_1_4, p6_16a_2_1, p6_16a_2_2, p6_16a_2_3, p6_16a_2_4, p6_16a_3_1, p6_16a_3_2, p6_16a_3_3, p6_16a_3_4, p6_16a_4_1, p6_16a_4_2, p6_16a_4_3, p6_16a_4_4, p6_16a_5_1, p6_16a_5_2, p6_16a_5_3, p6_16a_5_4, p6_16a_6_1, p6_16a_6_2, p6_16a_6_3, p6_16a_6_4
    dataset_limpio["TiempoApoyoOtroHogarLV"] = dataset["P6_16A_1_1"] + (dataset["P6_16A_1_2"] / 60) + dataset["P6_16A_2_1"] + (dataset["P6_16A_2_2"] / 60) + dataset["P6_16A_3_1"] + (dataset["P6_16A_3_2"] / 60) + dataset["P6_16A_4_1"] + (dataset["P6_16A_4_2"] / 60) + dataset["P6_16A_5_1"] + (dataset["P6_16A_5_2"] / 60) + dataset["P6_16A_6_1"] + (dataset["P6_16A_6_2"] / 60)
    dataset_limpio["TiempoApoyoOtroHogarSD"] = dataset["P6_16A_1_3"] + (dataset["P6_16A_1_4"] / 60) + dataset["P6_16A_2_3"] + (dataset["P6_16A_2_4"] / 60) + dataset["P6_16A_3_3"] + (dataset["P6_16A_3_4"] / 60) + dataset["P6_16A_4_3"] + (dataset["P6_16A_4_4"] / 60) + dataset["P6_16A_5_3"] + (dataset["P6_16A_5_4"] / 60) + dataset["P6_16A_6_3"] + (dataset["P6_16A_6_4"] / 60)
    
    # Tiempo Voluntariado
    # preguntas 6_17_1, p6_17_2
    # para la p6_17a_1_1, p6_17a_1_2, p6_17a_1_3, p6_17a_1_4, p6_17a_2_1, p6_17a_2_2, p6_17a_2_3, p6_17a_2_4
    dataset_limpio["TiempoVoluntariadoLV"] = dataset["P6_17A_1_1"] + (dataset["P6_17A_1_2"] / 60) + dataset["P6_17A_2_1"] + (dataset["P6_17A_2_2"] / 60)
    dataset_limpio["TiempoVoluntariadoSD"] = dataset["P6_17A_1_3"] + (dataset["P6_17A_1_4"] / 60) + dataset["P6_17A_2_3"] + (dataset["P6_17A_2_4"] / 60)
    
    # Tiempo Actividades recreativas (Oseo, físicas, pasatiempos)
    # preguntas p6_18, p6_19_1, p6_19_2, p6_20, p6_21_1, p6_21_2, p6_21_3, p6_21_4, p6_22_1, p6_22_2, p6_22_3, p6_22_4, p6_22_5, p6_23_1
    # para la p6_18a_1, p6_18a_2, p6_18a_3, p6_18a_4, p6_19a_1_1, p6_19a_1_2, p6_19a_1_3, p6_19a_1_4, p6_19a_2_1, p6_19a_2_2, p6_19a_2_3, p6_19a_2_4, p6_20a_1, p6_20a_2, p6_20a_3, p6_20a_4, p6_21a_1_1, p6_21a_1_2, p6_21a_1_3, p6_21a_1_4, p6_21a_2_1, p6_21a_2_2, p6_21a_2_3, p6_21a_2_4, p6_21a_3_1, p6_21a_3_2, p6_21a_3_3, p6_21a_3_4, p6_21a_4_1, p6_21a_4_2, p6_21a_4_3, p6_21a_4_4, p6_22a_1_1, p6_22a_1_2, p6_22a_1_3, p6_22a_1_4, p6_22a_2_1, p6_22a_2_2, p6_22a_2_3, p6_22a_2_4, p6_22a_3_1, p6_22a_3_2, p6_22a_3_3, p6_22a_3_4, p6_22a_4_1, p6_22a_4_2, p6_22a_4_3, p6_22a_4_4, p6_22a_5_1, p6_22a_5_2, p6_22a_5_3, p6_22a_5_4, p6_23a_1_1, p6_23a_1_2, p6_23a_1_3, p6_23a_1_4
    dataset_limpio["TiempoActividadesRecreativasLV"] = dataset["P6_18A_1"] + dataset["P6_18A_2"] + dataset["P6_19A_1_1"] + (dataset["P6_19A_1_2"] / 60) + dataset["P6_19A_2_1"] + (dataset["P6_19A_2_2"] / 60) + dataset["P6_20A_1"] + dataset["P6_20A_2"] + dataset["P6_21A_1_1"] + (dataset["P6_21A_1_2"] / 60) + dataset["P6_21A_2_1"] + (dataset["P6_21A_2_2"] / 60) + dataset["P6_21A_3_1"] + (dataset["P6_21A_3_2"] / 60) + dataset["P6_21A_4_1"] + (dataset["P6_21A_4_2"] / 60) + dataset["P6_22A_1_1"] + (dataset["P6_22A_1_2"] / 60) + dataset["P6_22A_2_1"] + (dataset["P6_22A_2_2"] / 60) + dataset["P6_22A_3_1"] + (dataset["P6_22A_3_2"] / 60) + dataset["P6_22A_4_1"] + (dataset["P6_22A_4_2"] / 60) + dataset["P6_22A_5_1"] + (dataset["P6_22A_5_2"] / 60) + dataset["P6_23A_1_1"] + (dataset["P6_23A_1_2"] / 60)
    dataset_limpio["TiempoActividadesRecreativasSD"] = dataset["P6_18A_3"] + dataset["P6_18A_4"] + dataset["P6_19A_1_3"] + (dataset["P6_19A_1_4"] / 60) + dataset["P6_19A_2_3"] + (dataset["P6_19A_2_4"] / 60) + dataset["P6_20A_3"] + dataset["P6_20A_4"] + dataset["P6_21A_1_3"] + (dataset["P6_21A_1_4"] / 60) + dataset["P6_21A_2_3"] + (dataset["P6_21A_2_4"] / 60) + dataset["P6_21A_3_3"] + (dataset["P6_21A_3_4"] / 60) + dataset["P6_21A_4_3"] + (dataset["P6_21A_4_4"] / 60) + dataset["P6_22A_1_3"] + (dataset["P6_22A_1_4"] / 60) + dataset["P6_22A_2_3"] + (dataset["P6_22A_2_4"] / 60) + dataset["P6_22A_3_3"] + (dataset["P6_22A_3_4"] / 60) + dataset["P6_22A_4_3"] + (dataset["P6_22A_4_4"] / 60) + dataset["P6_22A_5_3"] + (dataset["P6_22A_5_4"] / 60) + dataset["P6_23A_1_3"] + (dataset["P6_23A_1_4"] / 60)
    
    # Atención a la salud
    # preguntas p6_23_2
    # para la p6_23a_2_1, p6_23a_2_2, p6_23a_2_3, p6_23a_2_4
    dataset_limpio["TiempoAtenciónSaludLV"] = dataset["P6_23A_2_1"] + (dataset["P6_23A_2_2"] / 60)
    dataset_limpio["TiempoAtenciónSaludSD"] = dataset["P6_23A_2_3"] + (dataset["P6_23A_2_4"] / 60)

    # Sentimiento Quehaceres del hogar
    # preguntas p7_1_1
    dataset_limpio["SentimientoQuehaceresHogar"] = dataset["P7_1_1"]
    catalogo_sentimiento_quehaceres_hogar = pd.read_csv(ruta_catalogo_sentimiento_quehaceres_hogar, encoding="latin1")
    dataset_limpio["SentimientoQuehaceresHogar"] = dataset_limpio["SentimientoQuehaceresHogar"].replace(catalogo_sentimiento_quehaceres_hogar.set_index("cve").to_dict()["descrip"])

    # Sentimiento actividades estudio
    # preguntas p7_1_2
    dataset_limpio["SentimientoEstudio"] = dataset["P7_1_2"]
    catalogo_sentimiento_estudio = pd.read_csv(ruta_catalogo_sentimiento_estudio, encoding="latin1")
    dataset_limpio["SentimientoEstudio"] = dataset_limpio["SentimientoEstudio"].replace(catalogo_sentimiento_estudio.set_index("cve").to_dict()["descrip"])

    # Sentimiento trabajo
    # preguntas p7_1_3
    dataset_limpio["SentimientoTrabajo"] = dataset["P7_1_3"]
    catalogo_sentimiento_trabajo = pd.read_csv(ruta_catalogo_sentimiento_trabajo, encoding="latin1")
    dataset_limpio["SentimientoTrabajo"] = dataset_limpio["SentimientoTrabajo"].replace(catalogo_sentimiento_trabajo.set_index("cve").to_dict()["descrip"])
     
    # Sentimiento cuidado y apoyo a familiares
    # preguntas p7_1_4
    dataset_limpio["SentimientoCuidadoApoyoFamiliares"] = dataset["P7_1_4"]
    catalogo_sentimiento_cuidado_apoyo_familiares = pd.read_csv(ruta_catalogo_sentimiento_cuidado_apoyo_familiares, encoding="latin1")
    dataset_limpio["SentimientoCuidadoApoyoFamiliares"] = dataset_limpio["SentimientoCuidadoApoyoFamiliares"].replace(catalogo_sentimiento_cuidado_apoyo_familiares.set_index("cve").to_dict()["descrip"])
     
    # Sentimiento actividades de oseo convivencia
    # preguntas p7_1_5
    dataset_limpio["SentimientoOcioConvivencia"] = dataset["P7_1_5"]
    catalogo_sentimiento_ocio_convivencia = pd.read_csv(ruta_catalogo_sentimiento_ocio_convivencia, encoding="latin1")
    dataset_limpio["SentimientoOcioConvivencia"] = dataset_limpio["SentimientoOcioConvivencia"].replace(catalogo_sentimiento_ocio_convivencia.set_index("cve").to_dict()["descrip"])
     
    # Sentimiento traslado
    # preguntas p7_1_6
    dataset_limpio["SentimientoTraslado"] = dataset["P7_1_6"]
    catalogo_sentimiento_traslado = pd.read_csv(ruta_catalogo_sentimiento_traslado, encoding="latin1")
    dataset_limpio["SentimientoTraslado"] = dataset_limpio["SentimientoTraslado"].replace(catalogo_sentimiento_traslado.set_index("cve").to_dict()["descrip"])
     
    # Sentimiento tramites y pagos
    # preguntas p7_1_7
    dataset_limpio["SentimientoTramitesPagos"] = dataset["P7_1_7"]
    catalogo_sentimiento_tramites_pagos = pd.read_csv(ruta_catalogo_sentimiento_tramites_pagos, encoding="latin1")
    dataset_limpio["SentimientoTramitesPagos"] = dataset_limpio["SentimientoTramitesPagos"].replace(catalogo_sentimiento_tramites_pagos.set_index("cve").to_dict()["descrip"])
     
    # Sentimiento vida general
    # preguntas p7_2_1
    dataset_limpio["SentimientoVidaGeneral"] = dataset["P7_2_1"]
    catalogo_sentimiento_vida_general = pd.read_csv(ruta_catalogo_sentimiento_vida_general, encoding="latin1")
    dataset_limpio["SentimientoVidaGeneral"] = dataset_limpio["SentimientoVidaGeneral"].replace(catalogo_sentimiento_vida_general.set_index("cve").to_dict()["descrip"])
     
    # Sentimiento vida familiar
    # preguntas p7_2_2
    dataset_limpio["SentimientoVidaFamiliar"] = dataset["P7_2_2"]
    catalogo_sentimiento_vida_familiar = pd.read_csv(ruta_catalogo_sentimiento_vida_familiar, encoding="latin1")
    dataset_limpio["SentimientoVidaFamiliar"] = dataset_limpio["SentimientoVidaFamiliar"].replace(catalogo_sentimiento_vida_familiar.set_index("cve").to_dict()["descrip"])
    
    # Sentimiento vida afectiva
    # preguntas p7_2_3
    dataset_limpio["SentimientoVidaAfectiva"] = dataset["P7_2_3"]
    catalogo_sentimiento_vida_afectiva = pd.read_csv(ruta_catalogo_sentimiento_vida_afectiva, encoding="latin1")
    dataset_limpio["SentimientoVidaAfectiva"] = dataset_limpio["SentimientoVidaAfectiva"].replace(catalogo_sentimiento_vida_afectiva.set_index("cve").to_dict()["descrip"])
     
    # Sentimiento vida social
    # preguntas p7_2_4
    dataset_limpio["SentimientoVidaSocial"] = dataset["P7_2_4"]
    catalogo_sentimiento_vida_social = pd.read_csv(ruta_catalogo_sentimiento_vida_social, encoding="latin1")
    dataset_limpio["SentimientoVidaSocial"] = dataset_limpio["SentimientoVidaSocial"].replace(catalogo_sentimiento_vida_social.set_index("cve").to_dict()["descrip"])
     
    # Sentimiento situación económica
    # preguntas p7_2_5
    dataset_limpio["SentimientoSituaciónEconómica"] = dataset["P7_2_5"]
    catalogo_sentimiento_situacion_economica = pd.read_csv(ruta_catalogo_sentimiento_situacion_economica, encoding="latin1")
    dataset_limpio["SentimientoSituaciónEconómica"] = dataset_limpio["SentimientoSituaciónEconómica"].replace(catalogo_sentimiento_situacion_economica.set_index("cve").to_dict()["descrip"])
     
    # Sentimiento con tu vivienda
    # preguntas p7_2_6
    dataset_limpio["SentimientoVivienda"] = dataset["P7_2_6"]
    catalogo_sentimiento_vivienda = pd.read_csv(ruta_catalogo_sentimiento_vivienda, encoding="latin1")
    dataset_limpio["SentimientoVivienda"] = dataset_limpio["SentimientoVivienda"].replace(catalogo_sentimiento_vivienda.set_index("cve").to_dict()["descrip"])
    
    # Sentimiento felicidad general
    # preguntas p7_3
    dataset_limpio["SentimientoFelicidadGeneral"] = dataset["P7_3"]
    catalogo_sentimiento_felicidad_general = pd.read_csv(ruta_catalogo_sentimiento_felicidad_general, encoding="latin1")
    dataset_limpio["SentimientoFelicidadGeneral"] = dataset_limpio["SentimientoFelicidadGeneral"].replace(catalogo_sentimiento_felicidad_general.set_index("cve").to_dict()["descrip"])

    
    
    # extraemos la cantidad de columnas
    cantidad_columnas = dataset_limpio.shape[1]
    cantidad_instancias = dataset_limpio.shape[0]
    ventana2 = mostrar_dataframe_en_qt(dataset_limpio, "Nuevo diccionario " + str(cantidad_columnas) + " columnas y " + str(cantidad_instancias) + " instancias")
    
    # vamos a quitar todos los acentos y caracteres especiales
    
    
    # Guardar el nuevo dataset
    dataset_limpio.to_csv("nuevo_dataset.csv", index=False, encoding="latin1")
    
    # Ejecutar la aplicación
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
