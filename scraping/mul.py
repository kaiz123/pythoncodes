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
import time
 
# get the path of ChromeDriverServer
dir = os.path.dirname("C:/Users/user/Desktop/chromedriver.exe")
chrome_driver_path = dir + "/chromedriver.exe"
 
# create a new Chrome session
driver = webdriver.Chrome(chrome_driver_path)
driver.implicitly_wait(30)
driver.maximize_window()
 
# navigate to the application home page

driver.get("http://cms.nic.in/ncdrcusersWeb/search.do?method=loadSearchPub")
# find_element_by_xpath("//select[@id='searchBy']/option[@value='6']").click()
mySelect = Select(driver.find_element_by_id("searchBy"))
mySelect.select_by_visible_text("Between dates")
x=driver.find_element_by_id('searchbutton')
x.click()
# driver.refresh()
# driver.implicitly_wait(5s)

# driver.find_element_by_partial_link_text(r"GetJudgement.do?method=GetJudgement&caseidin=0%2F0%2FCC%2F1184%2F2015&dtofhearing=2017-01-04&fmt=P").click()
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "para1"))

    )
finally:

	pg=driver.page_source

	# print(pg)
# links = browser.find_elements_by_partial_link_text('&fmt=P')
# for link in links:
#     print link.get_attribute("href")
	text = "&fmt=P"

	 
	year=2016
	count=0
	def this_year():


		for k in range (2): #replace 3 by 111
			myelements = driver.find_elements_by_xpath('//a[contains(@href, "%s")]' % text)
			next = driver.find_element_by_xpath('//a[contains(text(), "Next")]')
			print(type(myelements))

					

			print(myelements)
			for item in myelements:
				item.click()
			next.click()
	this_year()		


		

			
	for i in range(1):
		inputElement = driver.find_element_by_id("stDate")
		inputElement.clear()
		inputElement.send_keys('1/1/'+str(year))

		inputElement1 = driver.find_element_by_id("endDate")
		inputElement1.clear()
		inputElement1.send_keys('31/12/'+str(year))
		x=driver.find_element_by_id('searchbutton')
		x.click()
		time.sleep(10)
		year=year-1
		count=count+1

		# if inputElement.get_attribute('value')=='1/1/'+str(year) and inputElement1.get_attribute('value')=='31/12/'+str(year):
		# 	this_year()
		this_year()
				

	

	# select = driver.find_element_by_xpath( "//select[@id='stateId']")  #get the select element            
	# options = select.find_elements_by_tag_name("option") #get all the options into a list
	# print(options)

	# optionsList = []

	# for option in options: #iterate over the options, place attribute value in list
	#     optionsList.append(option.get_attribute("value"))

	# for optionValue in optionsList:
	#     print "starting loop on option %s" % optionValue

	#     select = Select(driver.find_element_by_xpath( "//select[@id='stateId']"))
	#     select.select_by_value(optionValue)
	#     time.sleep(3)



		# return List<WebElement> elements=driver.findElements(By.cssSelector("a[href*=&fmt=P]")	
		




  
 
# close the browser window
# driver.quit()