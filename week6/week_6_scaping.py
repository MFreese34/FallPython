# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 20:10:00 2019

@author: Milo
"""
import urllib.request
import bs4

def getSearchURL(term):
    url = input('Enter Web Address: ') 
    url = (url + '%s') % (str(term))
    return url

def getHTMLPageText(url):
    request = urllib.request.Request(url)
    # use the resource manager to request the page from the internet
    # and retrieve the HTML from that response for use as the return val
    with urllib.request.urlopen(request) as response:
        return response.read()

def getSearchInquiry():
    term = input('Enter search term: ')
    return term

def getSpanClassID():
    span = input('Enter desired span class name: ')
    return span

def fileName():
    file_name = input('Enter file name: ')
    return file_name

def writeToFile(file, item):
    try:
        f = open(file)
        f.close()
        with open(file, mode='a') as search_log:
            search_log.write(item)
            search_log.write('\n')
    except FileNotFoundError:
        with open(file, mode='w') as search_log:
            search_log.write(item)
            search_log.write('\n')
    # close file 
    search_log.close()
    
def main():
    pageText = getHTMLPageText(getSearchURL(getSearchInquiry()))
    soup = bs4.BeautifulSoup(pageText, 'html.parser')
    eles = soup.find_all('a', getSpanClassID())
    file = fileName()
    for item in eles:
        tag = item.find('span').string
        writeToFile(file, tag)
    
if __name__== '__main__':
    main()