from getXMLdata import get_creationsbyfile

creations = get_creationsbyfile('xmloutputs/Benedek__Miklós.xml')
print(creations)
file = "Benedek__Miklós_2016_010.txt"
notxt_filename = file.split('.txt')[0]
splitted_filename = notxt_filename.split('_')
formatted_filename = splitted_filename[0] + '__' + splitted_filename[2]


def current_titles(creationsbyfile, f_filename):
    global currenttitle
    for key in creationsbyfile.keys():
        # formatted_key = key.split('tiszataj_')[1]
        year = notxt_filename.split(f_filename)[1][1:]
        if year in key:
            currenttitle = creationsbyfile[key]
    return currenttitle


def multiple_splitter(filename, creationsbyfile, f_filename):
    global titles
    current_title = current_titles(creationsbyfile, f_filename)
    #for currentTitle in creationsbyfile.values():
    if ";" in current_title:
        titles = current_title.split(';')

    for i in range(len(titles)):
        titles[i] = titles[i].strip()
        if '[' in titles[i]:
            splitted = titles[i].split('[')
            titles[i] = splitted[0]
        if '(' in titles[i]:
            splitted = titles[i].split('(')
            titles[i] = splitted[0]
        if ':' in titles[i]:
            titles[i] = titles[i].replace(':', '').strip()
        if '?' in titles[i]:
            titles[i] = titles[i].replace('?', '').strip()

    with open(f'txtoutputs/{filename}', encoding='windows-1250', errors='ignore') as in_file:
        filelines = in_file.readlines()

        for i in range(0, len(filelines)):
            first_title = next((k for k in titles if filelines[i].rstrip("\n").startswith(k)), None)

            if first_title is not None:
                titles.remove(first_title)

                if len(titles) == 0:
                    with open(f'txtoutputs/{formatted_filename}_{first_title}.txt', 'w', encoding='windows-1250',
                              errors="ignore") as output:
                        output.writelines(filelines[i:])
                    break

                for j in range(i, len(filelines)):
                    isthereanother = any((k for k in titles if filelines[j].rstrip("\n").startswith(k)))

                    if isthereanother is True:
                        with open(f'txtoutputs/{formatted_filename}_{first_title}.txt', 'w', encoding='windows-1250',
                                  errors="ignore") as output:
                            output.writelines(filelines[i:j])

                        i = j + 1
                        break


multiple_splitter(file, creations, formatted_filename)
