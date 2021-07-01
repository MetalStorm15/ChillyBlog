# The structure of the texts stored in directory is comfined, as following:
# texts_dir/
#   0/
#       name.txt
#       body.txt
#   1/
#       name.txt
#       body.txt
#
# In order to keey files in order, every poem have two files, stored in a separated directory named by sequential numbers, which are 'name.txt', 
# containing the name, and 'body.txt', containing the main body.

import os
import re

def make_sites(texts_dir, model_loc, output, contents):
    """
    texts_dir: the directory where the texts stored.
    model_loc: the location of the file containing the model for the sites showing the poetry.
    output: the directory storing the html files.
    contents: the location of the contents file.

    Note: The '/' at end is necessary.

    This function is used for making the sites showing the powtry.
    """
    poem_numbers = os.listdir(texts_dir)
    for poem_number in poem_numbers:
        with open(texts_dir + poem_number + '/name.txt', encoding='utf-8') as file:
            poem_name = file.read()

        with open(texts_dir + poem_number + '/body.txt', encoding='utf-8') as file:
            poem_body = file.readlines()

        with open(model_loc, encoding='utf-8') as file:
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
            previous = contents
            next = contents
        model = model.replace('the title', poem_name)
        model = model.replace('the body', body)
        model = model.replace('previous', str(previous))
        model = model.replace('next', str(next))

        with open(output + poem_number + '.html', 'w', encoding='utf-8') as file:
            file.write(model)

def make_contents(texts_dir, model_loc, contents):
    """
    texts_dir: the directory where the texts stored.
    model_loc: the file containing the model for the contents.
    output: the contents file made by this function.

    Note: The '/' at end is necessary.

    This function is used for making the contents file.
    """
    file_names = os.listdir(texts_dir)
    files = []
    for f_name in file_names:
        files.append(int(f_name))
    files.sort()
    contents_list = ''
    for file in files:
        with open(texts_dir + str(file) + '/name.txt', encoding='utf-8') as f:
            name = f.read()
            name = name.replace('\n', '')
        contents_list += '<li><a href="{0}/{1}.html">{2}</a></li>\n'.format(output, str(file), name)
    with open(model_loc, encoding='utf-8') as f:
        model = f.read()
    with open(contents, 'w', encoding='utf-8') as f:
        model = model.replace('the list', contents_list)
        f.write(model)


def make(texts_dir, model_1, model_2, output, contents):
    """
    texts_dir: as above.
    model_1: the one for sites.
    model_2: the one for contents.
    output_1: the one for function make_sites().
    output_2: the contents file produced by make_contents() and also the one used in make_sites().

    This is a function to build websites files for poetry.
    """
    make_contents(texts_dir, model_2, contents)
    make_sites(texts_dir, model_1, output, contents)


texts_dir = '/home/chilly/Poet/sources/texts/'
model_1 = '/home/chilly/Poet/sources/models/model1.html'
model_2 = '/home/chilly/Poet/sources/models/model2.html'
output = '/home/chilly/Poet/contents/'
contents = '/home/chilly/Poet/contents/catalogue.html'
make(texts_dir, model_1, model_2, output, contents)
