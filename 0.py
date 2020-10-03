# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 23:38:02 2020

@author: D. Ogulcan CELIK
"""

import xlrd
import addevent
   
loc = ("0.xlsx") 
  
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0)

for i in range (62):
    dates = sheet.cell_value(i+1, 0)
    times0 = sheet.cell_value(i+1, 1)
    times1 = sheet.cell_value(i+1, 2)
    main_time = dates + "T" + times0 + ":00-" + times1
    name = sheet.cell_value(i+1, 3)
    courser = sheet.cell_value(i+1, 4)
    addevent.event(name, main_time, courser)
    
    