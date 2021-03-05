title = input("诗名: ")
writer = input("作者名(默认为支离): ")
body_loc = input("正文文件地址: ")
date = input("创作时间: ")

# 将作者名设为默认支离
if not writer:
    writer = '支离'

# 写入内容
with open("{0}.md".format(title), 'w') as output:
    # 写入背景样式
    output.write("<div style='background: url(background.jpg); background-size: contain; width: 90%; position: absolute'>\n")
    # 写入主题格式
    output.write('<div style="margin: 10%; font-family: sans-serif">\n')
    # 写入作者名
    output.write('<h1 style="text-align: center">{0}</h1>'.format(title))
    # 写入诗的作者
    output.write('<div style="text-align: right; margin: 10%">-{0}</div>\n'.format(writer))
    # 写入诗的正文
    with open(body_loc) as contents:
        body = contents.read()
        output.write('<div style="text-align: center">\n{0}</div>\n'.format(body))
    # 写入作诗的日期
    output.write('<div style="text-align: right; margin: 10%">{0}</div>\n'.format(date))
    # 写入关闭标签
    output.write("</div>\n" * 2)

# 说明写入以完成
print('The progress is finished.')

