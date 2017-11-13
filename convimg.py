import os
import sys, getopt
import textract

root_path=r'/home/kaiz_python/mycap.jpeg'

text=textract.process(root_path,method="pdfMiner")
print(text)
print("hi")
thisfile = open("/home/kaiz_python/"+"text.txt",'w') 
thisfile.write(text)  
				 
thisfile.close() 
