#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib
import urllib2
import sys
import time
import csv



def crawStEz(page_num):
    url='http://www.streeteasy.com/buildings/nyc/building_amenities:leed_registered?page='+page_num
    req=urllib2.Request(url)
    response=urllib2.urlopen(req)
    print 'page '+page_num+' crawled, processing string now...'
    return  response.read()

def procHtml(con):
    buildings=con.split('<div id="building')[1:]
    for bd in buildings:
        name=bd.split('se:clickable:target="true">')[-1].split('</a>')[0].rstrip()
        address=bd.split('<div class=\'closer\'>')[0].split('</div>')[-1].lstrip().rstrip()
        print "name:"+name+"\taddress:"+address
        writer.writerow([name,address])
    if '<span class="next">' in con:
        nextpage = con.split('<span class="next">')[-1].split('" rel="next">')[0].split('page=')[1]
        #sentence = con.split('<span class="next">')[-1].split('<div id="searchModal"')[0]
        #return sentence
        return nextpage
    else:
        return 'last page'

if __name__=="__main__":

    writer = csv.writer(open('leedr.csv', 'w'))
    writer.writerow(['name', 'address']) 

    if len(sys.argv)!=2:
        print 'should be:'+sys.argv[0]+' page_num'
        sys.exit(1)

    con = crawStEz('1')
    nextpageN = procHtml(con)
    while nextpageN != 'last page':
       con = crawStEz(nextpageN)
       nextpageN = procHtml(con)
       time.sleep(60)


