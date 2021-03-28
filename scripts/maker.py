import os
import re

def make_sites(poem_numbers='all'):
    if poem_numbers == 'all':
        poem_numbers = os.listdir('../contents')
    
    for poem_number in poem_numbers:
        with open('../contents/{0}/name.txt'.format(poem_number)) as file:
            poem_name = file.read()

        with open('../contents/{0}/body.txt'.format(poem_number)) as file:
            poem_body = file.readlines()

        with open('model1.txt') as file:
            model = file.read()
        
        model = re.split('split', model)
        
        with open ('../{0}.html'.format(poem_number), 'w') as file:
            file.write(model[0])
            file.write(poem_name)
            file.write(model[1])
            file.write(poem_name)
            file.write(model[2])
            for line in poem_body:
                if not line == '\n':
                    line = '<p>\n' + line + '</p>\n'
                    file.write(line)
            file.write(model[3])

