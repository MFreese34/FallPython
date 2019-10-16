# -*- coding: utf-8 -*-
#####################################
# DAT-129                           # 
# Purpose: Webscraping              #
# Author: Milo Freese               #
# Last Modified: 10/16/2019         #
#####################################

# Import statements
import urllib.request
import bs4


#####################################
# Obtain Web address from user      #
#####################################
def getSearchURL(term):
    url = input('Enter Web Address: ') 
    url = (url + '%s') % (str(term))
    return url


######################################
# Obtain HTML Page Text              #
######################################
def getHTMLPageText(url):
    request = urllib.request.Request(url)
    # use the resource manager to request the page from the internet
    # and retrieve the HTML from that response for use as the return val
    with urllib.request.urlopen(request) as response:
        return response.read()

#####################################
# Obtain Search term from user      #
#####################################
def getSearchInquiry():
    term = input('Enter search term: ')
    return term

############################################################
# Obtain Span class name from user for desired search term #
############################################################
def getSpanClassID():
    span = input('Enter desired span class name: ')
    return span

######################################
# Obtain desired file name from user #
######################################
def fileName():
    file_name = input('Enter file name: ')
    return file_name

######################################
# Write items into a file            #
######################################
def writeToFile(file, item):
    # Determine if file name already exists
    try:
        f = open(file)
        f.close()
        # append the file if it already exists
        with open(file, mode='a') as search_log:
            search_log.write(item)
            search_log.write('\n')
    except FileNotFoundError:
        # Write to a new file if the file does not exist
        with open(file, mode='w') as search_log:
            search_log.write(item)
            search_log.write('\n')
            
    # close file 
    search_log.close()
    
######################################
# Main Function                      #
######################################
def main():
    
    # Get HTML Page text, website url, and desired search term
    pageText = getHTMLPageText(getSearchURL(getSearchInquiry()))
    soup = bs4.BeautifulSoup(pageText, 'html.parser')
    # Obtain span class name and find items relative to search term
    eles = soup.find_all('a', getSpanClassID())
    # prompt user to enter file name
    file = fileName()
    # write items into file
    for item in eles:
        tag = item.find('span').string
        writeToFile(file, tag)
    
if __name__== '__main__':
    main()