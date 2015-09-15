#file=open("dances_test.txt","a")	#todo
import requests
from bs4 import BeautifulSoup as b
import re
dic={}
url="https://en.wikipedia.org/wiki/List_of_dances"
uls=b(requests.get(url).content).find("div",{"id":"mw-content-text"}).findAll("ul")
for i in range(2,47):
#print uls[46]	#(2-47)
	
	lis=uls[i].findAll('li')
	for per_li in lis:
		
		try:
			display_order = ["Dance_name","Dance_desc","Dance_link"]
			dance_name= per_li.find('a').get("title").encode("utf-8")
			if "(page does not exist)" in str(dance_name):
				continue
			else:
				dic["Dance_name"] = " "+dance_name+" "
		
			
#print dance_name	
#		else:

#			file.write(dance_name.encode('utf-8'))		
		#try:
			dance_link="https://en.wikipedia.org"+per_li.find('a').get('href')
			dic["Dance_link"] = " "+dance_link+" "
#				file.write(dance_link.encode('utf-8'))
			#print dance_link
			link_soup=b(requests.get(dance_link).content)		

			dance_desc = link_soup.find("div",{"id":"mw-content-text"}).findAll("p")[0].text
			dance_desc = dance_desc.encode('utf-8')
			dance_desc=re.sub('\[\d*\]',"",dance_desc)
			dic["Dance_desc"] = " "+dance_desc+"  "
#				file.write(dance_desc.encode('utf-8'))				
			#print dance_desc
			try:
				img=link_soup.find("div",{"class":"thumbinner"}).find('a').find('img').get('src')
	#				if len(img)==1:
	#					print img.get('href')
				if img:
					dic["Image"] = " "+"https:"+str(img)+" "
					#print "https:"+str(img)
					display_order.append("Image")
	#				file.write(img.encode('utf-8'))
			except :
				pass
			dic["Display_order"]=str(display_order)
			print dic  
			
		except Exception as e:
			print e
		print "***********************************************************************************************************************"		
		
