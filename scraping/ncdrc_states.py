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


display = Display(visible=0, size=(800, 600))
display.start() 

check=0
all_links=[]
all_links_html=[]

errorlist_html=[]

for outermost in range(2,8):
	#dir = os.path.dirname("C:/Users/user/Desktop/chromedriver.exe")
	#chrome_driver_path = dir + "/chromedriver.exe"
	 
	# create a new Chrome session
	driver = webdriver.Chrome()
	driver.implicitly_wait(30)
	driver.maximize_window()
		
	driver.get("http://cms.nic.in/ncdrcusersWeb/search.do?method=loadSearchPub")

	# find_element_by_xpath("//select[@id='searchBy']/option[@value='6']").click()
	mySelect = Select(driver.find_element_by_id("searchBy"))
	mySelect.select_by_visible_text("Between dates")
	select = driver.find_element_by_xpath( "//select[@id='stateId']")  #get the select element            
	options = select.find_elements_by_tag_name("option") #get all the options into a list
	# print(options)

	optionsList = []
	statelist=[]
	#iterate over the options, place attribute value in list
	for option in options: 
		optionsList.append(option.get_attribute("value"))
		statelist.append(option.text) 




	#create folders for all states
	root_path = '/home/kaiz_python/ncdrc1'
	# print(statelist)

	statelist.remove(u"Circuit Bench Kohlapur")
	statelist.remove(u"Circuit Bench Asansol")
	statelist.remove(u"Circuit Bench Nashik")
	statelist.remove(u"Circuit Bench Pune")
	statelist.remove(u"Circuit Bench Siliguri")

	for folder in statelist:
		folder_name=str(folder)
		# print(folder_name)
		if not os.path.exists(os.path.join(root_path,folder_name)):
			os.mkdir(os.path.join(root_path,folder_name))
		for sc in folder:
			if not os.path.exists(os.path.join(root_path+"/"+folder_name,"statecommission")):
				os.mkdir(os.path.join(root_path+"/"+folder_name,"statecommission"))
			for p in sc:
				if not os.path.exists(os.path.join(root_path+"/"+folder_name+"/"+"statecommission","PDF")):
					os.mkdir(os.path.join(root_path+"/"+folder_name+"/"+"statecommission","PDF"))
			for h in sc:
				if not os.path.exists(os.path.join(root_path+"/"+folder_name+"/"+"statecommission","HTML")):
					os.mkdir(os.path.join(root_path+"/"+folder_name+"/"+"statecommission","HTML"))
			for e in sc:
				if not os.path.exists(os.path.join(root_path+"/"+folder_name+"/"+"statecommission","ERROR")):
					os.mkdir(os.path.join(root_path+"/"+folder_name+"/"+"statecommission","ERROR"))				






	# print(statelist)
	# print(type(optionsList))
	# print(optionsList)   
	optionsList.remove(u'49') 
	optionsList.remove(u'47') 
	optionsList.remove(u'48') 
	optionsList.remove(u'46')
	optionsList.remove(u'50')
	select = Select(driver.find_element_by_xpath( "//select[@id='stateId']"))
	select.select_by_value(optionsList[outermost])


	x=driver.find_element_by_id('searchbutton')
	x.click()
	# driver.implicitly_wait(5s)

	
	try:
	    element = WebDriverWait(driver, 10).until(
	        EC.presence_of_element_located((By.ID, "para1"))

	    )
	finally:

		# pg=driver.page_source

		# print(pg)

		mytext="&fmt=P"
		mytext1 ="getPdf"
		mytext2="caseid"
		keywordFilter=['&fmt=P','getPdf']
		links=[]
		links_html=[]
		


		



		year=2016
		

		def this_year():
			count=0
			
			

			
			for k in range (1000): 
				# print("hi")

				
				
				driver.implicitly_wait(3)
				time.sleep(2)
				pg=driver.page_source
				source=bs(pg)
				# print(pg)
				# print(type(source))
				# check=check+1
				# print(check)
				links=source.findAll('a', href=re.compile(mytext))
				difflinks=source.findAll('a', href=re.compile(mytext1))
				links_html=source.findAll('a', href=re.compile(mytext2))
				for line in difflinks:
					if "img" in str(line):
						difflinks.remove(line)
				for item in difflinks:
					if "img" in item:
						difflinks.remove(item)
				# print(difflinks)		
				for dif in difflinks:
					links.append(dif)


				# print(difflinks)	
				links1=[]
				links2=[]
				# getstate = Select(driver.find_element_by_id("stateId").text)
				for l in links:
					links1.append("http://cms.nic.in/ncdrcusersWeb/"+l['href'].encode('UTF8'))
				links1.append(statelist[outermost])

				#print(links1)
				for l in links_html:
					links2.append("http://cms.nic.in/ncdrcusersWeb/"+l['href'].encode('UTF8'))
				links2.append(statelist[outermost])
				links2 = [sent for sent in links2 if not any(word in sent for word in keywordFilter)]

		
				print(links2)
				all_links.append(links1)	
				all_links_html.append(links2)
				
				# # myelements = driver.find_elements_by_xpath('//a[contains(@href, "%s")]' % text)
				# print(links1)
				# myelements1 = driver.find_elements_by_xpath('//a[contains(@href, "%s")]' % text1)
				# try:
				# 	driver.implicitly_wait(3)
				# 	myelements1 = driver.find_elements_by_xpath('//a[contains(@href, "%s")]' % text1)
				# except NoSuchElementException:
				# 	print("one")

				

				print("hey"+str(k))


				# isnext=driver.findElements(By.xpath('//a[contains(text(), "Next")]')).size()!=0
				# isnext=driver.find_element_by_xpath('//a[contains(text(), "Next")]').size()!=0
				# isnext = driver.find_element(By.PARTIAL_LINK_TEXT,"Next" ).size()!=0
				# if isnext==True:
					# next = driver.find_element_by_xpath('//a[contains(text(), "Next")]')

				
				try:
					# driver.implicitly_wait(2)
					next = driver.find_element_by_xpath('//a[contains(text(), "Next")]')
					# print(myelements)
					
					# for item in myelements:
					# 	item.click()
					# for item in myelements1:
					# 	item.click()
					# time.sleep()
					# driver.implicitly_wait(3)
					next.click()
					time.sleep(5)
					# print(links1)

					driver.implicitly_wait(30)
				except NoSuchElementException:
					if count==0:
					# 	for item in myelements:
					# 		item.click()
					# 	for item in myelements1:
					# 		item.click()
						count=count+1	
						driver.implicitly_wait(30)	
					else:
						break
						driver.implicitly_wait(30)	
			
								
							
					
						# print("hi")
						

				


				
				
					

		this_year()	
		all_links.pop(-1)
		all_links_html.pop(-1)
		# driver.close()	
		
		driver.implicitly_wait(30)	

				
		for i in range(36):
			time.sleep(10)
			# driver.get("http://cms.nic.in/ncdrcusersWeb/search.do?method=loadSearchPub")
			inputElement = driver.find_element_by_id("stDate")
			inputElement.clear()
			inputElement.send_keys('1/1/'+str(year))

			inputElement1 = driver.find_element_by_id("endDate")
			inputElement1.clear()
			inputElement1.send_keys('31/12/'+str(year))
			time.sleep(5)
			x=driver.find_element_by_id('searchbutton')
			x.click()
			print("hello"+str(i))
			time.sleep(10)
			year=year-1
			this_year()
			# driver.close()
			all_links.pop(-1)
			all_links_html.pop(-1)		
	driver.close()
			# if inputElement.get_attribute('value')=='1/1/'+str(year) and inputElement1.get_attribute('value')=='31/12/'+str(year):
			# 	this_year()
			





