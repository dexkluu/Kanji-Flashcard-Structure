# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 23:20:18 2018

@author: dluu1
"""
import pickle

kanji_info = pickle.load( open( "kanji_info_dict.pkl", "rb" ))
file = open(r"kanji_by_frequency.txt",encoding='utf8',mode='r').read()
kanji_by_freq = file.split('\n')
list_couple = [list(x.split(': ')) for x in kanji_by_freq]
list_couple.pop(2501)
tuple_couple = [(int(y[0]),y[1]) for y in list_couple]
kanji_freq = dict(tuple_couple)

for i in range(1,76):#First 75 flashcards (change the range to get that interval of cards)
    if i!=1:
        print('|')
    print(kanji_freq[i]+'~'+str(i)+'. '+kanji_info[i][0])
    print('Kun readings: '+str(kanji_info[i][1]))
    for j in kanji_info[i][2]:
        print(j+':  '+kanji_info[i][2][j])
    print('On readings: '+str(kanji_info[i][3]))
    for k in kanji_info[i][4]:
        print(k+':  '+kanji_info[i][4][k])
        
