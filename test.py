#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys
import csv

print sys.version

#open files
boro = 'qn'
amenity1 = 'doorman'
filename1 = './data/%s_%s.csv' % (amenity1,boro)
amenity2 = 'pool'
filename2 = './data/%s_%s.csv' % (amenity2, boro)
amenity3 = 'parking'
filename3 = './data/%s_%s.csv' % (amenity3, boro)
amenity4 = 'laundry'
filename4 = './data/%s_%s.csv' % (amenity4, boro)
amenity5 = 'gym'
filename5 = './data/%s_%s.csv' % (amenity5,boro)
f1 = open(filename1,'r')
reader1 = csv.reader(f1)
f2 = open(filename2,'r')
reader2 = csv.reader(f2)
f3 = open(filename3,'r')
reader3 = csv.reader(f3)
f4 = open(filename4,'r')
reader4 = csv.reader(f4)
f5 = open(filename5,'r')
reader5 = csv.reader(f5)

#open file to write

filenamew = 'output_%s.csv'%boro
# write out in <filename>
writer = csv.writer(open(filenamew, 'w'))
writer.writerow(['bid',amenity1,amenity2,amenity3, amenity4, amenity5,'name', 'address'])
dicttowrite = {}
# print out 5 rows for test
# write each record in reader1 to dictionary
r=0
for row in reader1:
    if row[0] == "bid":
        continue
    row.insert(1, '1')
    row.insert(2, '0')
    row.insert(3, '0')
    row.insert(4, '0')
    row.insert(5, '0')
    dicttowrite[row[0]]=row[1:]
    if r<=5:
        print row[2]
        print dicttowrite
        r+=1
# for each record in reader2: check in already in dict, if exist, change flag for amenity2; if not, add to dict
for row in reader2:
    if row[0] == "bid":
        # if this is header
        continue
    elif row[0] in dicttowrite.keys():
        # if this bid already exists in list
        dicttowrite[row[0]][1]='1'
    else:
        # if this is a new bid for the list
        row.insert(1, '0')
        row.insert(2, '1')
        row.insert(3, '0')
        row.insert(4, '0')
        row.insert(5, '0')
        dicttowrite[row[0]] = row[1:]

# for each record in reader3: check in already in dict, if exist, change flag for amenity3; if not, add to dict
for row in reader3:
    if row[0] == "bid":
        # if this is header
        continue
    elif row[0] in dicttowrite.keys():
        # if this bid already exists in list
        dicttowrite[row[0]][2] = '1'
    else:
        # if this is a new bid for the list
        row.insert(1, '0')
        row.insert(2, '0')
        row.insert(3, '1')
        row.insert(4, '0')
        row.insert(5, '0')
        dicttowrite[row[0]] = row[1:]

# for each record in reader4: check in already in dict, if exist, change flag for amenity4; if not, add to dict
for row in reader4:
    if row[0] == "bid":
        # if this is header
        continue
    elif row[0] in dicttowrite.keys():
        # if this bid already exists in list
        dicttowrite[row[0]][3] = '1'
    else:
        # if this is a new bid for the list
        row.insert(1, '0')
        row.insert(2, '0')
        row.insert(3, '0')
        row.insert(4, '1')
        row.insert(5, '0')
        dicttowrite[row[0]] = row[1:]

# for each record in reader5: check in already in dict, if exist, change flag for amenity5; if not, add to dict
for row in reader5:
    if row[0] == "bid":
        # if this is header
        continue
    elif row[0] in dicttowrite.keys():
        # if this bid already exists in list
        dicttowrite[row[0]][4] = '1'
    else:
        # if this is a new bid for the list
        row.insert(1, '0')
        row.insert(2, '0')
        row.insert(3, '0')
        row.insert(4, '0')
        row.insert(5, '1')
        dicttowrite[row[0]] = row[1:]
# write dictionary to csv file
for key, value in dicttowrite.iteritems():
    # if address is not empty and starts with 'At ', then remove at
    if value[6].startswith('At'):
        value[6]=value[6][3:]
    # if address is empty, assume name is address, copy name
    elif value[6]=='':
        value[6]=value[5]
        # print value[6]
    temp = value
    temp.insert(0,key)
    writer.writerow(temp)
