# -*- coding: utf-8 -*-
"""
Editor de Spyder

Autor: Victor Alzorriz Pedrero
"""

import requests
import pandas as pd
from lxml import html
from textblob import TextBlob

title_page = 'https://www.tripadvisor.com'
base_page = 'https://www.tripadvisor.com/Hotel_Review-g60763-d10330604-Reviews{0}-Four_Seasons_Hotel_New_York_Downtown-New_York_City_New_York.html'
num_pages = 2

coments = []
polarities = []
subjectivities = []

for index_1 in range(0,num_pages):
    print('Empezando a parsear la pagina ' + str(index_1 + 1))
    
    if index_1 == 0:
        format_text = ''
    else:
        format_text = '-or' + str(index_1*5)
    
    url_page = base_page.format(format_text)
    code_page = requests.get(url_page)
    
    tree_page = html.fromstring(code_page.content)
    base_coments = tree_page.xpath('//a[@class="location-review-review-list-parts-ReviewTitle__reviewTitleText--2tFRT"]/@href')
    
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

df = pd.DataFrame(polarities, columns={'Polarities'})
df['Subjectivities'] = subjectivities
df['Coments'] = coments
df.to_csv("./coments.csv", sep=',', encoding='utf-8', header=True, index=False)