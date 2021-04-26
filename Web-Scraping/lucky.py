#Created by Jedsada LUENGARAMSUK 15/4/2021
#lucky.py - Opens several Google search results. 

import requests, sys, webbrowser , bs4 

print('Googling... now') #Display text while downloading the Google page 
res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status() #Check status of this page, if doesn't work it will raise an error 


#Retrieve top search result links. 
soup = bs4.BeautifulSoup(res.text)

#Open a browser tab for each result 
linkElems = soup.select('.r a')
numOpen = min(5, len(linkElems)) #Select the right element
for i in range(numOpen): 
    webbrowser.open('http://google.com' + linkElems[i].get('href'))


#After learning HTML it will make sense. 