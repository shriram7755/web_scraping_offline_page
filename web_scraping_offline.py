# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 09:19:45 2023

@author: acer
"""

from bs4 import BeautifulSoup
soup=BeautifulSoup(open("sample_doc.html"),'html.parser')
print(soup)

# it is going to show all the html content extracted
soup.text
# it will show only text
soup.contents
# it will going to show all the html contents extracted
soup.find('address')
soup.find_all('address')
soup.find_all('q')
soup.find_all('b')
table=soup.find('table')
table

    
# it will show all rows except first row

###############################################################################








