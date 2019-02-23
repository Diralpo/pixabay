# -*- coding: UTF-8 -*-

from cookie import *
from methods import savefile
from bs4 import BeautifulSoup

def search(search_data, maxtimes):
    #需要POST的数据
    postdata={
        'q':search_data,
        'hp': '',
        'image_type': 'all',
        'order': '',
        'cat': '',
        'min_width': '',
        'min_height': ''
    }
    #需要给Post数据编码
    postData = urllib.parse.urlencode(postdata)
    new_url = 'https://pixabay.com/zh/photos/?' + postData
    result = savefile.access_and_save( new_url, "{}/result.html".format(postdata['q']) )
    soup = BeautifulSoup(result, 'lxml')
    the_list = soup(class_ = 'item')
    i = 0
    print(maxtimes)
    for res in the_list:
        try:
            url = res.find('img')['src']
            filename = os.path.basename( url)
            print("{:<5}: {}".format(i, filename))
            savefile.access_and_save(url, "{}/{}".format(postdata['q'], filename))
            i = i + 1
            print(i)
        except:
            print("error...")
        if(i == maxtimes):
            break
