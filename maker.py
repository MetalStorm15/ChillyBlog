title = input("The title: ")
writer = input("The writer or poet: ")
body_loc = input("The location of the file of body: ")
date = input("The date you create it(if it's your work): ")
align = input('Text-align(if you did not type, it will be center): ')

if align:
    text_align = align
else:
    text_align = 'center'

with open("{0}.md".format(title), 'w') as output:
    output.write("<div style='background: url(background.jpg); background-size: contain; width: 90%; position: absolute'>\n")
    output.write('<div style="margin: 10%; font-family: sans-serif">\n')
    output.write('<h1 style="text-align: {0}">{1}</h1>'.format(text_align, title))
    output.write('<div style="text-align: right; margin: 10%">-{0}</div>\n'.format(writer))
    with open(body_loc) as contents:
        body = contents.read()
        output.write('<div style="text-align: center">\n{0}</div>\n'.format(body))
    if date:
        output.write('<div style="text-align: right; margin: 10%">{0}</div>\n'.format(date))

    output.write("</div>\n" * 2)

print('The progress is finished.')


