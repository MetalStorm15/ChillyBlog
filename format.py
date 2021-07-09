import os

numbers = list(range(19, 38))
numbers.sort(reverse=True)
for number in numbers:
    num = str(number)
    num_new = str(number + 2)
    dir = './resources/texts/'
    os.system('mv {0} {1}'.format(dir + num, dir + num_new))

