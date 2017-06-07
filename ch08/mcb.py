#!/usr/bin/env python
# mcb.py - クリップボードのテキストを保存・復元
# Usage:
# ./mcb.py save <keyword> - クリップボードをキーワードに紐づけて保存
# ./mcb.py <keyword> - キーワードに紐付けられたテキストをクリップボードにコピー
# ./mcb.py list - 全キーワードをクリップボードにコピー

import pyperclip
import shelve
import sys

mcb_shelf = shelve.open('mcb')

# クリップボードの内容を保存
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcb_shelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
    # キーワード一覧と、内容の読み込み
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcb_shelf.keys())))
    elif sys.argv[1] in mcb_shelf:
        pyperclip.copy(mcb_shelf[sys.argv[1]])

mcb_shelf.close()
