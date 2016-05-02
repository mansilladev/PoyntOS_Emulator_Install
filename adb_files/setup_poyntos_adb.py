#!/usr/bin/python
import urllib2
import os
import json
from subprocess import call
import sys

index_url = "https://s3-us-west-1.amazonaws.com/poynt-apks/v1.2.11/"
index_file = "download.json"

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


#download the index file
download(index_url, index_file)

#parse the json
json_data=open(index_file)
data = json.load(json_data)
json_data.close()

host = data["host"]

#downnload co.poynt.capability.manager
download( host, data["apps"]["co.poynt.capability.manager"]["apk"])

#download co.poynt.services
download( host, data["apps"]["co.poynt.services"]["apk"])

#download accessory manager
download( host, data["apps"]["co.poynt.accessory"]["apk"])

#download co.poynt.terminal
download( host, data["apps"]["co.poynt.terminal"]["apk"])

#download co.poynt.register
download( host, data["apps"]["co.poynt.register"]["apk"])

#download co.poynt.launcher
download( host, data["apps"]["co.poynt.launcher"]["apk"])

#download co.poynt.help
download( host, data["apps"]["co.poynt.help"]["apk"])

#download co.poynt.setupwizard
download( host, data["apps"]["co.poynt.setupwizard"]["apk"])

#download co.poynt.settlements
download( host, data["apps"]["co.poynt.settlements"]["apk"])

#uninstall existing apps
print "\n\n\n Uninstalling existing apps..."
print "\n [NOTE: Some failures are ok to ignore here if a previous version was not found.]\n\n"
print "Launcher:"
try:							      
	call(["adb", "uninstall", "co.poynt.launcher"])	      
except OSError as e:
	print "Error:", e.strerror
	print "*** Please make sure adb is in your PATH variable ***" 
	sys.exit()

print "Register:"
call(["adb", "uninstall", "co.poynt.register"])
print "Terminal:"
call(["adb", "uninstall", "co.poynt.terminal"])
print "OOBE:"
call(["adb", "uninstall", "co.poynt.setupwizard"])
print "Settings:"
call(["adb", "uninstall", "co.poynt.settings"])
print "Services:"
call(["adb", "uninstall", "co.poynt.services"])
print "ContentProviders:"
call(["adb", "uninstall", "co.poynt.contentproviders"])
call(["adb", "uninstall", "co.poynt.os.contentproviders"])
call(["adb", "uninstall", "co.poynt.capability.manager"])
call(["adb", "uninstall", "co.poynt.accessory"])
call(["adb", "uninstall", "co.poynt.help"])
call(["adb", "uninstall", "co.poynt.settlements"])


#install new apps
print "\n\n Installing new apps..."
print "co.poynt.capability.manager: "
call(["adb", "install", data["apps"]["co.poynt.capability.manager"]["apk"]])
print "co.poynt.services: "
call(["adb", "install", data["apps"]["co.poynt.services"]["apk"]])
print "co.poynt.accessory: "
call(["adb", "install", data["apps"]["co.poynt.accessory"]["apk"]])
print "co.poynt.terminal: "
call(["adb", "install", data["apps"]["co.poynt.terminal"]["apk"]])
print "co.poynt.register: "
call(["adb", "install", data["apps"]["co.poynt.register"]["apk"]])
print "co.poynt.launcher: "
call(["adb", "install", data["apps"]["co.poynt.launcher"]["apk"]])
print "co.poynt.help: "
call(["adb", "install", data["apps"]["co.poynt.help"]["apk"]])
print "co.poynt.setupwizard: "
call(["adb", "install", data["apps"]["co.poynt.setupwizard"]["apk"]])
print "co.poynt.settlements: "
call(["adb", "install", data["apps"]["co.poynt.settlements"]["apk"]])

#launch the PoyntLauncher
print "\n\n *** install complete***"
print "\n\n NOTE: If you haven't activated your device before, select \"Setup Wizard\" option in the dialog. If you've already activated before, just select \"PoyntLauncher\" to continue."
call(["adb", "shell", "am start -c android.intent.category.HOME -a android.intent.action.MAIN"])
