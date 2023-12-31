# -*- coding: utf-8 -*-
"""Untitled8.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xakjWeSIWE_qdLdsdv2kTdqpR0Kg1OqB

Creamos gráfico dónde se ordenen por likes
"""

import plotly.express as px

# Datos
participantes = ["Pamela Diaz", "Junior Playboy", "El futuro fuera de orbita", "La guaren", "Luis Mateucci",
                 "Eva Gomez", "Simon de la Costa", "Fran Maira", "Scarleth", "Alessia"]
reality = ["TB", "TB", "TB", "TB", "TB", "TB", "TB", "GH", "GH", "GH"]
likes = [33200, 28200, 21700, 17900, 16200, 15300, 13600, 8144, 6148, 5516]
comentarios = [2448, 2409, 1768, 1091, 978, 528, 1768, 1091, 621, 235]

# Crear DataFrame
import pandas as pd
df = pd.DataFrame({'Participante': participantes, 'Reality': reality, 'Likes': likes, 'Comentarios': comentarios})

# Ordenar por likes
df = df.sort_values(by='Likes', ascending=False)

# Crear gráfico de burbujas con colores distintos para GH y TB
fig = px.scatter(df, x='Likes', y='Comentarios', size='Likes', color='Reality',
                 hover_name='Participante', template='plotly_white', color_discrete_map={'GH': 'fuchsia', 'TB': 'lightgreen'},
                 title='Top 10 participantes con más likes en sus presentaciones')
# Cambiar el tamaño, la fuente y centrar el título
fig.update_layout(
    title_text='Top 10: participantes con presentaciones más populares en RRSS',
    title_font=dict(size=48, color='Pink', family='Times New Roman'),
    title_x=0.5  # Centro horizontalmente el título
)


# Añadir etiquetas personalizadas arriba de las burbujas
for i, row in df.iterrows():
    fig.add_annotation(
        x=row['Likes'],
        y=row['Comentarios'] + 200,  # Ajustar la posición vertical de las etiquetas
        text=row['Participante'],
        showarrow=False,
        font=dict(size=10),
    )

# Anotación para la sección de detalle
fig.add_annotation(
    x=0.5,
    y=-0.23,
    xref='paper',
    yref='paper',
    text='<b>El tamaño de las burbujas refleja la cantidad de likes y mientras más a la derecha esté más comentarios tiene</b>',
    showarrow=False,
    font=dict(size=13),
)

# Mostrar el gráfico
fig.show()