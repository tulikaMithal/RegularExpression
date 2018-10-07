# -*- coding: utf-8 -*-
"""
Created on Sat Sep  1 23:40:44 2018

@author: lenovo
"""

#importing packages

import sys
import re
import numpy as np


# reading file content
with open(sys.argv[1], 'r') as content_file:
    content = content_file.read()
    
    
#pattern to be matched
pattern = re.compile(r'(<tr>\s)?<td>\s(<a name=".*"></a>)?<a href=.*>(.*)</a><br />\s(.*)<br />\s(.*<br />\s)?</td>\s<td>(\s)?(<a href=.*>(.*)</a><br />\s)?(\(?.*\)?-?\s?\d\d\d-(.*))?(<br />\s)?(<a href=.*>(Website)</a>(<br />\s)?)?</td>(\s)?(</tr>)?')

matchObj = pattern.findall(content)

#number of matches found
print(len(matchObj))

#opening output file
fo = open(sys.argv[2], "a")

for i in matchObj:
    line = i[2]+" | "+i[3]+" | "+i[7]+" | "+i[9]+"\n"
    fo.write(line)
    

    
    
