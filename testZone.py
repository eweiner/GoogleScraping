from genAlg import Population
from internetSearch import Search
__author__ = 'ericweiner'
import urllib
from bs4 import BeautifulSoup

#print(BeautifulSoup(urllib.request.urlopen("https://www.google.com"),"html.parser").title.string)



#s = Search()
#print(s.googleSearch("mil", 10))

def createFile(suffix, npages):
    f = open(suffix + "Sites.txt", "w")
    s = Search()
    results = s.googleSearch(suffix,npages)
    for site in results:
        if not site == "":
            f.write(site + "\n")
    f.close()

createFile("mil", 1)
