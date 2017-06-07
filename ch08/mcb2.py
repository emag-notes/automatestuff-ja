#!/usr/bin/env python
# mcb.py - クリップボードのテキストを保存・復元

import pyperclip
import shelve
import sys

sub_commands = ['save', 'list', 'delete', 'deleteall']


def save(keyword, shelf):
    shelf[keyword] = pyperclip.paste()


def copy(keyword, shelf):
    pyperclip.copy(shelf[keyword])


def listing(shelf):
    pyperclip.copy(str(list(shelf.keys())))


def delete(keyword, shelf):
    del shelf[keyword]


def delete_all(shelf):
    for keyword in shelf:
        del shelf[keyword]


def parse_args():
    sub_command = ''
    keyword = ''

    if sys.argv[1] in sub_commands:
        sub_command = sys.argv[1]
        if sub_command == 'save' or sub_command == 'delete':
            try:
                keyword = sys.argv[2]
            except IndexError:
                usage()
                sys.exit(1)
    else:
        keyword = sys.argv[1]

    return sub_command, keyword


def usage():
    message = '''Usage:
    ./mcb.py save <keyword>   - クリップボードをキーワードに紐づけて保存
    ./mcb.py <keyword>        - キーワードに紐付けられたテキストをクリップボードにコピー
    ./mcb.py list             - 全キーワードをクリップボードにコピー
    ./mcb.py delete <keyword> - キーワードを削除
    ./mcb.py deleteall        - 全キーワードを削除
    '''
    print(message)


if len(sys.argv) < 2:
    usage()
    sys.exit(1)

sub_command, keyword = parse_args()

mcb_shelf = shelve.open('mcb')

# 'save', 'list', 'delete', 'deleteall'
if sub_command == 'save':
    save(keyword, mcb_shelf)
elif sub_command == 'list':
    listing(mcb_shelf)
elif sub_command == 'delete':
    delete(keyword, mcb_shelf)
elif sub_command == 'deleteall':
    delete_all(mcb_shelf)
elif sub_command == '':
    copy(keyword, mcb_shelf)

mcb_shelf.close()
