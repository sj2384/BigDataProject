#!/usr/bin/env python
import csv
import sys
from utils import get_type
import datetime

reader = csv.reader(sys.stdin)
# Skip first row
next(reader, None)

for entry in reader:
    #if len(entry) == 22:
    RPT_DT = str(entry[5])

    if RPT_DT == '' or RPT_DT is None:
        label = 'NULL'
        RPT_DT = 'NULL'
    else:
        try:
            datetime.datetime.strptime(RPT_DT, '%m/%d/%Y')
            label = 'VALID'
        except ValueError:
            label = 'INVALID'


    print('%s\t%s,date,%s' % (RPT_DT, get_type(RPT_DT), label))
    
