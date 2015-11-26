from __future__ import division
import os,sys
import nltk
import math
import operator
import sys  
from io import open
from nltk import word_tokenize
reload(sys)  
sys.setdefaultencoding('utf8')

outputFile = open("IDF.txt", "wb") 

outputFile1 = open("stop_words_IDF.txt", "wb") 

closed_class_stop_words = ['a','the','an','and','or','but','about','above','after','along','amid','among',\
                           'as','at','by','for','from','in','into','like','minus','near','of','off','on',\
                           'onto','out','over','past','per','plus','since','till','to','under','until','up',\
                           'via','vs','with','that','can','cannot','could','may','might','must',\
                           'need','ought','shall','should','will','would','have','had','has','having','be',\
                           'is','am','are','was','were','being','been','get','gets','got','gotten',\
                           'getting','seem','seeming','seems','seemed',\
                           'enough', 'both', 'all', 'your' 'those', 'this', 'these', \
                           'their', 'the', 'that', 'some', 'our', 'no', 'neither', 'my',\
                           'its', 'his' 'her', 'every', 'either', 'each', 'any', 'another',\
                           'an', 'a', 'just', 'mere', 'such', 'merely' 'right', 'no', 'not',\
                           'only', 'sheer', 'even', 'especially', 'namely', 'as', 'more',\
                           'most', 'less' 'least', 'so', 'enough', 'too', 'pretty', 'quite',\
                           'rather', 'somewhat', 'sufficiently' 'same', 'different', 'such',\
                           'when', 'why', 'where', 'how', 'what', 'who', 'whom', 'which',\
                           'whether', 'why', 'whose', 'if', 'anybody', 'anyone', 'anyplace', \
                           'anything', 'anytime' 'anywhere', 'everybody', 'everyday',\
                           'everyone', 'everyplace', 'everything' 'everywhere', 'whatever',\
                           'whenever', 'whereever', 'whichever', 'whoever', 'whomever' 'he',\
                           'him', 'his', 'her', 'she', 'it', 'they', 'them', 'its', 'their','theirs',\
                           'you','your','yours','me','my','mine','I','we','us','much','and/or'
                           ]


word_to_docFreq_map = {} 
word_to_idf_map = {}
word_to_no_stop_word_idf_map = {} 
#change the path to the directory that contains all the files and python program	
path = "/home/yh1008/NLP/hw5/unzip/all-OANC-dir/" 

dir = os.listdir(path)
num_of_files = 0 #store the total number of documents in all-OANC-dir directory
list = [] #store all distinct token within a file 

#print (os.getcwd())
#print ("**********************************************whole directory: " )
#print dir
tokens =[]
for root, dirs, files in os.walk(path, topdown=False):
	for name in files:
		if name == 'IDF.py' or name == 'IDF.txt' or name == 'stop_words_IDF.txt':
			continue
		num_of_files = num_of_files + 1 
		name = name.encode('utf-8')
		
		
		#with open(name) as f:
		#	file_content = f.read()
                name = unicode(name, errors='ignore')
		name.decode('utf-8')
		
		file1 = open(path+'/'+name, encoding='utf-8' )
		file_content = file1.read()
		tokens = word_tokenize(file_content)
		unique_words_in_file = {}
		for token in tokens:
			if token not in unique_words_in_file:
				unique_words_in_file[token] = 0 #only the key that matters, value doesn't, so we just assign it to zero
	
		for unique_word_in_file in unique_words_in_file.keys(): #loop through all the tokens in the file
			if unique_word_in_file not in word_to_docFreq_map:
				word_to_docFreq_map[unique_word_in_file] = 1
			else:
				word_to_docFreq_map[unique_word_in_file] += 1
			
for word in word_to_docFreq_map:
	if word_to_docFreq_map[word] > 1:
		word_to_idf_map[word] = math.log(num_of_files/word_to_docFreq_map[word])
	else:
		pass



sorted_word_to_idf_map = sorted(word_to_idf_map.items(), key=operator.itemgetter(1))
sorted_word_to_idf_map.reverse()

#print (sorted_word_to_idf_map)

for i in range(len(sorted_word_to_idf_map)):
	outputFile.write (str(sorted_word_to_idf_map[i][0]) + "\n")

outputFile.close()

for word in word_to_docFreq_map:
	if word not in closed_class_stop_words:

		if word_to_docFreq_map[word] > 1:
			word_to_no_stop_word_idf_map[word] = math.log(num_of_files/word_to_docFreq_map[word])
		else:
			pass
	


sorted_word_to_no_stop_word_idf_map = sorted(word_to_no_stop_word_idf_map.items(), key=operator.itemgetter(1))
sorted_word_to_no_stop_word_idf_map.reverse()

for i in range(len(sorted_word_to_no_stop_word_idf_map)):
	outputFile1.write (str(sorted_word_to_no_stop_word_idf_map[i][0]) + "\n")

outputFile1.close() 
