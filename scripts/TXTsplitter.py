from getXMLdata import get_name, get_filenames, get_creationsbyfile
from TXTpreprocessing import preprocessing

xmlfile = 'xmloutputs/Csikós__Zsuzsanna.xml'
creator_name = get_name(xmlfile)
print(creator_name)

filenames = get_filenames(xmlfile)
filename = filenames[4]
print(filename)

creationsbyfile = get_creationsbyfile(xmlfile)
print(creationsbyfile)

addition = ""
for key in creationsbyfile.keys():
    if key == filename:
        if ";" in creationsbyfile[key]:
            addition = filename.split('_', 1)[1]
        else:
            if '[' in creationsbyfile[key] and ':' in creationsbyfile[key]:
                addition = creationsbyfile[key].split('[')[0].replace(':', '').strip() + ".txt"
            if '?' in creationsbyfile[key]:
                addition = creationsbyfile[key].replace('?', '').strip() + ".txt"
            elif '[' in creationsbyfile[key]:
                addition = creationsbyfile[key].split('[')[0].strip() + ".txt"
            elif '(' in creationsbyfile[key]:
                addition = creationsbyfile[key].split('(')[0].strip() + ".txt"
            elif ':' in creationsbyfile[key]:
                addition = creationsbyfile[key].replace(':', '').strip() + ".txt"
            else:
                addition = creationsbyfile[key] + ".txt"

# for currentTitle in creationsbyfile.values():
#     if ";" in currentTitle:
#         titles = currentTitle.split(';')
#
#         for i in range(len(titles)):
#             titles[i] = titles[i].strip()
#             if '[' in titles[i]:
#                 splitted = titles[i].split('[')
#                 titles[i] = splitted[0]
#                 addition = filename
#
#     else:
#         addition = currentTitle + '.txt'

creators_file = open("../data/creators.txt", "r", encoding="utf-8")
content = creators_file.read()
other_creators = content.split("\n")
other_creators.pop()
creators_file.close()

bigcreatorname = creator_name.upper().replace(' ', '')

extended_list = []

for i in range(len(other_creators)):
    # kezdő \t elhagyása - Abafáy-Deák\tCsillag
    other_creators[i] = other_creators[i][1:]
    # darabolás \t mentén - ['Abafáy-Deák', 'Csillag']
    separate = other_creators[i].split('\t')
    normal_name = separate[0] + separate[1]
    # 'ABAFÁY-DEÁKCSILLAG'
    normal_name = normal_name.strip().upper().replace(' ', '')
    rev_name = separate[1] + separate[0]
    # 'CSILLAGABAFÁY-DEÁK'
    rev_name = rev_name.strip().upper().replace(' ', '')
    extended_list.append(normal_name)
    extended_list.append(rev_name)

extended_list = list(dict.fromkeys(extended_list))
extended_list.append("HIVATKOZOTTÉSFÖLHASZNÁLTIRODALOM")
extended_list.append("JEGYZETEK")

# __ beszúrása a vezeték- és keresztnév közé, a fájlnevek konvenciójának megfelelően
creator_name_f = creator_name.replace(" ", "__")
with open(f"../data/txt/{filename}", encoding="utf-8", errors="ignore") as in_file:
    in_file_lines = in_file.readlines()

    for i in range(len(in_file_lines)):
        # előkészítő szkript + szóközök, tabulátorok eltávolítása + darabolás soronként
        in_file_lines[i] = preprocessing(in_file_lines[i]).replace(' ', '').replace('	', '').strip('\n')

    creator_line_indexes = []
    creator_line_names = []

for i in range(0, len(in_file_lines)):
    startcreators = next((k for k in extended_list if in_file_lines[i].startswith(k)), None)
    if startcreators is not None:
        creator_line_indexes.append(i + 1)
        creator_line_names.append(startcreators)


print(creator_line_names)
print(creator_line_indexes)


def find_index(namelist, indexlist, creatorname):
    authorpos = []
    otherauthorpos = []
    indexes = []
    for g in range(0, len(namelist)):
        if namelist[g] == creatorname:
            authorpos.append(indexlist[g])
            otherauthorpos.append(indexlist[g + 1])
    indexes.append(authorpos[1])
    indexes.append(otherauthorpos[1])
    return indexes


