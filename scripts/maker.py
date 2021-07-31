# The structure of the texts stored in directory is comfined, as following:
# texts_dir/
#   0/
#       name.txt
#       body.txt
#   1/
#       name.txt
#       body.txt
#
# In order to keey files in order, every poem have two files, stored in a separated
# directory named by sequential numbers, which are 'name.txt',
# containing the name, and 'body.txt', containing the main body.

import os


def make_sites(texts_dir, model_loc, output, catalogue):
    """
    texts_dir: the directory where the texts stored.
    model_loc: the location of the file containing the model for the sites showing the poetry.
    output: the directory storing the html files.
    catalogue_file: the location of the catalogue_file file.

    Note: The '/' at end is necessary.

    This function is used for making the sites showing the powtry.
    """

    # 获取文件名
    poems = os.listdir(texts_dir)

    # 制作网页文件
    for poem in poems:
        # 读取诗名
        with open(texts_dir + poem + '/name.txt', encoding='utf-8') as file:
            poem_name = file.read()

        # 读取诗的正文
        with open(texts_dir + poem + '/body.txt', encoding='utf-8') as file:
            poem_body = file.readlines()

        # 读取模板文件
        with open(model_loc, encoding='utf-8') as file:
            model = file.read()

        body = ''

        # 制作诗词正文字符串
        for line in poem_body:
            if not line == '\n':
                line = '\t\t<p>' + line[:-1] + '</p>\n'
                body += line

        # 获取跳转所需的链接
        if poem == '0':
            previous_page = catalogue
            n = int(poem) + 1
            next_page = str(n) + '.html'
        elif int(poem) == len(poems) - 1:
            p = int(poem) - 1
            next_page = catalogue
            previous_page = str(p) + '.html'
        else:
            p = int(poem) - 1
            n = int(poem) + 1
            next_page = str(n) + '.html'
            previous_page = str(p) + '.html'

        # 填充模板，制作网页文件
        model = model.replace('the title', poem_name)
        model = model.replace('the body', body)
        model = model.replace('the previous', previous_page)
        model = model.replace('the next', next_page)
        model = model.replace('the catalogue', catalogue)

        # 写入内容
        with open(output + poem + '.html', 'w', encoding='utf-8') as file:
            file.write(model)


def make_catalogue(texts_dir, model_loc, catalogue):
    """
    texts_dir: the directory where the texts stored.
    model_loc: the file containing the model for the contents.
    output: the catalogue_file file made by this function.

    Note: The '/' at end is necessary.

    This function is used for making the contents file.
    """

    # 读取文件夹名
    file_names = os.listdir(texts_dir)
    files = []

    # 将字符串文件名转为整数格式
    for f_name in file_names:
        files.append(int(f_name))

    # 重新排序
    files.sort()
    contents_list = ''

    # 制作目录
    for file in files:
        with open(texts_dir + str(file) + '/name.txt', encoding='utf-8') as f:
            name = f.read()
            name = name.replace('\n', '')
            
        contents_list += '\t\t\t<li><a href="./{0}.html">{1}</a></li>\n'.format(str(file), name)

    # 读取模板
    with open(model_loc, encoding='utf-8') as f:
        model = f.read()

    # 写入填充后的模板
    with open(catalogue, 'w', encoding='utf-8') as f:
        model = model.replace('the list', contents_list)
        f.write(model)


def make_md(texts_dir, output='../Poetry.md'):
    """
    texts_dir: the directory containing all you texts.
    output: the file produced.

    To create a markdown file which contains all the contents of the poetry.
    """

    # 读取文件夹
    poems = os.listdir(texts_dir)
    poem_numbers = []

    # 文件名转换为数字格式
    for poem in poems:
        poem_numbers.append(int(poem))

    # 重新排序
    poem_numbers.sort()
    poems_n = []

    # 转回字符串格式
    for poem_number in poem_numbers:
        poems_n.append(str(poem_number))

    poems = poems_n[:]

    # 写入诗词正文
    with open(output, 'w', encoding='utf-8') as f:
        # 写入大标题
        f.write('# Poetry\n\n')
        # 写入目录
        for poem in poems:
            # 读取诗名
            with open(texts_dir + poem + '/name.txt', encoding='utf-8') as file:
                poem_name = file.read()
            
            # Markdown目录索引
            index = poem_name.replace('（', '')
            index = index.replace('）', '')

            # 写入目录
            f.write('+ [{0}](#{1})\n'.format(poem_name, index))

        f.write('\n')

        # 写入诗词正文
        for poem in poems:
            # 读取诗名
            with open(texts_dir + poem + '/name.txt', encoding='utf-8') as file:
                poem_name = file.read()

            # 写入诗名
            f.write('## {0} \n\n'.format(poem_name))

            # 读取诗正文
            with open(texts_dir + poem + '/body.txt', encoding='utf-8') as file:
                poem_body = file.readlines()

            # 写入诗正文
            for line in poem_body:
                f.write('{0}\n'.format(line))

            # 写入分隔符
            f.write('\n-----\n\n')


def make(texts_dir, model_1, model_2, output, catalogue, md_file='../Poetry.md'):
    """
    texts_dir: the directory containing all you texts.
    model_1: the model for sites.
    model_2: the model for catalogue_file.
    output: the directory containing all the produced files.
    md_file: the markdown file containing all the poetry.
    catalogue_file: the catalogue_file file produced by make_contents() and also the one used in make_sites().

    Note: the catalogue_file file must in the output directory.

    This is a function to build websites files for poetry.
    """
    # 制作目录文件
    make_catalogue(texts_dir, model_2, catalogue)
    # 制作网页文件
    make_sites(texts_dir, model_1, output, catalogue)
    # 制作Markdown文件
    make_md(texts_dir, md_file)


# change the path below based on the real environments
texts = '../resources/texts/'
model_sites = '../resources/models/model1.html'
model_catalogue = '../resources/models/model2.html'
output_dir = '../contents/'
catalogue_file = '../contents/catalogue.html'
make(texts, model_sites, model_catalogue, output_dir, catalogue_file)
