#!/usr/bin/env python

import urllib
import urllib2
import sys


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

if __name__=="__main__":
    if len(sys.argv)!=2:
        print 'should be:'+sys.argv[0]+' <page num>'
        sys.exit(1)
    con=crawStEz(sys.argv[1])
    procHtml(con)
