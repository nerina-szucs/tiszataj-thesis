from getXMLdata import get_creationsbyfile, get_formattedname

# file = input("Továbbdarabolni kívánt fájl: (fajlnev.txt)")
# print(file)
# file = "Abafáy-Deák__Csillag_2020_002.txt"
# xml = input("XML fájl neve: (fajlnev.xml)")
# name = get_formattedname('xmloutputs/Csobánka__Zsuzsa_Emese.xml')
# print(name)
# xml = "Abafáy-Deák__Csillag.xml"
# print(xml)
# creations = get_creationsbyfile(f'xmloutputs/{xml}')
# print(creations)
# notxt_filename = file.split('.txt')[0]
# splitted_filename = notxt_filename.split('_')
# formatted_filename = splitted_filename[0] + '__' + splitted_filename[2]


def current_titles(creationsbyfile, formattedfilename, notxtfilename):
    global currenttitle
    for key in creationsbyfile.keys():
        # formatted_key = key.split('tiszataj_')[1]
        print(notxtfilename)
        print(formattedfilename)
        year = notxtfilename.split(formattedfilename)[1][1:]
        print(year)
        if year in key:
            currenttitle = creationsbyfile[key]
    return currenttitle


def multiple_splitter(filename, creationsbyfile, creator_name_f):
    global titles
    notxt_filename = filename.split('.txt')[0]
    # splitted_filename = notxt_filename.split('_')
    # f_filename = splitted_filename[0] + '__' + splitted_filename[2]
    current_title = current_titles(creationsbyfile, creator_name_f, notxt_filename)
    # for currentTitle in creationsbyfile.values():
    if ";" in current_title:
        titles = current_title.split(';')
        print(titles)

    for i in range(len(titles)):
        titles[i] = titles[i].strip()
        if '[' in titles[i]:
            splitted = titles[i].split('[')
            titles[i] = splitted[0].strip()
        if '(' in titles[i]:
            splitted = titles[i].split('(')
            titles[i] = splitted[0].strip()
        if ':' in titles[i]:
            titles[i] = titles[i].replace(':', '').strip()
        if '?' in titles[i]:
            titles[i] = titles[i].replace('?', '').strip()
        titles[i] = titles[i].replace('  ', ' ')

    print(titles)
    with open(f'txtoutputs/{filename}', encoding='windows-1250', errors='ignore') as in_file:
        filelines = in_file.readlines()

        for i in range(0, len(filelines)):
            first_title = next((k for k in titles if filelines[i].rstrip("\n").startswith(k)), None)

            if first_title is not None:
                titles.remove(first_title)

                if len(titles) == 0:
                    with open(f'txtoutputs/{creator_name_f}_{first_title}.txt', 'w', encoding='windows-1250',
                              errors="ignore") as output:
                        output.writelines(filelines[i:])
                        print("Kész!")
                    break

                for j in range(i, len(filelines)):
                    isthereanother = any((k for k in titles if filelines[j].rstrip("\n").startswith(k)))

                    if isthereanother is True:
                        with open(f'txtoutputs/{creator_name_f}_{first_title}.txt', 'w', encoding='windows-1250',
                                  errors="ignore") as output:
                            output.writelines(filelines[i:j])

                        i = j + 1
                        break

# multiple_splitter(file, creations)
