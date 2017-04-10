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
    CMPLNT_FR_DT = str(entry[1])

    if CMPLNT_FR_DT == '' or CMPLNT_FR_DT is None:
        label = 'NULL'
        CMPLNT_FR_DT = 'NULL'
    else:
        try:
            datetime.datetime.strptime(CMPLNT_FR_DT, '%m/%d/%Y')
            label = 'VALID'
        except ValueError:
            label = 'INVALID'


    print('%s\t%s,date,%s' % (CMPLNT_FR_DT, get_type(CMPLNT_FR_DT), label))
    
