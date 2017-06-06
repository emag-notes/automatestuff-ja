#!/usr/bin/env python
# myStrip.py - おれおれ strip()

import re


def my_strip(text, chars=None):
    if chars == None:
        strip_regex = re.compile(r'^\s+|\s+$')
        return strip_regex.sub('', text)
    else:
        # like '^[ABC]+|[ABC]+$'
        strip_regex = re.compile('^[' + chars + ']+|[' + chars + ']+$')
        return strip_regex.sub('', text)


result1 = my_strip('   as df ')
print(result1) # => 'as df

result2 = my_strip('ABC as df CBA', 'ABC')
print(result2) # => ' as df '
