#!/usr/bin/python
import os, sys, shutil, zipfile, urllib2
from shutil import copyfile
from stat import *
from os.path import join

### Update files with user's avd path
#
def updatefile(source):
	f1 = open(source, 'r')
	f2 = open(source + '.update', 'w')
	for line in f1:
		f2.write(line.replace('%%AVD_PATH%%', avd))
	f2.close()
	f1.close()
	shutil.move(source + '.update', source)

### Download ZIP from CDN
#
def download(host, file_name):
    if (os.path.isfile('./' + file_name)):
        print "File already downloaded: %s" % file_name
        return
    url = host + "" + file_name
    print url
    u = urllib2.urlopen(url)
    f = open(file_name, 'wb')
    meta = u.info()
    file_size = int(meta.getheaders("Content-Length")[0])
    print "Downloading: %s Bytes: %s" % (file_name, file_size)

    file_size_dl = 0
    block_sz = 8192
    while True:
        buffer = u.read(block_sz)
        if not buffer:
            break

        file_size_dl += len(buffer)
        f.write(buffer)
        status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
        status = status + chr(8)*(len(status)+1)
        print status,

    f.close()

def unzip(file_name):
    zf = zipfile.ZipFile('./' + file_name)
    
    zf.extract('userdata.img', './Poynt_Emulator_1_2_11.avd')
    zf.extract('sdcard.img', './Poynt_Emulator_1_2_11.avd')

### Main
#
avd = raw_input("\nEnter full path of your `avd` directory: ")
avd = avd.replace('\\','/')
if not (os.path.isdir(avd)):
    print "\nSorry, but `",avd,"` is not a valid directory.\n"
    sys.exit(0)

avd = avd.rstrip('/')

#http://d1su11fsq8j9e7.cloudfront.net/poyntos_1_2_11_avd_img.zip
# Download and unzip
download('http://d1su11fsq8j9e7.cloudfront.net/','poyntos_1_2_11_avd_img.zip')
unzip('poyntos_1_2_11_avd_img.zip')

# Copy files to destination directory
print("\nCopying PoyntOS Emulator image to avd directory...")
shutil.copy('./Poynt_Emulator_1_2_11.ini', avd + '/')
shutil.copytree('./Poynt_Emulator_1_2_11.avd', avd + '/Poynt_Emulator_1_2_11.avd')

# Update the .ini/.xml files
os.chdir(avd)
updatefile("./Poynt_Emulator_1_2_11.ini")
os.chdir(avd + '/Poynt_Emulator_1_2_11.avd')
updatefile("./config.ini")
updatefile("./poynt_hardware.xml")

print("\nCompleted. You can now launch the PoyntOS emulator device in avd.\n\n")
