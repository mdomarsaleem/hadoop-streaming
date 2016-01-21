#!/usr/bin/env python

import sys
import re
import os
text = sys.stdin.read()
file = os.getenv('map_input_file')
print(os.path.basename(file),text.count('\n'),text.count(' '),len(re.split('\s+', text)),len(text),text.count('\t'),text.count('{'),text.count('('),text.count('class'),text.count('javascript'),text.count('meta content'),text.count('input'),text.count('forum'),text.count('.gif'),text.count('.js'),text.count('.css'),text.count('adblockkey'),text.count('facebook'),text.count('gmail'),text.count('twitter'),text.count('linkedIn'),text.count('subscribe'),text.count('href'),text.count('http'),text.count('<'),text.count('('),len(re.split('\w+', text)),text.count('\n\t'),text.count('//'),text.count('/'),text.count('<!'),text.count('/>'),text.count('&'),text.count(';'),text.count('=='),text.count('==='),text.count('css'),text.count('#'),text.count('@'),text.count('$'),text.count('%'),text.count('^'),text.count('+'),text.count('?'),text.count('|'),text.count('\\'),text.count('*'),text.count('||'),text.count('\t\t'),text.count('\t\t\t'))

