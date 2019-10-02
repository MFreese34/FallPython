# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 19:29:24 2019

@author: Milo
"""

# Does the racial make up of the acj reflect the make up of AC at large on 6/19
import csv

ACJ_file = open ('jail_june_2019.csv', newline='')
reader = csv.DictReader(ACJ_file)
blk_total = 0
wht_total = 0
census_date = '6/27/2019'

# iterating over rows with these keys
# Date,Gender,Race,Age at Booking,Current Age
for row in reader:
    if row['Date'] == census_date:
        if row['Race'] == 'B':
            blk_total = blk_total + 1
        elif row['Race'] == 'W':
            wht_total = wht_total + 1
ACJ_file.close()

print('Total white count June 1' + str(wht_total))
perc_white = wht_total / (wht_total + blk_total)
print('White percent: ' + str(perc_white))
print('Total Black count on June 1' + str(blk_total))
perc_black = blk_total / (wht_total + blk_total)
print('White percent: ' + str(perc_black))