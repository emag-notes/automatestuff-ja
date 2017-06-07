#!/usr/bin/env python
# textGenerator.py - 作文ジェネレータ

import os
import re
import sys

if len(sys.argv) < 2:
    print('Please specify a file.')
    sys.exit(1)

original_file = open(sys.argv[1])
original_content = original_file.read()
original_file.close()

generated_file_dir = 'textGenerator'
if not os.path.exists(generated_file_dir):
    os.makedirs(generated_file_dir)

keywords = ['ADJECTIVE', 'NOUN', 'ADVERB', 'VERB']
generated_content = original_content

adjective_regex = re.compile(r'ADJECTIVE')
noun_regex = re.compile(r'NOUN')
adverb_regex = re.compile(r'ADVERB')
verb_regex = re.compile(r'VERB')

for word in original_content.split():
    word = word.strip(',.')
    if word in keywords:
        if word == 'ADJECTIVE':
            print('Enter an adjective:')
            adjective = input()
            generated_content = adjective_regex.sub(adjective, generated_content, 1)
        elif word == 'NOUN':
            print('Enter an none:')
            noun = input()
            generated_content = noun_regex.sub(noun, generated_content, 1)
        elif word == 'ADVERB':
            print('Enter an adverb:')
            adverb = input()
            generated_content = adverb_regex.sub(adverb, generated_content, 1)
        elif word == 'VERB':
            print('Enter an verb:')
            verb = input()
            generated_content = verb_regex.sub(verb, generated_content, 1)

generated_file_name = os.path.join(generated_file_dir, 'generated.txt')
generated_file = open(generated_file_name, 'w')
generated_file.write(generated_content)
generated_file.close()

