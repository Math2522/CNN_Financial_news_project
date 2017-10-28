


import glob
import os


folders = glob.glob('*')
for folder in folders:
    files = os.listdir(str('C:\\Users\\au483134\\Desktop\\CNN_project\\20061020_20131126_bloomberg_news\\' + folder))
    for file in files:
            print(folder)