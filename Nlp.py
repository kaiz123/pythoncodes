
import nltk
# nltk.download()
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer
import nltk.data
import io


tokenizer = RegexpTokenizer(r'\w+')
tokenizer1 = nltk.data.load('tokenizers/punkt/english.pickle')



fp = io.open("txt1.txt",encoding='utf-8-sig')
fp1 = io.open("txt2.txt",encoding='utf-8-sig')
data = fp.read()
data1 = fp1.read()
stop_words = set(stopwords.words('english'))
#tokenizing into list of words
word_tokens=tokenizer.tokenize(data)
word_tokens1=tokenizer.tokenize(data1)
#tokenizing into list of sentences
sentence=tokenizer1.tokenize(data)
sentence1=tokenizer1.tokenize(data1)


l=[]
l1=[]
new=[]
final=[]
final1=[]
word_counter = {}
#Eliminate stopwords
for w in word_tokens:
    if w not in stop_words:
        l.append(w)


for w in word_tokens1:
    if w not in stop_words:
        l1.append(w) 
#get similar words and sort them in new array
for word in l:
	for word1 in l1:
		if word.lower()==word1.lower():
			new.append(word.lower())
			
		
#get frequency of similar words and sort them in that order in rank array
for word in new:

 	if word in word_counter:
 		word_counter[word] += 1
 	else:
 		word_counter[word] = 1
        
rank = sorted(word_counter, key = word_counter.get, reverse = True)
print("Similar words:")
for word in rank:
	print word
#get all sentences from both files that contain similar words in the order of frequency of words and store
for item in sentence:
	item1=item.lower()

	

	for word in rank:
		if word in item1:
			final.append(item)
			break

for item in sentence1:
	item1=item.lower()
	for word in rank:
		if word in item1:
			final1.append(item)
			break			
print("txt1:")
for sent in final:
	print (sent)
print("txt2:")	
for sent in final1:
	print (sent)




