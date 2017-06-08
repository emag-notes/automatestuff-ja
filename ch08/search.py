#!/usr/bin/env python
# search.py - *.txt 内のキーワード検索

import os
import re
import sys

if len(sys.argv) < 3:
    print('Please specify target dir and keyword.')
    sys.exit(1)

target_dir_name = sys.argv[1]
target_dir = os.listdir(target_dir_name)
pattern = sys.argv[2]

for each_file in target_dir:
    if each_file.endswith('.txt'):
        content_file = open(os.path.join(target_dir_name, each_file))
        content = content_file.read()
        content_file.close()
        regex = re.compile(pattern, re.IGNORECASE)
        results = regex.findall(content)
        if len(results) != 0:
            print('###', each_file)
            for result in results:
                print(result)
            print()
        else:
            print('no results in ' + each_file)

