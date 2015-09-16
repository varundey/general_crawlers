import requests
from bs4 import BeautifulSoup as b
from pymongo import MongoClient
cl = MongoClient()
coll = cl["local"]["test2"]
url="http://www.differencebetween.info/tagclouds/chunk/3"
soup=b(requests.get(url).content)		#getting inside main link
tags = soup.find("div",{"class":"wrapper tagclouds"}).findAll('a')		#tags list has all tags
display_order = ["Title1","Title2","TitleLink","Description"]
dic={}
for per_tag in tags:
	tag_link = "http://www.differencebetween.info"+per_tag.get('href')
#	print tag_link
	link_soup = b(requests.get(tag_link).content)			#getting inside tag link 
	total_pages = link_soup.find("li",{"class":"pager-last odd last"}).find('a').get('href')	#finding total no of pages
	total_pages=int(total_pages.split("=")[1])
	
	
	for curr_page in range(total_pages):					#iterating
		page_url=tag_link+"?page=%d"%curr_page
		print page_url
		
		result_table = b(requests.get(page_url).content).find('div',{"class":"view-taxonomy-term"}).findAll('tr',{"class":"row-1 row-first row-last"})			#getting inside tags and generating result div
		
		for per_result_table in result_table:
			link = "http://www.differencebetween.info"+per_result_table.find('div',{"class":"views-field views-field-title"}).find('a').get('href')
			dic["TitleLink"] = " "+link+" "	
#			print link
			linksoup = b(requests.get(link).content)		#going inside link
			title = linksoup.find("header",{"id":"main-content-header"}).text
#			print title.strip()
			try:
				title1 = title.split("Difference between ")[1].split(" and ")[0].encode('utf-8').strip()
				dic["Title1"] = " "+title1+" "
				title2 = title.split("Difference between ")[1].split(" and ")[1].encode('utf-8').strip()
				dic["Title2"] = " "+ title2+" "
#				print title1
#				print title2
				desc = 	linksoup.find("div",{"class":"panel-pane pane-custom pane-1 no-title block"})
				if desc.find("h5"):
#					print desc.find('h5').text.strip()
					dic["Description"] = " "+desc.find('h5').text.encode('utf-8').strip()+" "
					print "*****************************************************************************************************************"
				else:
#					print desc.find('p').text.strip()
					dic["Description"] = " " + desc.find('p').text.encode('utf-8').strip() + " "
					print "***************************************************************************************************"				
			except Exception as e:
				print e
				pass
			print dic
			coll.insert(dic)
			
