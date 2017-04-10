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
    CMPLNT_TO_DT = str(entry[3])

    if CMPLNT_TO_DT == '' or CMPLNT_TO_DT is None:
        label = 'NULL'
        CMPLNT_TO_DT = 'NULL'
    else:
        try:
            datetime.datetime.strptime(CMPLNT_TO_DT, '%m/%d/%Y')
            label = 'VALID'
        except ValueError:
            label = 'INVALID'


    print('%s\t%s,date,%s' % (CMPLNT_TO_DT, get_type(CMPLNT_TO_DT), label))
    
