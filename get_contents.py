import os
import re

for file in os.listdir('.'):
    if file == 'contents':
        os.system('rm -rf contents')

all_files = os.listdir('./')
files = []
for file_name in all_files:
    if os.path.splitext(file_name)[1] == '.md':
        if not file_name == 'README.md':
            files.append(file_name)

name = re.compile(r'<h1.*?>(.*?)</h1>')
body = re.compile(r'<div style="text-align: center">(.*?)</div>', re.S)

number = 0

os.system('mkdir contents')

for f in files:
    with open(f, 'r') as file:
        contents = file.read()
        n = name.search(contents).group(1)
        b = body.search(contents).group(1)

    if number < 10:
        name_num = '00' + str(number)
    if number >= 10 and number < 100:
        name_num = '0' + str(number)
    if number >= 100:
        name_num = number

    os.system('mkdir contents/{0}'.format(name_num))

    with open('contents/{0}/name.txt'.format(name_num), 'w') as file:
        file.write(n)

    with open('contents/{0}/body.txt'.format(name_num), 'w') as file:
        file.write(b)

    os.system('cd ..')

    number += 1

