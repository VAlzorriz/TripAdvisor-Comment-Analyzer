# -*- coding: utf-8 -*-
"""
Editor de Spyder

Autor: Victor Alzorriz Pedrero
"""

import requests
import pandas as pd
from lxml import html
from textblob import TextBlob

"""
Introducimos la URL del hotel de Tripadvisor que queremos y el numero de paginas de comentarios que queremos procesar.
"""
title_page = 'https://www.tripadvisor.com'
base_page = 'https://www.tripadvisor.com/Hotel_Review-g60763-d10330604-Reviews{0}-Four_Seasons_Hotel_New_York_Downtown-New_York_City_New_York.html'
num_pages = 50

"""
Inicializamos 3 listas para guardar el texto, la polaridad y la subjetividad de cada comentario.
"""
coments = []
polarities = []
subjectivities = []

"""
Recorremos todas las paginas de comentarios para recuperar el HTML de cada una.
"""
for index_1 in range(0,num_pages):
    
    """
    -La pagina 0 es diferente a todas las demas ya que no tiene la estructura de paginacion en la URL que es "-or(numero de comentarios)", por
    eso con el "if else" hacemos que si es la primera pagina no cambie la URL de la pagina a recuperar, pero si es cualquiera otra pagina añade a
    la URL el numero de pagina multiplicado por 5 ya que es el numero de comentarios que aparecen por pagina, pero como el comentario aparece
    dividido en vez de recuperar los comentarios recuperamos la URL de cada comentario.
    """
    print('Empezando a parsear la pagina ' + str(index_1 + 1))
    
    if index_1 == 0:
        format_text = ''
    else:
        format_text = '-or' + str(index_1*5)
    
    url_page = base_page.format(format_text)
    code_page = requests.get(url_page)
    
    tree_page = html.fromstring(code_page.content)
    base_coments = tree_page.xpath('//a[@class="location-review-review-list-parts-ReviewTitle__reviewTitleText--2tFRT"]/@href')
    
    """
    -Recorremos todas las URL de los comentarios y descargamos cada pagina para extraer el comentario de cada una y hacer el analisis de sentimientos.
    -Tambien destacar los comentarios mas largos no aparecen enteros y hay que pulsar un boton para leer mas, a causa de esto la etiqueta que contiene
    el texto cambia y en vez de ser "fullText" es "fullText hidden". Por eso si al buscar la primera etiqueta no devuelve nada, porque no al ha 
    encontrado, buscata la segunda.
    -Tambien destacar que algunos comentarios estan divididos en parrafos, por lo que para que sea mas facil manupular utilizamos un bucle for para
    unir todos los parrafos en un solo string.
    -Tambien destacar que eliminamos el caracter ";" de los comentarios por que si no luego en el CSV lo detecta como cambio de celda.
    """
    for index_2 in range(0, len(base_coments)):
        print('Parsenado comentario ' + str(index_2 + 1) + ' de la pagina ' + str(index_1 + 1))
        
        url_coments = str(title_page) + str(base_coments[index_2])
        code_coments = requests.get(url_coments)
        
        tree_coments = html.fromstring(code_coments.content)
        
        text_coments = tree_coments.xpath('//span[@class="fullText "]/text()')
        
        if not text_coments:
            text_coments = tree_coments.xpath('//span[@class="fullText hidden"]/text()')
            
        full_coment = ''
        
        for index_3 in range(0, len(text_coments)):
            full_coment = full_coment + str(text_coments[index_3].replace(";", ""))
        
        print('Analizando comentario ' + str(index_2 + 1) + ' de la pagina ' + str(index_1 + 1))
        
        testimonial = TextBlob(full_coment)
            
        polarity = testimonial.sentiment.polarity
        subjectivity = testimonial.sentiment.subjectivity
            
        coments.append(full_coment)
        polarities.append(polarity)
        subjectivities.append(subjectivity)

"""
Creamos un Data Frame de la libreria Pandas al que añadimos las 3 listas con los comentarios, la polaridad y la subjetividad para volcarlo 
a un fichero .csv.
"""
df = pd.DataFrame(polarities, columns={'Polarities'})
df['Subjectivities'] = subjectivities
df['Coments'] = coments
df.to_csv("./coments.csv", sep=',', encoding='utf-8', header=True, index=False)