__author__ = 'ericweiner'
from page import Page
import random
import time
class Search():
    def convertToUrlReady(self, term):
        for i in range(len(term)):
            if term[i] == " ":
                term = term[:i] + "%20" + term[i+1:]
                i += 2

        return term

    def googleSearch(self, ending, numPages = 1):
        term = self.convertToUrlReady(ending)
        links = []
        for start in range(0,numPages):
            url = "https://www.google.com/search?q=site:" + term +"+https&safe=active&start=" + str(start*10)
            page = Page(url)
            links.append(page.gSoupToLinks())
            random_interval = random.randrange(15, 20, 1)
            print("sleeping for: " + str(random_interval) + " seconds")
            time.sleep(random_interval)

        return links



