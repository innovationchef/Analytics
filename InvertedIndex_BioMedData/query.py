from nltk.corpus import stopwords
import string
from autocorrect import spell
import nltk
def remove_stopwords(data):
	
	k=0
	mylist = list()
	for sentence in data:
		sentence = data[k]
		for c in string.punctuation:
			sentence= sentence.replace(c,"")
		k = k+1
		item = [i for i in sentence.split() if i not in stop]
		# ' '.join(reduce(lambda a, b: a + b, item))
		print item
		mylist.append(item)

	return mylist

def writeout(text,filename,header=["ID"]):
    # save out to .csv
    f = open(filename,'w')
    csvf=csv.writer(f)
    csvf.writerow(header)
    csvf.writerows(zip(text))
    f.close()

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


data = "cancer is a bad disease"
all_words = useful_words(data)



