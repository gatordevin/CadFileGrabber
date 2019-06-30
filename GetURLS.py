from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests, zipfile, io
URL = "https://www.gobilda.com/"
resp = urlopen(URL)
soup = BeautifulSoup(resp, from_encoding=resp.info().get_content_charset(), features="html.parser")
parentURLS = ["https://www.gobilda.com/"]
for link in soup.find_all('a', href=True):
    parentURLS.append(link['href'])
 
def getSubDir(parent, omit):
    global parentURLS
    tempList = []
    for link in parent:
        if("https://www.gobilda.com/" in link):
            resp = urlopen(link)
            soup = BeautifulSoup(resp, from_encoding=resp.info().get_content_charset(),features="html.parser")
            for sublink in soup.find_all('a', href=True):
                if sublink['href'] not in omit and "https://www.gobilda.com/" in sublink["href"]:
                    tempList.append(sublink['href'])
                    parentURLS.append(sublink["href"])
                    #print(sublink["href"])
    return(tempList)
def getCAD(parent):
	for link in parent:
		if("https://www.gobilda.com/" in link):
			resp = urlopen(link)
			soup = BeautifulSoup(resp, from_encoding=resp.info().get_content_charset(),features="html.parser")
			for anchor in soup.findAll('a', href=True):
				#print(anchor["href"])
				if(anchor["href"].endswith(".zip")):
					Step = "https://www.gobilda.com" + anchor["href"]
					print(Step)
					r = requests.get(Step)
					z = zipfile.ZipFile(io.BytesIO(r.content))
					z.extractall()
    
subURLs = getSubDir(parentURLS[0:10],parentURLS)
sub2URLs = getSubDir(subURLs, parentURLS)
print(getCAD(sub2URLs))