indexes = find_index(creator_line_names, creator_line_indexes, bigcreatorname)

done = False
lineindex = 0
with open(f"../data/txt/{filename}", encoding="utf-8", errors="ignore") as in_file:
    while not done:
        with open(f"txtoutputs/{creator_name_f}_{addition}", "w", encoding="windows-1250", errors="ignore") as out_file:
            while not done:
                global line_name1
                try:
                    line = preprocessing(next(in_file))
                    lineindex += 1
                except StopIteration:
                    done = True
                    break
                # ha a keresett szerzo neve
                line_name1 = False
                if lineindex == indexes[0]:
                    line_name1 = line
                    # hagyja ki es folytassa
                    break
                # ha egy masik szerzo neve
                if lineindex == indexes[1]:
                    # ha nem a keresett szerzo neve
                    if line_name1 != line and line_name1 != "None":
                        done = True
                else:
                    out_file.write(line + '\n')

# print(' '.encode('utf-16'))
# print('	'.encode('utf-16'))

# done = False
# with open(f"../data/txt/{filename}", encoding="utf-8", errors="ignore") as in_file:
#     while not done:
#         with open(f"txtoutputs/{creator_name_f}.txt", "w", encoding="windows-1250", errors="ignore") as out_file:
#             while not done:
#                 global line_name1
#                 try:
#                     line = preprocessing(next(in_file))
#                     line_nospace = line.replace(" ", "")
#                 except StopIteration:
#                     done = True
#                     break
#                 # ha a keresett szerzo neve
#                 line_name1 = False
#                 if any(e in line for e in creator_variations):
#                     line_name1 = line
#                         # hagyja ki es folytassa
#                     break
#                     # ha szokozokkel, de benne volt a keresett szerzo
#                 elif any(e in line_nospace for e in creator_variations):
#                     line_name1 = line
#                     break
#                 # ha egy masik szerzo neve
#                 if any(f in line for f in extended_list):
#                         # ha nem a keresett szerzo neve
#                     if line_name1 != line and line_name1 != "None":
#                         done = True
#                 else:
#                     out_file.write(line + '\n')

# for creators, filelines in zip_longest(extended_list, in_file_lines):
#     if creators in filelines:
#         testnames.append(creators)

# for key in creator_line_indexes:
#     for value in creator_line_names:
#         merged[key] = value
#         creator_line_names.remove(value)
#         break

# def find_indexes(dictionary, authorname):
# authorpos = []
# nextauthorpos = 0
# indexes = []
#
# for key, value in dictionary.items():
#     if value == authorname:
#         authorpos.append(key)
#         nextauthorpos = dictionary[key]
#
# indexes.append(authorpos[1])
# indexes.append(nextauthorpos)
# return indexes

# for i in range(0, len(in_file_lines)):
#     for elem in extended_list:
#         # 46. sor nem jo
#         substring = elem
#         if substring in in_file_lines[i] or in_file_lines[i] in extended_list:
#             creator_line_indexes.append(i + 1)
#             creator_line_names.append(in_file_lines[i])
#         break
# for i in range(0, len(in_file_lines)):
#     # 46. sor nem jo
#     substring = extended_list[i]
#     if substring in in_file_lines[i] or in_file_lines[i] in extended_list:
#         creator_line_indexes.append(i + 1)
#         creator_line_names.append(in_file_lines[i])
# for i in range(0, len(in_file_lines)):
#     for j in range(0, len(extended_list)):
#         matching = [s for s in in_file_lines if extended_list[j] in s]
#         if in_file_lines[i] in extended_list:
#             creator_line_indexes.append(i + 1)
#             creator_line_names.append(in_file_lines[i])
#         print(matching)
#     break

# for i in range(0, len(in_file_lines)):
#     startcreators = next((k for k in extended_list if in_file_lines[i].startswith(k)), None)
#     if in_file_lines[i] in extended_list:
#         creator_line_indexes.append(i + 1)
#         creator_line_names.append(in_file_lines[i])
#     elif startcreators is not None:
#         creator_line_indexes.append(i + 1)
#         creator_line_names.append(startcreators)
