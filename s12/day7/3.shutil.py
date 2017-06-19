#!/usr/bin/env python
#coding:utf8
"""
import shutil
#copy file
shutil.copyfileobj(open('old.xml','r'), open('new.xml', 'w'))
shutil.copyfile('f1.log', 'f2.log')
#仅拷贝权限
shutil.copymode('f1.log','f2.log')
#仅拷贝状态的信息，包括：mode bits, atime, mtime, flags
shutil.copystat('f1.log','f2.log')
#copy 文件和权限
shutil.copy()
#copy 文件和状态
shutil.copy2()
#copy文件夹    symlinks=false
shutil.copytree('folder1', 'folder2', ignore=shutil.ignore_patterns('*.pyc', 'tmp*'))
#递归删除
shutil.rmtree('folder1')
#move
shutil.move('folder1', 'folder3')
#压缩www.gztar
ret = shutil.make_archive("www", 'gztar', root_dir='/Users/wupeiqi/Downloads/test')
#压缩www.gztar指定目录
ret = shutil.make_archive("/Users/wupeiqi/www", 'gztar', root_dir='/Users/wupeiqi/Downloads/test')



#zipfile
import zipfile
#压缩
z=zipfile.ZipFile('temp.zip','a')   #a追加,w
z.write('xo2.xml')
z.close()

#解压
z=zipfile.ZipFile('temp.zip','r')
z.extractall()
for item in z.namelist():
    print(item)
#z.extract('xo1.xml')
z.close()
"""
import tarfile
"""
tar = tarfile.open('your.tar','w')
tar.add('xo1.xml', arcname='x1.log')
tar.add('xo2.xml', arcname='x2.log')
tar.close()
"""
tar = tarfile.open('your.tar','r')
#tar.extractall()
obj=tar.getmember('x1.log')
tar.extract(obj)
tar.close()



