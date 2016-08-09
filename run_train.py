#-*- coding: utf-8 -*-

# from os import listdir
# from os.path import isfile, join
# onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]



# import os
#
# for path in os.environ.get('PATH', '').split(':'):
#     a = 0
#     # filepath = os.path.join(path, PROG_NAME)
#     # if os.path.exists(filepath) and not os.path.isdir(filepath):
#     #     return True


from os import walk


mypath = "/home/modu/PycharmProjects/chainer-fast-neuralstyle-master/train2014"

# mypath = os.path.dirname(os.path.abspath(__file__))

# imgFileName = []
imgFolderName = []
for (dirpath, dirnames, filenames) in walk(mypath):

