AUTHOR = '支离'
SITENAME = '支离的博客'
SITEURL = '.'

PATH = 'content'
OUTPUT_PATH = './output'
TIMEZONE = 'Asia/Shanghai'
DEFAULT_LANG = 'Chinese (Simplified)'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('支离的诗歌网站', 'https://MetalStorm15.github.io/ChillyPoetry/'),)

# Social widget
SOCIAL = (('知乎：支离-Chilly', 'https://www.zhihu.com/people/jin-shu-feng-bao-56'),
          ('微博：支离-Chilly', 'https://m.weibo.cn/u/7418468313?uid=7418468313&t=0&luicode=10000011&lfid=100103type%3D1%26q%3D%E6%94%AF%E7%A6%BB-Chilly'),)

DEFAULT_PAGINATION = 20

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

THEME = './pelican-theme/backdrop'
PAGINATED_DIRECT_TEMPLATES = ('categories', 'archives')
EMAIL = 'metalstorm15@163.com'
BACKDROP_IMAGE = "/images/bg.jpg"
