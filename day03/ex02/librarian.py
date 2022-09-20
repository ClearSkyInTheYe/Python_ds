#!chfederi/bin/python3
import os
import sys

if os.environ['VIRTUAL_ENV'][-8:] != 'chfederi':
    raise Exception('Please set the right environment')
os.system('pip3 install PyTest')
os.system('pip3 install bs4 beautifulsoup4')
os.system('pip freeze')
os.system('pip freeze > requirements.txt')
sys.exit(1)
