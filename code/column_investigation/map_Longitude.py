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
    Longitude = str(entry[22])
    if Longitude == '' or Longitude is None:#in valid_list:
        label = 'NULL'
        Longitude = 'NULL'
    else:
        label = 'VALID'
    print('%s\t%s,longitude,%s' % (Longitude, get_type(Longitude), label))
    
