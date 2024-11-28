import pandas as pd
import altair as alt
import numpy as np
import os

# Leemos el archivo CSV
df = pd.read_csv("../muestraFinal.csv")


# Calcular estadísticas numéricas
def estadisticas_numericas(df):
    columnas_numericas = df.select_dtypes(include=[np.number])
    resultado = []
    for columna in columnas_numericas.columns:
        media = columnas_numericas[columna].mean()
        mediana = columnas_numericas[columna].median()
        minimo = columnas_numericas[columna].min()
        maximo = columnas_numericas[columna].max()
        desviacion_estandar = columnas_numericas[columna].std()
        resultado.append({
            'Columna': columna,
            'Media': media,
            'Mediana': mediana,
            'Mínimo': minimo,
            'Máximo': maximo,
            'Desviación Estándar': desviacion_estandar
        })
    return pd.DataFrame(resultado)

# Calcular estadísticas categóricas
def estadisticas_categoricas(df):
    columnas_categoricas = df.select_dtypes(include=['object', 'category'])
    resultado = []
    for columna in columnas_categoricas.columns:
        conteo = columnas_categoricas[columna].value_counts()
        moda = columnas_categoricas[columna].mode()
        resultado.append({
            'Columna': columna,
            'Conteo': conteo.to_dict(),
            'Moda': moda.iloc[0] if not moda.empty else None
        })
    return resultado

# Calcular estadísticas
estadisticas_cat = estadisticas_categoricas(df)

# Crear directorio para guardar gráficos
directorio_salida = "./html"
os.makedirs(directorio_salida, exist_ok=True)

# Crear gráficos interactivos de estadísticas categóricas con tablas adicionales
for est in estadisticas_cat:
    columna = est['Columna']
    conteo = pd.DataFrame(list(est['Conteo'].items()), columns=['Categoría', 'Frecuencia'])

    # Gráfico de barras con tooltip
    bar_chart = alt.Chart(conteo).mark_bar().encode(
        x=alt.X('Categoría', title='Categoría'),
        y=alt.Y('Frecuencia', title='Frecuencia'),
        tooltip=[alt.Tooltip('Categoría', title='Categoría'),
                 alt.Tooltip('Frecuencia', title='Frecuencia')]
    ).properties(
        width=300,
        title=f'Estadísticas de la columna {columna}'
    )

    # Tabla con los mismos datos
    table = alt.Chart(conteo).mark_text().encode(
        y=alt.Y('Categoría:N', title=None, axis=alt.Axis(labels=True)),
        text=alt.Text('Frecuencia:Q'),
        tooltip=[alt.Tooltip('Categoría', title='Categoría'),
                 alt.Tooltip('Frecuencia', title='Frecuencia')]
    ).properties(
        width=200,
        title="Tabla de Frecuencias"
    )

    # Nueva tabla con estadísticas resumidas
    resumen_data = pd.DataFrame({
        'Estadística': ['Moda'],
        'Valor': [est['Moda']]
    })

    

    # Combinar gráfico de barras, tabla de frecuencias y tabla de estadísticas
    combined = alt.hconcat(bar_chart, table).resolve_scale(
        y='shared'
    )

    ruta_guardado = f'{directorio_salida}/estadisticas_categoricas_{columna}.html'
    combined.save(ruta_guardado)
    print(f"Gráfico interactivo con tablas guardado en: {ruta_guardado}")


estadisticas_num_df = estadisticas_numericas(df)

# Crear gráficos interactivos de estadísticas numéricas con tabla 
for _, row in estadisticas_num_df.iterrows():
    columna = row['Columna']
    data = pd.DataFrame({
        'Estadística': ['Media', 'Mediana', 'Mínimo', 'Máximo', 'Desviación Estándar'],
        'Valor': [row['Media'], row['Mediana'], row['Mínimo'], row['Máximo'], row['Desviación Estándar']]
    })

    # Gráfico de barras con tooltip
    bar_chart = alt.Chart(data).mark_bar().encode(
        x=alt.X('Estadística', title='Estadística'),
        y=alt.Y('Valor', title='Valor'),
        tooltip=[alt.Tooltip('Estadística', title='Estadística'),
                 alt.Tooltip('Valor', title='Valor', format='.2f')]
    ).properties(
        width=400,
        title=f'Estadísticas de la columna {columna}'
    )

    # Tabla con los mismos datos
    table = alt.Chart(data).mark_text().encode(
        y=alt.Y('Estadística:N', title=None, axis=alt.Axis(labels=True)),
        text=alt.Text('Valor:Q', format='.2f'),
        tooltip=[alt.Tooltip('Estadística', title='Estadística'),
                 alt.Tooltip('Valor', title='Valor', format='.2f')]
    ).properties(
        width=200,
        title="Tabla de Valores"
    )
    
    boxplot = alt.Chart(df).mark_boxplot().encode(
        y=alt.Y(columna, title=columna)
    ).properties(
        title=f'Box plot {columna}'
    )

    # Combinar gráfico de barras y tabla lado a lado
    combined = alt.hconcat(bar_chart, table, boxplot).resolve_scale(
        y='shared'
    )
    ruta_guardado = f'{directorio_salida}/estadisticas_numericas_{columna}.html'
    combined.save(ruta_guardado)
    print(f"Gráfico interactivo con tabla guardado en: {ruta_guardado}")