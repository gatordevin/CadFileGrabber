from bs4 import BeautifulSoup
import urllib2

URL = "https://www.gobilda.com/"
resp = urllib2.urlopen(URL)
soup = BeautifulSoup(resp, from_encoding=resp.info().getparam('charset'), features="html.parser")
parentURLS = ["https://www.gobilda.com/"]
for link in soup.find_all('a', href=True):
    parentURLS.append(link['href'])

def getSubDir(parent, omit):
    global parentURLS
    tempList = []
    for link in parent:
        if("https://www.gobilda.com/" in link):
            resp = urllib2.urlopen(link)
            soup = BeautifulSoup(resp, from_encoding=resp.info().getparam('charset'),features="html.parser")
            for sublink in soup.find_all('a', href=True):
                if sublink['href'] not in omit and "https://www.gobilda.com/" in sublink["href"]:
                    tempList.append(sublink['href'])
                    parentURLS.append(sublink["href"])
    return(tempList)
subURLs = getSubDir(parentURLS[0:10],parentURLS)
sub2URLs = getSubDir(subURLs, parentURLS)
print(sub2URLs)
print(getSubDir(sub2URLs[3:4], parentURLS))
'''
for link3 in subURL2:
    if("https://www.gobilda.com/" in link3):
        resp = urllib2.urlopen(link3)
        soup = BeautifulSoup(resp, from_encoding=resp.info().getparam('charset'),features="html.parser")
        for link4 in soup.find_all('a', href=True):
            if link4['href'] not in subURL1 and link4['href'] not in subURL2 and "https://www.gobilda.com/" in link4["href"]:
                print(link4["href"])
'''
