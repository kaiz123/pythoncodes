from pyvirtualdisplay import Display
from selenium.webdriver.support.ui import Select
import requests
from bs4 import BeautifulSoup as bs
import os
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time
import re
import urllib2
import requests
import httplib
import socket
import glob
import pickle

display = Display(visible=0, size=(800, 600))
display.start() 


# create a new Chrome session
driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.maximize_window()


with open(r'/home/kaiz_python/data_2017.txt', 'r') as f:
    mylinks = [line.strip() for line in f]
    mylinks=list(sorted(set(mylinks), key=mylinks.index))
    # if "http://patnahighcourt.gov.in/ShowJPdf.aspx?noc=1&cno=4&year=1995&search=" in mylinks:
    # 	print("http://patnahighcourt.gov.in/ShowJPdf.aspx?noc=1&cno=4&year=1995&search=")
    # mylinks=mylinks[-100:]
    print(len(mylinks))
    print(type(mylinks))
# chromeOptions = webdriver.ChromeOptions()
# prefs = {"download.default_directory" : r"C:/Users/user/Desktop","directory_upgrade": True}
# # chromeOptions.add_experimental_option("prefs",prefs)
# # chromeOptions.add_argument("download.default_directory=C:\\Users\\user\\Desktop")
# driver = webdriver.Chrome(chrome_driver_path,chrome_options=chromeOptions)
# driver.implicitly_wait(30)
# driver.maximize_window()






# with open("mydict_2017.txt", "rb") as myFile:
#     mydict = pickle.load(myFile)
# with open("mydict1_2017.txt", "rb") as myFile:
#     mydict1= pickle.load(myFile)

# print mydict

# # mydict={}
# # mydict1={}

# def years(first,second):
# 	driver = webdriver.Chrome()
# 	driver.implicitly_wait(30)
# 	driver.maximize_window()
# 	driver.get("http://patnahighcourt.gov.in/JudgementFTS.aspx")
# 	inputElement = driver.find_element_by_name("ctl00$MainContent$txtFrom")
# 	inputElement.clear()
# 	inputElement.send_keys(first)

# 	inputElement1 = driver.find_element_by_name("ctl00$MainContent$txtTo")
# 	inputElement1.clear()
# 	inputElement1.send_keys(second)
# 	time.sleep(10)
# 	x=driver.find_element_by_name('ctl00$MainContent$btnSeach')
# 	x.click()


# 	# SMRtable = driver.find_element_by_xpath('//*[@id="ctl00_MainContent_gvSearch"]/tbody')

# 	# for i in SMRtable.find_elements_by_xpath('.//tr'):
# 	#     print i.get_attribute('innerHTML')
# 	table_id = driver.find_element(By.ID, 'ctl00_MainContent_gvSearch')
# 	rows = table_id.find_elements(By.TAG_NAME, "tr") # get all of the rows in the table
# 	# print(type(rows))
# 	soup = bs(driver.page_source)
# 	table = soup.find(lambda tag: tag.name=='table' and tag.has_key('id') and tag['id']=="ctl00_MainContent_gvSearch")
# 	rows1 = table.findAll(lambda tag: tag.name=='tr')
# 	# print(rows)
# 	rcount=0
# 	for row,row1 in zip(rows,rows1):
# 		rcount=rcount+1
# 		# print(type(row))
# 		# if rcount>100:
# 		# 	break
# 	    # Get the columns (all the column 2)        
# 		# col = row.find_elements(By.TAG_NAME, "td")[2] #note: index start from 0, 1 is col 2
# 		# print(col)
# 		# print col.text #prints text from the element
# 		if rcount>1:
# 			cells = row1.findAll(lambda tag: tag.name=='td')
# 			for index,elem in enumerate(cells):
# 				elem=str(elem)
# 				elem=elem.replace("\n","")
# 				# print(elem)
# 				elem=re.search(r'\>.*\<', elem).group()
# 				elem=elem.replace("<","")
# 				elem=elem.replace(">","")
# 				print(elem)
# 				if index==6:
# 					doj=elem

# 				if index==4:
# 					pet=elem
# 					pet=pet.replace("amp","")
# 					pet=pet.replace(";","")
# 				if index==5:
# 					res=elem	
# 					res=res.replace("amp","")
# 					res=res.replace(";","")	
				
# 			# print(type(cells))



# 			thisrow=row.text
# 			# print thisrow
# 			if rcount>1:
# 				yr=re.findall(r'-(\d{4})',thisrow)
# 				stryr=str(yr[0])
# 				stryr=stryr.replace("-","")
# 				print(stryr)
# 				cno=re.findall(r'(\d+)',thisrow)
# 				strcno=str(cno[1])
# 				filing_yr=str(cno[2])
# 				print(strcno)
# 				# print(strcno)
# 				mydict[strcno]=stryr
# 				mydict1[strcno]="<CASE_NO>"+"\n"+strcno+" of "+filing_yr+"\n"+"</CASE_NO>"+"\n"+"<DOJ>"+"\n"+doj+"\n"+"</DOJ>"+"\n"+"<PETITIONER>"+"\n"+pet+"\n"+"</PETITIONER>"+"\n"+"<RESPONDENT>"+"\n"+res+"\n"+"</RESPONDENT>"

# 	driver.close()





# # years("01-Jan-1994","31-Dec-1995")
# years("01-Jan-2017","29-Sep-2017")
# years("01-Jan-1994","31-Dec-2010")

# print(mydict)
# with open("mySavedDict.txt", "wb") as myFile:
#     pickle.dump(mydict, myFile)
		








counter=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.maximize_window()
	


count=0
for link in mylinks:
	count=count+1
	strlink=str(link)
	print(strlink)
	caseno=re.search(r'cno=(.*?)&year', link).group(1)
	print(caseno)
	# for key,val in mydict.items():
	# 	# print(key+"-"+val)

	# 	if key==caseno:
	# 		print 'hi'
	# 		year=val
	# year=re.search(r'year=(.*?)&', link).group(1)
	# thiscount=int(year)-1994
	# counter[thiscount]=counter[thiscount]+1
	# print(caseno)
	if count>100:
		break
	
	# x=driver.find_element_by_id("download").get_attribute('href')
	# print(x)
	try:
		driver.get(link)
		result = (urllib2.urlopen(link)).geturl()
		# response=urllib2.urlopen(result)
		driver.get(result)
		driver.find_element_by_id("download").click()
		time.sleep(3)
		# driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 'w')

		newest = max(glob.iglob('/home/kaiz_python/*.pdf'), key=os.path.getctime)
		os.rename(newest, '/home/kaiz_python/patna_test/'+caseno+'.pdf')
		# file = open('/home/kaiz_python/patna_tags/'+year+" NearLaw (Patna HC) "+str(counter[thiscount])+'.xml','w') 
 
		# file.write(mydict1[caseno]) 
		# file.close()
	except:
		file = open('/home/kaiz_python/patna_log.txt','a') 
 
		file.write(caseno+"   "+result+"\n") 
		file.close()










	# print(newest)