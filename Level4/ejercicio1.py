# Write a Python regex function to find sequences of lowercase letters joined with an underscore.

str = 'a-b-c123456789a-b-c1236123465aad_eeee1232134565aaa_bbfff125444i_iii123456'

"""
import re

pattern = "[a-z]+_[a-z]+"

result1 = re.search(pattern, str)
print("result1: ",result1)

result3 = re.findall(pattern, str, flags=0)
print(result3)
"""

import re

def match_pattern(pattern, str):
    return re.findall(pattern, str, flags=0)

pattern = "[a-z]+_[a-z]+"
str = 'a-b-c123456789a-b-c1236123465aad_eeee1232134565aaa_bbfff125444i_iii123456'

print("result: ", match_pattern(pattern,str))



