import requests
from bs4 import BeautifulSoup


# for i in range(406):
page = requests.get("http://judis.nic.in/supremecourt/imgst.aspx?filename=31813")
# print (page.content)
soup = BeautifulSoup(page.content, 'html.parser')
test=soup.find_all('textarea')[0].get_text()
# print (test)
text_file = open("Output.txt", "w")

text_file.write(test)

text_file.close()