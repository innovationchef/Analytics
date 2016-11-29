import nltk
from nltk.corpus import stopwords
import numpy as np
import csv
import string
import pandas as pd
import re 
import sys
from autocorrect import spell
def open_file(filename):
  f = open(filename, 'r')
  x = f.readlines()
  return x

def remove_stopwords(data):
    item = re.sub('[^A-Za-z0-9]+', ' ', data)
    return item

def spell_correct(array):
    for k in array:
        if k.isupper():
            print k
            continue
            # lmtzr.WordNetLemmatizer
        print spell(k)

def useful_words(data):
    correct = list()
    for word in data.split():
        correct.append(spell(word))
    data = ' '.join(word for word in correct)
    is_noun = lambda pos: pos[:2] == 'NN'
    is_adj = lambda pos: pos[:2] == 'JJ'
    is_vb = lambda pos: pos[:2] == 'VB'
    tokenized = nltk.word_tokenize(data)
    nouns = [word for (word, pos) in nltk.pos_tag(tokenized) if is_noun(pos)] 
    adj = [word for (word, pos) in nltk.pos_tag(tokenized) if is_adj(pos)] 
    vb = [word for (word, pos) in nltk.pos_tag(tokenized) if is_vb(pos)] 
    all_words = nouns + adj + vb
    stop = set(stopwords.words('english'))
    for word in all_words:
        if word in stop:
            all_words.remove(word)

    return all_words

def save_file_text(n):
    filetext = {}
    array = np.empty(n)
    for number in range(n):
        array[number] = number
        name = str(int(array[number]))+".txt"
        filetext[name] = str(open_file(name)[0])
    return filetext

def find_word_freq(filetext):
    wordfreq = {}
    for key, values in filetext.items():    
        words = remove_stopwords(values).lower()
        for raw_word in words.split():
            if raw_word not in wordfreq:
                wordfreq[raw_word] = 0 
            wordfreq[raw_word] = wordfreq[raw_word] + 1
    return wordfreq

def find_inverted_index(filetext, wordfreq):
    inverted_index = {}
    for key, value in wordfreq.items():
        for name, text in filetext.items():
            words = remove_stopwords(text).lower()
            # print key, words
            if key in words:
                try:
                    inverted_index[key].append(name)
                except KeyError:
                    inverted_index[key] = [name]
                continue 
    return inverted_index

def docwise_freq(filetext):
    wordfreq = {}
    i=0
    for key, values in filetext.items():    
        words = remove_stopwords(values).lower()
        for raw_word in words.split():
            if (i,raw_word) not in wordfreq:
                wordfreq[(i,raw_word)] = 0 
            wordfreq[(i,raw_word)] = wordfreq[(i,raw_word)] + 1
        i=i+1
    return wordfreq

def get_all_files(inverted_index, keywords):
    files = {}
    for value in keywords: 
        if value in inverted_index.keys():
            files[value] = inverted_index.get(value)
    return files

def find_intersection_files(all_files):
    intersection_files = list()
    for key, value in all_files.items():
        intersection_files.append(value)
    return set(intersection_files[0]).intersection(*intersection_files)

def removetxt(files):
    intersection_files_names = list()
    for name in intersection_files:
        for char in ".txt":
            name = name.replace(char,"")
        intersection_files_names.append(int(name))
    return intersection_files_names

p = int(sys.argv[1])
filetext = save_file_text(p)
wordfreq = find_word_freq(filetext)
# docwise_wordfreq = docwise_freq(filetext)
inverted_index = find_inverted_index(filetext, wordfreq)

data = raw_input('Enter Query ------ ')
keywords = useful_words(data.lower())
all_files = get_all_files(inverted_index, keywords)
intersection_files = list(find_intersection_files(all_files))

#Here I have important keywords from query question and the relevant documents
print intersection_files
# print removetxt(intersection_files)
# print keywords
data1 = raw_input('Type name of the file you want to see ------ ')
print open_file(data1)






################################################################
# table = np.zeros(shape=(len(keywords),len(intersection_files_names)))
# for word in keywords:
#     for file in intersection_files_names:
#         try:
#             print docwise_wordfreq[(file, word)], word, file 
#         except KeyError:
#             continue

# TAbular Printing
# table = np.array([[1, 2, 1, 1, 2, 1, 1],
                 # [0, 1, 0, 0, 1, 0, 3]])
# row_format ="{:>15}" * (len(intersection_files) + 1)
# print row_format.format("", *intersection_files)
# for team, row in zip(keywords, table):
#     print row_format.format(team, *row)
################################################################

