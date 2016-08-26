#!/usr/bin/env python
from urllib.parse import urlparse
import urllib.request
from pyquery import PyQuery as pq
from pprint import pprint

import argparse
import os

def getDownloadList(url='http://www.yahoo.co.jp'):
    dom = pq(url)
    result = set()
    for img in dom('img').items():
        img_url = img.attr['src']
        if img_url.startswith('http'):
            result.add(img_url)
        else:
            result.add(urlparse.urljoin(url, img_url))
            
    return result

def download(resulturl, output, outFname):
    if not os.path.exists(output):
        os.mkdir(output)

    i = 0
    for url in resulturl:
        urllib.request.urlretrieve(url, '{0}/{1}_{2}.png'.format(output,outFname, i))
        i = i + 1


def main():
    parser = argparse.ArgumentParser(description='URL for download')
    parser.add_argument('--url','-u', default='http://www.yahoo.co.jp')
    parser.add_argument('--out','-o', default='output')
    parser.add_argument('--outFname','-n', default='output')
    args = parser.parse_args()
    
    resulturl = getDownloadList(args.url)
    download(resulturl, args.out, args.outFname)

if __name__ == "__main__":
    main()
