import os
import re

def make_sites():
    poem_numbers = os.listdir('../texts')
    for poem_number in poem_numbers:
        with open('../texts/{0}/name.txt'.format(poem_number), encoding='utf-8') as file:
            poem_name = file.read()

        with open('../texts/{0}/body.txt'.format(poem_number), encoding='utf-8') as file:
            poem_body = file.readlines()

        with open('../scripts/model1.html', encoding='utf-8') as file:
            model = file.read()
        body = ''
        for line in poem_body:
                if not line == '\n':
                    line = '<p>\n' + line + '</p>\n'
                    body += line
        if not poem_number == '0' and not int(poem_number) == len(poem_numbers) - 1:
            previous = int(poem_number) - 1
            next = int(poem_number) + 1
        else:
            previous = './contents.html'
            next = './contents.html'
        model = model.replace('the title', poem_name)
        model = model.replace('the body', body)
        model = model.replace('previous', str(previous))
        model = model.replace('next', str(next))

        with open('./{0}.html'.format(poem_number), 'w', encoding='utf-8') as file:
            file.write(model)

def make_contents():
    file_names = os.listdir('../texts')
    files = []
    for f_name in file_names:
        files.append(int(f_name))
    files.sort()
    contents = ''
    for file in files:
        with open('../texts/{0}/name.txt'.format(str(file)), encoding='utf-8') as f:
            name = f.read()
            name = name.replace('\n', '')
        contents += '<li><a href="./{0}.html">{1}</a></li>\n'.format(str(file), name)
    with open('../scripts/model2.html', encoding='utf-8') as f:
        model = f.read()
    with open('./contents.html', 'w', encoding='utf-8') as f:
        model = model.replace('the list', contents)
        f.write(model)


make_sites()
make_contents()

