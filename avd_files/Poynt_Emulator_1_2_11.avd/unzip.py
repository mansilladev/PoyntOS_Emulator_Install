import zipfile,os.path

zf = zipfile.ZipFile('./userdata.img.zip')
zf.extract('userdata.img', './neil.img')
