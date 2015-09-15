import requests
from bs4 import BeautifulSoup as b
url="http://www.differencebetween.info/tagclouds/chunk/3"
soup=b(requests.get(url).content)		#getting inside main link
tags = soup.find("div",{"class":"wrapper tagclouds"}).findAll('a')		#tags list has all tags
for per_tag in tags:
	tag_link = "http://www.differencebetween.info"+per_tag.get('href')
	print tag_link
	link_soup = b(requests.get(tag_link).content)			#getting inside tag link 
	total_pages = link_soup.find("li",{"class":"pager-last odd last"}).find('a').get('href')	#finding total no of pages
	total_pages=int(total_pages.split("=")[1])
	
	
	for curr_page in range(total_pages):					#iterating
		page_url=tag_link+"?page=%d"%curr_page
		
		result_table = b(requests.get(page_url).content).find('div',{"class":"view-taxonomy-term"}).findAll('tr',{"class":"row-1 row-first row-last"})			#getting inside tags and generating result div
		
		for per_result_table in result_table:
			link = "http://www.differencebetween.info"+per_result_table.find('div',{"class":"views-field views-field-title"}).find('a').get('href')
			print link
			linksoup = b(requests.get(link).content)		#going inside link
			title = linksoup.find("header",{"id":"main-content-header"}).text
			print title.strip()
			title1 = title.split("Difference between ")[1].split(" and ")[0]
			title2 = title.split("Difference between ")[1].split(" and ")[1]
			print title1
			print title2	
			
			
			desc = 	linksoup.find("div",{"class":"panel-pane pane-custom pane-1 no-title block"})
			if desc.find("h5"):
				print desc.find('h5').text
			else:
				print desc.find('p').text
		
	'''
	
	
	
	result_table = b(requests.get(link).content).find('div',{"class":"view-taxonomy-term"}).findAll('tr',{"class":"row-1 row-first row-last"})			#getting inside tag and generating result div
	
	for per_result_table in result_table:
		link = "http://www.differencebetween.info"+per_result_table.find('div',{"class":"views-field views-field-title"}).find('a').get('href')
		print link
		linkup = b(requests.get(link).content)		
		total_pages = link_soup.find("li",{"class":"pager-last odd last"}).find('a').get('href')
		total_pages=total_pages.split("=")[1]
		
		for per_page in range (total_pages):
		
			
		
			title = link_soup.find("header",{"id":"main-content-header"}).text
			print title.strip()
			title1 = title.split("Difference between ")[1].split(" and ")[0]
			title2 = title.split("Difference between ")[1].split(" and ")[1]
			print title1
			print title2		
		
#	for per_result_table in result_table:
		
#	print len(result_table)	
	
	print "****************************************************************************************************************************"
	
	
	'''
