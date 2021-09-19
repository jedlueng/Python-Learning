#By Jedsada LUENGARAMSUK 16/4/2021
#! python3 
# downloadXkcd.py - Downloads every single XKCD comic 


import requests, os, bs4

url = 'http://xkcd.com'     #starting url 
os.makedirs('xkcd', exist_ok=True) #store comics in ./xkcd 
#exist_ok = If the target directory already exists an OSError is raised if its value is False otherwise not

while not url.endswith('#'):
    #TODO: Download the page. 
    print('Downloading page $s...' % url)
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text) #This is the text (beautiful soup object)

    #TODO: Find the URL of the comic image. 
    comicElem = soup.select('comi img') #select comic img element 
    if comicElem == []: 
        print('Could not ifnd comic image.')
    else: 
        comicUrl = comicElem[0].get('src')
    #TODO: Download the image 
    print('Downloading image %s...' % (comicUrl))
    res = requests.get(comicUrl)
    res.raise_for_status()

    #TODO: Save the image to ./xkcd. 
    imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)),'wb')
    for chunk in res.iter_content(100000):
        imageFile.write(chunk)
    imageFile.close()

    #TODO: Get the Prev button's url. 
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com' + prevLink.get('href')

print('Done')





