import os
import re

def make_sites(poem_number='all'):
    if not poem_number == 'all':
        with open('../contents/{0}/name.txt'.format(poem_number)) as file:
            poem_name = file.read()

        with open('../contents/{0}/body.txt'.format(poem_number)) as file:
            poem_body = file.readline()

        for line in poem_body:
            line = '<p>' + line + '</p>'

        
