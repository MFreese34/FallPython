# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 20:13:20 2019

@author: Milo
"""

import json

# simplest example of encoding python objects in JSON and writing to file
file = open('samplewrite.txt', 'w')
file.write(json.dumps({'student_count': 12, 'teacher_count': 1}))
file.close()

jso = json.loads('{"numbers": [33, 55, 66]}')
print(jso)
