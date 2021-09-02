# Downloader
import pandas as pd
import requests
import urllib.request,urllib.error,urllib.parse
def getUrlContent(url):
    #downloads and returns content
    return requests.get(url).content
"""a="https://www.icicibank.com/"
data=getUrlContent(a)
print(data)"""
def downloadUrl(url):
    #downloads and returns content
    response = urllib.request.urlopen(url)
    webContent = response.read()
    return webContent
"""a="https://www.icicibank.com/"
data=downloadUrl(a)
print(data)"""

def SaveFile(filename,data):
    file = open(filename,"w")
    file.write(data)
    file.flush()
    file.close()

def getLocalFileName(site):
    filedirectory="saved/"
    if site.startswith("https://"):
        filename=site.replace("https://","")+ ".txt"
        filename= filename.replace("/","-")
    else:
        filename=site.replace("http://","")+ ".txt"
    return filedirectory + filename

