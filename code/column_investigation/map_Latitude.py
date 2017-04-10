#!/usr/bin/env python
import csv
import sys
from utils import get_type

reader = csv.reader(sys.stdin)
# Skip first row
next(reader, None)
#valid_list = ['BRONX','BROOKLYN','MANHATTAN','QUEENS','STATEN ISLAND']
for entry in reader:
    #if len(entry) == 22:
    Latitude = str(entry[21])
    if Latitude == '' or Latitude is None:#in valid_list:
        label = 'NULL'
        Latitude = 'NULL'
    else:
        label = 'VALID'
    print('%s\t%s,latitude,%s' % (Latitude, get_type(Latitude), label))
    