#print(all_links_html)				
# print((all_links[0]))
# print((all_links[1]))
# print((all_links[2]))
# print((all_links[3]))
# print(len(all_links[4]))
# print(len(all_links[5]))



#print(all_links)
print(all_links_html)
dir = os.path.dirname("C:/Users/user/Desktop/chromedriver.exe")
chrome_driver_path = dir + "/chromedriver.exe"
 
# create a new Chrome session
#chromeOptions = webdriver.ChromeOptions()
#prefs = {"download.default_directory" : "C:\Users\user\Desktop\\test_download"}
#chromeOptions.add_experimental_option("prefs",prefs)
#chromedriver = "path/to/chromedriver.exe"
# driver = webdriver.Chrome(executable_path=chrome_driver_path, chrome_options=chromeOptions)




count=0
filenames=[]
for link_list in all_links:
	
	# print(link_list)
	#print("hi")

	state_name=str(link_list[-1])
	for link in link_list:
		
		if link==link_list[-1]:
			break
		errorlist=[]

		# driver = webdriver.Chrome(chrome_driver_path)
		# driver.implicitly_wait(30)
		# driver.maximize_window()
		
		try:
	    	 response = urllib2.urlopen(link)
		except urllib2.HTTPError, e:
		    checksLogger.error('HTTPError = ' + str(e.code))
		    errorlist.append(link)
		except urllib2.URLError, e:
		    checksLogger.error('URLError = ' + str(e.reason))
		    errorlist.append(link)
		except httplib.HTTPException, e:
		    checksLogger.error('HTTPException')
		    errorlist.append(link)
		match=re.findall(r'(\d{4})[-](\d{2})[-](\d{2})', link) 
		match_case=re.search(r'(&(cid|caseidin).*&dt)', link)
		# str(match_case.group(0))
		# print(type(match_case.group(0)))
		strmatch_case=str(match_case.group(0))
		strmatch_case=strmatch_case.replace("&dt","")
		print(strmatch_case)
		if "&cid" in strmatch_case:
			print("cid")
			strmatch_case=strmatch_case.replace("&cid=","")
		else:
			print("caseidin")
			strmatch_case=strmatch_case.replace("&caseidin=","")	

		filename=match[0][0]+"-"+match[0][1]+"-"+match[0][2]+"_"+strmatch_case
		print(str(filename))

		# strfile=str(filename)
		# if strfile not in filenames:
		# 	count=0
		# else:
		# 	count=count+1	
		    
		# filenames.append(strfile)
		#print(str(filename))   


		# name = url.split("/")
		file = open("/home/kaiz_python/ncdrc1/"+state_name+"/statecommission/PDF/"+str(filename)+".pdf", 'wb')

		if len(errorlist)!=0:
			file_error = open("/home/kaiz_python/ncdrc1/"+state_name+"/statecommission/ERROR/"+str(count)+"_"+str(filename)+".pdf", 'wb')
			while True:
				content = response.read()
				if not content:
					break
		    			# print(content)	
				file_error.write(content)

				# file.write(response.read())
			file_error.close()	


		while True:
			content = response.read()
			if not content:
				break
    			# print(content)	
			file.write(content)

		# file.write(response.read())
		file.close()	





