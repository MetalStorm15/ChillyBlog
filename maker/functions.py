import os


def make_sites(texts_dir: str, model_loc: str, output: str, contents_list: str):
    """此函数用于制作各个诗歌的网页

    Args:
        texts_dir (str): 诗歌源文件目录
        model_loc (str): 诗歌网页模板
        output (str): 诗歌网页输出目录
        contents_list (str): 目录字符串
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
                line = ' ' * 28 + '<p>' + line[:-1] + '</p>\n'
                body += line

        catalogue = '#catalogue'
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
        model = model.replace('the contents', contents_list)

        # 写入内容
        with open(output + poem + '.html', 'w', encoding='utf-8') as file:
            file.write(model)


def make_catalogue(texts_dir: str, model_loc: str, catalogue: str):
    """"本函数用于制作首页网页

    Args:
        texts_dir (str): 诗歌源文件目录
        model_loc (str): 首页模板目录
        catalogue (str): 要制作首页文件名

    Returns:
        [str]: 目录字符, 用于插入其他文档
    """
    # 读取文件夹名
    file_names = os.listdir(texts_dir)
    files = []

    # 将字符串文件名转为整数格式
    for f_name in file_names:
        files.append(int(f_name))

    # 重新排序
    files.sort()
    contents_list = '<ol>'
    contents_list_page = '<ol>'

    # 制作目录
    for file in files:
        with open(texts_dir + str(file) + '/name.txt', encoding='utf-8') as f:
            name = f.read()
            name = name.replace('\n', '')

        contents_list += ' ' * 32 + '<li><a href="./pages/{0}.html">{1}</a></li>\n'.format(str(file), name)
        contents_list_page += ' ' * 32 + '<li><a href="./{0}.html">{1}</a></li>\n'.format(str(file), name)
    contents_list += '</ol<>'
    contents_list_page += '</ol>'
    # 读取模板
    with open(model_loc, encoding='utf-8') as f:
        model = f.read()

    # 写入填充后的模板
    with open(catalogue, mode='w', encoding='utf-8') as f:
        model = model.replace('the contents', contents_list)
        f.write(model)

    return contents_list_page

def make_md(texts_dir: str, output:str):
    """本函数用于制作所有诗歌的汇总文件

    Args:
        texts_dir (str): 诗歌源文件目录
        output (str, optional): 诗歌汇总md文件名.
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
        f.write('<h1 style="text-align: center">支离诗集</h1>\n\n')
        f.write('<h2 style="text-align: center">目录</h2>\n\n')

        # 写入目录
        f.write('<div style="margin-left: 30%">\n\n')
        timer = 1
        for poem in poems:
            # 读取诗名
            with open(texts_dir + poem + '/name.txt', encoding='utf-8') as file:
                poem_name = file.read().replace('/n', '')

            # Markdown目录索引
            index = str(timer)
            timer += 1

            # 写入目录
            f.write('{1}. <a href="#{1}">{0}</a>\n'.format(poem_name, index))

        f.write('\n')
        f.write('</div>')
        f.write('<div style="text-align: center;">\n\n')
        # 写入诗词正文
        timer = 1
        for poem in poems:
            # 读取诗名
            with open(texts_dir + poem + '/name.txt', encoding='utf-8') as file:
                poem_name = file.read()

            # 写入诗名
            f.write('<h2 id="{0}">{1}</h2>\n\n'.format(str(timer), poem_name))
            timer += 1

            # 读取诗正文
            with open(texts_dir + poem + '/body.txt', encoding='utf-8') as file:
                poem_body = file.readlines()

            # 写入诗正文
            for line in poem_body:
                f.write('{0}\n'.format(line))

            # 写入分隔符
            f.write('\n-----\n\n')

        f.write('</div>')


def make_poems(texts_dir: str, output: str):
    """本函数用于制作诗歌的单个文件。

    Args:
        texts_dir (str): 源文件目录
        output (str): 输出的诗歌单文件的存储目录
    """
    poems = os.listdir(texts_dir)
    for poem in poems:
        with open(texts_dir + poem + '/name.txt', encoding='utf-8') as file:
            poem_name = file.read().replace('/n', '')

        with open(texts_dir + poem + '/body.txt', encoding='utf-8') as file:
            poem_body = file.readlines()

        with open(output + '{0}.md'.format(poem_name), 'w', encoding='utf-8') as file:
            file.write('# ' + poem_name + '\n\n')

            for line in poem_body:
                file.write(line + '\n')


def make(texts_dir: str, model_1: str, model_2: str, output: str, index: str, md_file: str, poems_dir: str):
    """
    运行本函数即可完成所有工作的构建。
        
    texts_dir: 文档源文件目录
    model_1: 诗歌网页模板
    model_2: 首页网页模板
    output: 制作完成的网页的目录
    index: 首页网页
    md_file: 总md文件
    poems_dir: 单个诗歌文件目录
    """
    # 制作目录文件
    contents_list = make_catalogue(texts_dir, model_2, index)
    # 制作网页文件
    make_sites(texts_dir, model_1, output, contents_list)
    # 制作Markdown文件
    make_md(texts_dir, md_file)
    make_poems(texts_dir, poems_dir)
