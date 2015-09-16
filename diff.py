import requests
import re
#from pymongo import MongoClient
#cl = MongoClient()
#coll = cl["local"]["test2"]
from bs4 import BeautifulSoup as b
url="http://www.differencebetween.net/"
display_order = ["Title1","Title2","TitleLink","Description"]
dic={}
###getting all categories####
cats=b(requests.get(url).content).find("div",{"id":"featured-cats"}).findAll("h5")

for per_cat in cats:

###getting links category wise
	cat_link = per_cat.find('a').get('href')
#	print cat_link
	
###getting page numbers if exists	
	try:
		pages=b(requests.get(cat_link).content).find("span",{"class":"pages"}).text
		pages = re.findall(r'.[\d]',pages)
		pages= int(pages.pop().strip())
		
	except Exception as e:
		print e
	
	for curr_page in range(1,pages+1):
		cat_soup = cat_link+"page/%d/"%curr_page
		print "*************************************************************************************************************"
		print cat_soup
		print "*************************************************************************************************************"
		lis=b(requests.get(cat_soup).content).find("ul",{"class":"archive-list clearfloat"}).findAll("li")
		for per_li in lis:
			link = per_li.find('a').get('href')
			title = per_li.find('a').get('title')
#			print link
			try:
				dic["TitleLink"] = " "+ link +" "			
	#			print title
				title1 = title.split("ween")[1].split("and")[0].strip().encode('utf-8')
	#			print title1
				dic["Title1"] = " "+ title1 +" "
				title2 = title.split("ween")[1].split("and")[1].strip().encode("utf-8")
				dic["Title2"] = " "+ title2 +" "			
#			print title2

				link_soup=b(requests.get(link).content)
				p = link_soup.find("div",{"class":"entry clearfloat"}).findAll("p")
				if len(p[1].text)<=50:

					if len(p[2].text) <= 50:
						dic["Description"] = " "+ p[3].text.strip().encode('utf-8')  +" "					
#						print p[3].text
						print dic
						print "*************************************************************************************************************"
						continue
					elif len(p[2].text) > 50: 
#						print p[2].text
						dic["Description"] = " "+ p[2].text.strip().encode('utf-8')  +" "					
						print dic
						print "*************************************************************************************************************"
						continue

				elif len(p[1].text)>50:
#					print p[1].text
					dic["Description"] = " "+ p[1].text.strip().encode('utf-8')  +" "
					print dic
					print "*************************************************************************************************************"
					continue
#			print desc.text
			except Exception as e:
				print e
				pass

