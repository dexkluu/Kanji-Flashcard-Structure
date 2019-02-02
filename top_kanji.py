# -*- coding: utf-8 -*-
"""
This code will take the kanji list
"""

from bs4 import BeautifulSoup
import requests
import re

def read_ex(reading,kun_or_on,soup):
    '''reading is the list of kun or on readings.
    soup is the BeautifulSoup object of the webpage for the character.
    kun_or_on is 1 for kun and 0 for on if they both exist. If only one exists,
    then it is 0.'''
    dict_defn = {}
    count=0
    for j in reading:
        count=count+1
        if (j[0] != '-') & (j[-1] != '-'):
            lst_ex = re.findall('【(.*)】', soup.find_all('ul', class_='no-bullet')[kun_or_on].get_text())
            for k in lst_ex:
                if j in k:
                    start_ex = '\n  【' + k + '】\n  '
                    end_ex = '\n\n'
                    ex = start_ex + '(.*)' + end_ex
                    defn = re.findall(ex, soup.find_all('ul', class_='no-bullet')[kun_or_on].get_text())[0]
                    ex2 = '\n\n  '+'(.*)'+start_ex
                    read = re.findall(ex2, soup.find_all('ul', class_='no-bullet')[kun_or_on].get_text())[0]
                    dict_defn[reading[count-1]] = read+' '+defn
                    break
    return dict_defn

file = open(r"kanji_by_frequency.txt",encoding='utf8',mode='r').read()
kanji_by_freq = file.split('\n')
list_couple = [list(x.split(': ')) for x in kanji_by_freq]
list_couple.pop(2501) # The last element is an empty string so pop it
# Convert the number kanji pair to tuples in a list. The number means usage rank in newspapers
tuple_couple = [(int(y[0]),y[1]) for y in list_couple]
kanji_freq = dict(tuple_couple) # Create a dictionary from the tuple pairs
final_dict = {}
# Scrape the information off of jisho.org
for i in range(1,len(kanji_freq)+1):
    result = requests.get('https://jisho.org/search/' + kanji_freq[i] + '%23kanji')
    c = result.content
    soup = BeautifulSoup(c)
    # Defines the main meaning of the kanji
    main_meaning = soup.find('div',class_="kanji-details__main-meanings").get_text()[7:-5]
    if len(soup.find_all('dd', class_="kanji-details__main-readings-list")) == 2:
        # Splits readings and defines as a list
        kun_reading = soup.find_all('dd', class_="kanji-details__main-readings-list")[0].get_text()[1:-1].split('、 ')
        on_reading = soup.find_all('dd', class_="kanji-details__main-readings-list")[1].get_text()[1:-1].split('、 ')
        if len(soup.find_all('ul', class_='no-bullet'))==2:
            kun_reading_ex = read_ex(kun_reading,1,soup)
            on_reading_ex = read_ex(on_reading,0,soup)
        elif len(soup.find_all('ul', class_='no-bullet'))==1:
            if soup.find_all('h2')[0:2] == 'On':
                on_reading_ex = read_ex(on_reading,0,soup)
                kun_reading_ex = []
            else:
                kun_reading_ex = read_ex(kun_reading,0,soup)
                on_reading_ex=[]
        else:
            kun_reading_ex = []
            on_reading_ex = []
    elif soup.find_all('dt')[2].get_text()=='Kun:':
        kun_reading = soup.find_all('dd', class_="kanji-details__main-readings-list")[0].get_text()[1:-1].split('、 ')
        if len(soup.find_all('ul', class_='no-bullet'))==1:
            kun_reading_ex = read_ex(kun_reading,0,soup)
            on_reading_ex=[]
        else:
            kun_reading_ex = []
            on_reading_ex = []
    elif soup.find_all('dt')[2].get_text()=='On:':
        on_reading = soup.find_all('dd', class_="kanji-details__main-readings-list")[0].get_text()[1:-1].split('、 ')
        if len(soup.find_all('ul', class_='no-bullet'))==1:
            on_reading_ex = read_ex(on_reading,0,soup)
            kun_reading_ex = []
        else:
            kun_reading_ex = []
            on_reading_ex = []
    final_dict[i] =[main_meaning,kun_reading,kun_reading_ex,on_reading,on_reading_ex]
# The final dictionary was saved as a pickle object
kanji_info = final_dict
