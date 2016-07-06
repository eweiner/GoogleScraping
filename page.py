__author__ = 'ericweiner'
from bs4 import BeautifulSoup
import urllib3
import urllib.request
class Page():
    def __init__(self, url, domain='google'):
        self.url = url
        self.domain = domain
#        opener = urllib2.build_opener()
#        opener.addheaders = [('User-agent', 'Mozilla/5.0')]'
        req = urllib.request.Request(self.url, data=None, headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'
        })
        self.page = urllib.request.urlopen(req)
        self.soup = BeautifulSoup(self.page, 'html.parser')

    def gSoupToLinks(self):
        cites = [cite.findAll('a', href = True) for cite in self.soup.findAll('h3') if ".com" not in str(cite) and "http:" not in str(cite)]
        toReturn = [str(cite)[str(cite).find('<a href="') + 15:str(cite).find('" ')]
                    for cite in cites]
        return toReturn


    def __str__(self):
        if self.domain == 'google':
            links = self.gSoupToLinks(self.soup)

        return links

