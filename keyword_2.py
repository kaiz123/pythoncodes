from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import nltk
from nltk.corpus import stopwords

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer
import nltk.data
import io
import numpy as np
from bs4 import BeautifulSoup
import re
import lxml.etree as ET
from os import listdir
from os.path import isfile, join
# mypath=r'C:\Users\user\Downloads\XML_2000-2016\XML\2000'
# onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
# print(onlyfiles)

filedata=[]
year=1999
for count in range(1):
	year=year+1
	mypath=r'C:\Users\user\Downloads\XML_2000-2016\XML\\'+str(year)
	onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
	# print onlyfiles

	for i in range(len(onlyfiles)):
		
		infile = open(r'C:\Users\user\Downloads\XML_2000-2016\XML\\'+str(year)+"\\"+onlyfiles[i],'r')
		# print(soup.prettify())
		contents = infile.read()
		print(i)
		try:
			doc = ET.fromstring(contents)
		

		except:
			continue	

		data = doc.find('JUDGMENT_TEXT')

		# soup = BeautifulSoup(contents,'lxml')
		# data = soup.find_all('JUDGMENT_TEXT')
		# print(data.text)
		# print(type(data.text))
		filedata.append(data.text)

min_df=int(0.05*(len(filedata)))
print(min_df)


tokenizer = RegexpTokenizer(r'\w+')
tokenizer1 = nltk.data.load('tokenizers/punkt/english.pickle')

stop_words = set(stopwords.words('english'))
l=[]
l1=[]
new=[]
final=[]
final1=[]
word_counter = {}






def createDTM(messages):
	vect = TfidfVectorizer(min_df=min_df,stop_words=stop_words).fit(messages)
	# dtm = vect.fit_transform(messages)
	# print(vect.get_feature_names())
	vectorized=vect.transform(messages)
	indices = np.argsort(vect.idf_)[::-1]
	features = vect.get_feature_names()
	# for index,item in enumerate(features):
	# 	stritem=str(item)
	# 	stritem=re.sub(r'\b\w{1,3}\b', '', stritem)
	# 	stritem=re.sub('\d*', '', stritem)
	# 	features[index]=stritem
	# features=features.remove('')	
	# for index,item in enumerate(features):
	# 	if item is "":
	# 		features=np.delete(features,index)

	feature_names=np.array(features)
	print(len(feature_names))
	sorted=vectorized.max(0).toarray()[0].argsort()
	largest_score=feature_names[sorted[:-101:-1]]


	for index,item in enumerate(largest_score):
		stritem=str(item)
		# print(type(stritem))

		stritem=re.sub(r'\b\w{1,3}\b','', stritem)
		stritem=re.sub('\d*','', stritem)
		largest_score[index]=stritem
	


		# largest_score=np.array(set(largest_score))
	# largest_score=list(largest_score)
	# largest_score=largest_score.remove("") 	
	# for item in largest_score:
	# 	print(item)

	new=(list(largest_score))
	# for index,item in enumerate(new):
	# 	stritem=str(item)
	# 	if(len(stritem)) is 0:
	new=filter(None,new)
			
	# print(new)

	# for index,item in enumerate(largest_score):
	# 	stritem=str(item)
	# 	if stritem is "":
	# 		largest_score=np.delete(largest_score,index)




	# print(len(features))

	top_n = 1000
	# print [features[x] for x in indices[:top_n]]
	# top_features = [features[x] for x in indices[:top_n]]
	# print(top_features)
	# dtm_array=dtm.toarray()
	# for index,element in enumerate(dtm_array):
	# 	if element is 0:
	# 		np.delete(dtm_array,index)


	# print(dtm_array)





	# return pd.DataFrame(dtm.toarray(), columns=vect.get_feature_names()) 
	# return top_features
	return largest_score




# document1 ="""Python is a 2000 made-for-TV horror movie directed by Richard
# Clabaugh. The film features several cult favorite actors, including William
# Zabka of The Karate Kid fame, Wil Wheaton, Casper Van Dien, Jenny McCarthy,
# Keith Coogan, Robert Englund (best known for his role as Freddy Krueger in the
# A Nightmare on Elm Street series of films), Dana Barron, David Bowe, and Sean
# Whalen. The film concerns a genetically engineered snake, a python, that
# escapes and unleashes itself on a small town. It includes the classic final
# girl scenario evident in films like Friday the 13th. It was filmed in Los Angeles,
#  California and Malibu, California. Python was followed by two sequels: Python
#  II (2002) and Boa vs. Python (2004), both also made-for-TV films."""

# document2 ="""Python, from the Greek word , is a genus of
# nonvenomous pythons[2] found in Africa and Asia. Currently, 7 species are
# recognised.[2] A member of this genus, P. reticulatus, is among the longest
# snakes known."""  




# document1 ="""This is food.The respondent is crazy.The petitioner is amazing"""

document2 ="""This is a drink.The petitioner and respondent are nice."""  
# print(type(document1))


document1="This is food.The petitioner and respondent are crazy."


word_tokens=tokenizer.tokenize(document1)
word_tokens1=tokenizer.tokenize(document2)

word_tokens = [token.lower() for token in word_tokens]
word_tokens1 = [token.lower() for token in word_tokens1]


# print(word_tokens)


for w in word_tokens:
    if w not in stop_words:
        l.append(w)


for w in word_tokens1:
    if w not in stop_words:
        l1.append(w)  
# print(l)
# for word in document1:
# 	if word in stop_words:
# 		document1=document1.replace(word,"")

# for word in document2:
# 	if word in stop_words:
# 		document2=document2.replace(word,"")

# print(document2)


str1 = ' '.join(l)
str2 = ' '.join(l1)

# messages=filedata
messages=filedata
largest_score=createDTM(messages)
print(largest_score)
# print(ans)
# count=0
# year=1999
# sum=0
# for count in range(1):
# 	year=year+1
# 	mypath=r'C:\Users\user\Downloads\XML_2000-2016\XML\\'+str(year)
# 	onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
# 	# print onlyfiles

# 	for i in range(20):
# 		count=count+1
# 		print(str(count)+"\n")
# 		infile = open(r'C:\Users\user\Downloads\XML_2000-2016\XML\\'+str(year)+"\\"+onlyfiles[i],'r')
# 		# print(soup.prettify())
# 		print(str(year)+"\\"+onlyfiles[i])
# 		contents = infile.read()
# 		word_tokens=tokenizer.tokenize(contents)
# 		word_tokens = [token.lower() for token in word_tokens]
# 		for word in largest_score:
# 			if word in word_tokens:
# 				sum=sum+1
# 				print word

# print int(sum/len(filedata))

