import selenium
from selenium.webdriver.support.ui import Select
import requests
from bs4 import BeautifulSoup as bs
import os

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
from PIL import Image
import StringIO
import base64


check=0
all_links=[]
all_links_html=[]

errorlist_html=[]

for outermost in range(24,25):
	dir = os.path.dirname("C:/Users/user/Desktop/chromedriver.exe")
	chrome_driver_path = dir + "/chromedriver.exe"
	 
	# create a new Chrome session
	driver = webdriver.Chrome(chrome_driver_path)
	driver.implicitly_wait(30)
	driver.maximize_window()
		
	driver.get("http://patnahighcourt.gov.in/JudgementFTS.aspx")
	elem = driver.find_element_by_css_selector("#aspnetForm > div.page > div.pageBody > table > tbody > tr:nth-child(1) > td > div > table > tbody > tr:nth-child(2) > td > table > tbody > tr:nth-child(9) > th > img")
	loc, size  = elem.location, elem.size
	left, top     = loc['x'], (loc['y'] - 587)
	width, height = size['width'], size['height']
	box = (int(left), int(top), int(left+width), int(top+height))
	screenshot = driver.get_screenshot_as_base64()
	img = Image.open(StringIO.StringIO(base64.b64decode(screenshot)))
	captcha = img.crop(box)
	captcha.save('captcha.png', 'PNG')



	#time.sleep(10)
 #get the select element            
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