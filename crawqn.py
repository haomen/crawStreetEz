#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib
import urllib2
import sys
import time
import csv



def crawStEz(amenity,boro,page_num):
    #query on <amenity> for all buildings in nyc from strEz web
    url='http://www.streeteasy.com/buildings/%s/building_amenities:%s?page=%s'%(boro,amenity,page_num)
    #http://streeteasy.com/buildings/nyc/building_amenities:parking%7Carea:119,139,144,135,101
    print 'url: %s'%url
    req=urllib2.Request(url)
    response=urllib2.urlopen(req)
    print 'page '+page_num+' crawled, processing string now...'
    return  response.read()



def runforsix(amenity,boro):
    # run crawStEz and parse for the amenity specified
    #amenity = sys.argv[1]
    print 'processing amenity: %s'%amenity
    filename = '%s_%s.csv'%(amenity,boro)
    # write out in <filename>
    writer = csv.writer(open(filename, 'w'))
    writer.writerow(['bid','name', 'address']) 
    def procHtml(con):
        #parse results from query and save name, address to file
        buildings=con.split('<div id="building')[1:]
        for bd in buildings:
            bid = bd.split('"')[0].split('_')[1]
            name=bd.split('se:clickable:target="true">')[-1].split('</a>')[0].rstrip()
            address=bd.split('<div class=\'closer\'>')[0].split('</div>')[-1].lstrip().rstrip()
            print "bid:"+bid+"name:"+name+"\taddress:"+address
            writer.writerow([bid,name,address])
        if '<span class="next">' in con:
            nextpage = con.split('<span class="next">')[-1].split('" rel="next">')[0].split('page=')[1]
            #sentence = con.split('<span class="next">')[-1].split('<div id="searchModal"')[0]
            #return sentence
            return nextpage
        else:
            return 'last page'
    
    con = crawStEz(amenity,boro,'1')
    nextpageN = procHtml(con)
    p = 1
    t = 0
    while nextpageN != 'last page':
    #while nextpageN != 3:
        con = crawStEz(amenity, boro, nextpageN)
        nextpageN = procHtml(con)
        time.sleep(120)
        p=+1
        if p % 10 ==0:
            time.sleep(240+(t//2)*30)
            t=+1

if __name__=="__main__":

    if len(sys.argv)!=3:
        print 'should be:'+sys.argv[0]+' <boro: manhattan, bronx, brooklyn, queens,statenisland> <amenity: leed_registration, doorman, gym, laundry, pool, parking>'
        sys.exit(1)
    if sys.argv[1] in ('leed_registration', 'doorman', 'gym', 'laundry', 'pool', 'parking'):
        amenity = sys.argv[1]
        runforsix(amenity, boro)
    elif sys.argv[1] == 'all':
        #runforsix('leed_registration')
        runforsix('gym',boro)

        runforsix('pool',boro)
        runforsix('parking',boro)
        runforsix('laundry',boro)
        runforsix('doorman',boro)
    else:
        print 'should be:'+sys.argv[0]+' <amenity: all, or leed_registration, doorman, gym, laundry, pool, parking>'
        


