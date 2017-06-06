#!/usr/bin/env python
# checkPasswordStrength.py - パスワードの強度チェック。パスワードはクリップボードから得る

import pyperclip
import re


def check_password_strength(password):
    return is_enough_length(password, 8) \
           and has_both_case(password) \
           and has_number(password)


def is_enough_length(password, min_length):
    if len(password) >= min_length:
        return True
    else:
        return False


def has_both_case(password):
    case_regex = re.compile(r'(?=.*?[a-z])(?=.*?[A-Z])[a-zA-Z]')
    mo = case_regex.search(password)
    if mo != None:
        return True
    else:
        return False


def has_number(password):
    number_regex = re.compile(r'[\d]')
    mo = number_regex.search(password)
    if mo != None:
        return True
    else:
        return False


password = str(pyperclip.paste())
result = check_password_strength(password)

if result:
    print('十分な強度のパスワードです')
else:
    print('注意! 脆弱なパスワードです')