count=0
filenames=[]
for link_list in all_links_html:
	# print(link_list)

	state_name=str(link_list[-1])
	for link in link_list:

		
		if link==link_list[-1]:
			break
		errorlist=[]

		# driver = webdriver.Chrome(chrome_driver_path)
		# driver.implicitly_wait(30)
		# driver.maximize_window()
		
		try:
	    	 response = urllib2.urlopen(link)
		except urllib2.HTTPError, e:
		    checksLogger.error('HTTPError = ' + str(e.code))
		    errorlist.append(link)
		except urllib2.URLError, e:
		    checksLogger.error('URLError = ' + str(e.reason))
		    errorlist.append(link)
		except httplib.HTTPException, e:
		    checksLogger.error('HTTPException')
		    errorlist.append(link)
		match=re.findall(r'(\d{4})[-](\d{2})[-](\d{2})', link) 
		match_case=re.search(r'(&(cid|caseidin).*&dt)', link)
		# print(str(match_case[0][0]))
		# print(type(match_case)) 
		strmatch_case=str(match_case.group(0))
		strmatch_case=strmatch_case.replace("&dt","")
		print(strmatch_case)

		if "&cid" in strmatch_case:
			strmatch_case=strmatch_case.replace("&cid=","")
		else:
			strmatch_case=strmatch_case.replace("&caseidn=","")	

		filename=match[0][0]+"-"+match[0][1]+"-"+match[0][2]+"_"+strmatch_case
		print(str(filename))  
		
		# strfile=str(filename)
		# if strfile not in filenames:
		# 	count=0
		# else:
		# 	count=count+1	
		    
		# filenames.append(strfile)
		print(str(filename))   


		# name = url.split("/")
		file = open("/home/kaiz_python/ncdrc1/"+state_name+"statecommission/HTML/"+str(filename)+".html", 'wb')

		if len(errorlist)!=0:
			file_error = open("/home/kaiz_python/ncdr1/"+state_name+"/statecommission/ERROR/"+str(count)+"_"+str(filename)+".html", 'wb')
			while True:
				content = response.read()
				if not content:
					break
		    			# print(content)	
				file_error.write(content)

				# file.write(response.read())
			file_error.close()	


		while True:
			content = response.read()
			if not content:
				break
    			# print(content)	
			file.write(content)

		# file.write(response.read())
		file.close()	

		



#print(all_links)	








		# select = driver.find_element_by_xpath( "//select[@id='stateId']")  #get the select element            
		# options = select.find_elements_by_tag_name("option") #get all the options into a list
		# print(options)

		# optionsList = []

		# for option in options: #iterate over the options, place attribute value in list
		#     optionsList.append(option.get_attribute("value"))

		# print(type(optionsList))
		# print(optionsList)   
		# optionsList.remove(u'49') 
		# optionsList.remove(u'47') 
		# optionsList.remove(u'48') 
		# optionsList.remove(u'46')
		# optionsList.remove(u'50')

		



		# for i in range(2):
		# 	driver.get("http://cms.nic.in/ncdrcusersWeb/search.do?method=loadSearchPub")
		# 	select = Select(driver.find_element_by_xpath( "//select[@id='stateId']"))
		# 	select.select_by_value(optionsList[i])


		


		
		# for optionValue in optionsList:
		# 	select = Select(driver.find_element_by_xpath( "//select[@id='stateId']"))
		# 	select.select_by_value(optionValue)
		# 	time.sleep(5)
				
		# 	x=driver.find_element_by_id('searchbutton')
		# 	x.click()		
		# 	time.sleep(10)
	 #    	full()	

				# time.sleep(3)

				
				
				# wait = WebDriverWait(driver, 10)
				# wait.until(EC.alert_is_present())
				# alertObj = driver.switch_to.alert
				# alertObj.dismiss()


			

	        	# driver.find_element_by_xpath("//*[text()='OK']").click()
	        
	    		
	        		


	  	
	        
	        		


	        



			# return List<WebElement> elements=driver.findElements(By.cssSelector("a[href*=&fmt=P]")	
			




	  
	 
	# close the browser window
	# driver.quit()