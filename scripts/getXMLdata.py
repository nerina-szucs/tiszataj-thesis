from xml.dom import minidom
from urllib.parse import urlparse
import sys
import os
import json


def get_filenames(xml_file):
    mydoc = minidom.parse(xml_file)
    files = mydoc.getElementsByTagName('url')
    # get the content of url tag
    txt_filenames = []
    # new list for the filenames that refer to the creator

    for elem in files:
        url = elem.firstChild.data
        url = urlparse(url).path
        segments = url.rpartition('/')
        pdf_filename = segments[2]
        pdf_segments = str(pdf_filename).rpartition('_')
        filenames = pdf_segments[0]
        filenames_ext = str(filenames) + ".txt"
        txt_filenames.append(filenames_ext)
        # modify the filename and add it to the list
    return txt_filenames


def get_creations(xml_file):
    mydoc = minidom.parse(xml_file)
    files = mydoc.getElementsByTagName('title')
    creations = []

    for elem in files:
        creation = elem.firstChild.data
        creations.append(creation.replace('\n', ' '))
    return creations


def get_creationsbyfile(xml_file):
    txt = get_filenames(xml_file)
    creations = get_creations(xml_file)
    creations_txt = dict(zip(txt, creations))
    return creations_txt


def get_startpage(xml_file):
    mydoc = minidom.parse(xml_file)
    pageranges = mydoc.getElementsByTagName('pagerange')
    startpages = []

    for elem in pageranges:
        page = elem.firstChild.data
        page_segments = page.rpartition('-')
        startpages.append(page_segments[0])
    return startpages


def get_pageranges(xml_file):
    mydoc = minidom.parse(xml_file)
    pageranges = mydoc.getElementsByTagName('pagerange')
    pages = []

    for elem in pageranges:
        page = elem.firstChild.data
        pages.append(page)
    return pages


def get_name(xml_file):
    global surname, firstname
    mydoc = minidom.parse(xml_file)
    creators = mydoc.getElementsByTagName('creators')

    for creator in creators:
        items = creator.getElementsByTagName('item')

        for item in items:
            names = item.getElementsByTagName('name')

            for name in names:
                surnames = name.getElementsByTagName('family')
                surname = surnames[0].firstChild.data
                firstnames = name.getElementsByTagName('given')
                firstname = firstnames[0].firstChild.data

    fullname = str(surname) + ' ' + str(firstname)
    return fullname

def get_formattedname(xml_file):
    global surname, firstname
    mydoc = minidom.parse(xml_file)
    creators = mydoc.getElementsByTagName('creators')

    for creator in creators:
        items = creator.getElementsByTagName('item')

        for item in items:
            names = item.getElementsByTagName('name')

            for name in names:
                surnames = name.getElementsByTagName('family')
                surname = surnames[0].firstChild.data
                firstnames = name.getElementsByTagName('given')
                firstname = firstnames[0].firstChild.data
    formatted_name = str(surname) + '__' + str(firstname)
    return formatted_name

def get_creationsforform(xml_file):
    creationslist = get_creations(xml_file)

    for i in range(len(creationslist)):
        if ";" in creationslist[i]:
            creationslist.remove(creationslist[i])
            splitted = creationslist[i].split(';')

            for i in range(len(splitted)):
                creationslist.append(splitted[i].strip())

    for i in range(len(creationslist)):
        if '?' in creationslist[i]:
            creationslist[i] = creationslist[i].replace('?', '').strip().replace('  ', ' ')
        if '[' in creationslist[i]:
            creationslist[i] = creationslist[i].split('[')[0].strip().replace('  ', ' ')
        if '(' in creationslist[i]:
            creationslist[i] = creationslist[i].split('(')[0].strip().replace('  ', ' ')
        if ':' in creationslist[i]:
            creationslist[i] = creationslist[i].replace(':', '').strip().replace('  ', ' ')
        if '"' in creationslist[i] or "„" in creationslist[i]:
            creationslist[i] = creationslist[i].replace('"', '').replace('„', '').strip().replace('  ', ' ')

    return creationslist


if __name__ == '__main__':
    try:
        php_param = sys.argv[1]
        xmlname = f'{os.getcwd()}\\scripts\\xmloutputs\\{php_param}'
        myListJson = json.dumps(get_creationsforform(xmlname))
        print(myListJson)
    except IndexError:
        print("Nincs php parameter")
