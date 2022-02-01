# 文件存储方式如下：
# texts_dir/
#   0/
#       name.txt
#       body.txt
#   1/
#       name.txt
#       body.txt
#   ...
#
# 每首诗需要两个文件，name.txt和body.txt，分别存储诗的名字和正文，再将这两个文件放到一个文件夹中，
# 将所有的文件夹以从0开始的数字命名统一放到你的text_dir目录中。
from functions import *

# 根据实际情况修改路径
texts = '../resources/texts/'
model_sites = '../resources/models/model-page.html'
model_catalogue = '../resources/models/model-catalogue.html'
output_dir = '../pages/'
catalogue_file = '../index.html'
make(texts, model_sites, model_catalogue, output_dir, catalogue_file)
