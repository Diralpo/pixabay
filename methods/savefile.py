# -*- coding: UTF-8 -*-
from cookie import *

def access_and_save(access_url, filename, save_bool = 0):
        #自定义一个请求# 先get下 lt
    req = urllib.request.Request(
        access_url
    )
    #访问该链接#
    result = opener.open(req)
    #解码返回的内容#
    file_data=result.read()
    #print(chardet.detect(result))
    if save_bool == 0:
        save_html(file_data, "save/{}".format(filename))

    return file_data

def save_html(file_data, path):
    father_path=os.path.abspath(os.path.dirname(path)+os.path.sep+".")
    isExists=os.path.exists(father_path)
    if not isExists:
        os.makedirs(father_path)
    f = open(path,'wb')
    f.write(file_data)
    f.close()


