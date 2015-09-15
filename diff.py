import requests
import re
from bs4 import BeautifulSoup as b
url="http://www.differencebetween.net/"

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
			print link
			print title
			try:
				link_soup=b(requests.get(link).content)
				p = link_soup.find("div",{"class":"entry clearfloat"}).findAll("p")
				if len(p[1].text)<=50:

					if len(p[2].text) <= 50:
					
						print p[3].text
						print "*************************************************************************************************************"
						continue
					elif len(p[2].text) > 50: 
						print p[2].text
						print "*************************************************************************************************************"
						continue

				elif len(p[1].text)>50:
					print p[1].text
					print "*************************************************************************************************************"
					continue
#			print desc.text
			except Exception as e:
				print e
