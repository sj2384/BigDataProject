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
    Lat_Lon = str(entry[23])
    if Lat_Lon == '' or Lat_Lon is None:#in valid_list:
        label = 'NULL'
        Lat_Lon = 'NULL'
    else:
        label = 'VALID'
    print('%s\t%s,coordinate,%s' % (Lat_Lon, get_type(Lat_Lon), label))
    
