'''
Created on 2016-8-4

@author: wzg
'''
import urllib


class HtmlDownloader(object):
    
    
    def download(self,url):
        
        
        if url is None:
            return None
        response = urllib.request.urlopen(url)
        
        if response.getcode()!=200:
            return None
        return response.read()
    



