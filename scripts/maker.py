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

def make_sites(texts_dir, model_loc, output, catalogue):
    """
    texts_dir: the directory where the texts stored.
    model_loc: the location of the file containing the model for the sites showing the poetry.
    output: the directory storing the html files.
    catalogue: the location of the catalogue file.

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

        if poem_number == '0':
            previous = catalogue
            n = int(poem_number) + 1
            next = str(n) + '.html'
        elif int(poem_number) == len(poem_numbers) - 1:
            p = int(poem_number) - 1
            next = catalogue
            previous = str(p) + '.html'
        else:
            p = int(poem_number) - 1
            n = int(poem_number) + 1
            next = str(n) + '.html'
            previous = str(p) + '.html'

        model = model.replace('the title', poem_name)
        model = model.replace('the body', body)
        model = model.replace('the previous', previous)
        model = model.replace('the next', next)
        model = model.replace('the catalogue', catalogue)

        with open(output + poem_number + '.html', 'w', encoding='utf-8') as file:
            file.write(model)

def make_catalogue(texts_dir, model_loc, catalogue):
    """
    texts_dir: the directory where the texts stored.
    model_loc: the file containing the model for the contents.
    output: the catalogue file made by this function.

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
        contents_list += '<li><a href="./{0}.html">{1}</a></li>\n'.format(str(file), name)
    with open(model_loc, encoding='utf-8') as f:
        model = f.read()
    with open(catalogue, 'w', encoding='utf-8') as f:
        model = model.replace('the list', contents_list)
        f.write(model)


def make(texts_dir, model_1, model_2, output, catalogue):
    """
    texts_dir: the directory containing all you texts.
    model_1: the model for sites.
    model_2: the model for catalogue.
    output: the directory containing all the produced files.
    catalogue: the catalogue file produced by make_contents() and also the one used in make_sites().

    Note: the catalogue file must in the output directory.

    This is a function to build websites files for poetry.
    """
    make_catalogue(texts_dir, model_2, catalogue)
    make_sites(texts_dir, model_1, output, catalogue)


# change the path below based on the real environments
texts_dir = '../resources/texts/'
model_1 = '../resources/models/model1.html'
model_2 = '../resources/models/model2.html'
output = '../contents/'
catalogue = '../contents/catalogue.html'
make(texts_dir, model_1, model_2, output, catalogue)
