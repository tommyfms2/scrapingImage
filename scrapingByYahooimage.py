
from urllib.parse import urlparse
import urllib.request
from pyquery import PyQuery as pq
from pprint import pprint

import argparse

from scraping_image import download

def getDownloadListInYahooImage(url):
    dom = pq(url)
    result = set()
    for alink in dom('a').items():
        if alink.attr['target']=='imagewin':
            img_url = alink.attr['href']
            if img_url.startswith('http'):
                result.add(img_url)
                

    return result

def main():
    parser = argparse.ArgumentParser(description="yahoo image scraping")
    parser.add_argument('--query','-q', default='yahoo')
    args = parser.parse_args()
    parser.add_argument('--out','-o', default=args.query)
    parser.add_argument('--outFname','-n', default=args.query)
    args = parser.parse_args()

    resultsurl = getDownloadListInYahooImage('http://image.search.yahoo.co.jp/search?p={0}'.format(args.query))

    download(resultsurl, args.out, args.outFname)
    
if __name__=='__main__':
    main()
