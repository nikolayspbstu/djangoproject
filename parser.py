import bs4
from bs4 import BeautifulSoup
import requests
import lxml

def lower_func(string):
    list = string.split(' ')
    list[0]= list[0].lower()
    element=list[0]
    up_word= element[0].upper()
    advanced_element=element.replace(element[0],up_word)
    list[0]=advanced_element
    name=" ".join(list)
    return name


def collect():
    url='https://aero.spbstu.ru/about/lectors'
    req=requests.get(url)
    url_image='url_image'
    names = 'name'
    text_profile='text_profile'
    dictionary={
        url_image: None,
        names: None,
        text_profile:None,
    }
    src=BeautifulSoup(req.text,'lxml')
    main_list = src.find_all('table',class_='category table table-striped table-bordered table-hover')
    td_tegs=[]
    for item in main_list:
        td_tegs=td_tegs+item.find_all('td')
    a=len(td_tegs)
    dict_list=[]

    for item in td_tegs:
        if item.find('img'):
            dictionary[url_image]=item.find('img').get('src')
            continue
        else:
            name = item.next_element.text
            name=name.replace(',','')
            name = lower_func(name)
            dictionary[names] = name
            name = item.next_element.next_element.next_element.text
            name = name.replace(',', '')
            dictionary[text_profile]= name

        dict_list.append(dictionary)
        dictionary={}

    return dict_list





