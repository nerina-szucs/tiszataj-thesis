from getXMLdata import get_name, get_formattedname, get_filenames, get_creationsbyfile
from TXTsplitter_multiple import multiple_splitter
from TXTpreprocessing import preprocessing

start = input("Induljon a szkript? (igen) ")
restart = "igen"
while start == "igen" and restart == "igen":

    xmlinput = input("XML fájl neve (fajlnev.xml): ")
    xmlfile = f'xmloutputs/{xmlinput}'
    creator_name = get_name(xmlfile)
    # a fájlnevek konvenciójának megfelelően
    creator_name_f = get_formattedname(xmlfile).replace(' ', '_')
    rev_creator_name = creator_name_f.split('__')[1] + creator_name_f.split('__')[0]
    # pl. Csobánka__Zsuzsa Emese -> Csobánka__Zsuzsa_Emese
    creationsbyfile = get_creationsbyfile(xmlfile)

    k = -1
    items = creationsbyfile.items()
    for item in items:
        k += 1
        print(str(k) + ": " + str(item))

    print("Választott szerző neve: " + creator_name)
    count = int(input("Hanyadik fájl legyen darabolva? "))
    filenames = get_filenames(xmlfile)
    filename = filenames[count]
    print("Darabolás: " + filename)

    addition = ""
    multiple = False
    for key in creationsbyfile.keys():
        if key == filename:
            if ";" in creationsbyfile[key]:
                multiple = True
                addition = filename.split('_', 1)[1]
            else:
                addition = creationsbyfile[key]
                if '?' in addition:
                    addition = addition.replace('?', '').strip().replace('  ', ' ')
                if '[' in addition:
                    addition = addition.split('[')[0].strip().replace('  ', ' ')
                if '(' in addition:
                    addition = addition.split('(')[0].strip().replace('  ', ' ')
                if ':' in addition:
                    addition = addition.replace(':', '').strip().replace('  ', ' ')
                if '"' in addition or "„" in addition:
                    addition = addition.replace('"', '').replace('„', '').strip().replace('  ', ' ')
                addition = addition + ".txt"

    creators_file = open("../data/creators.txt", "r", encoding="utf-8")
    content = creators_file.read()
    other_creators = content.split("\n")
    other_creators.pop()
    creators_file.close()

    bigcreatorname = creator_name.upper().replace(' ', '')
    bigcreatorname_rev = rev_creator_name.upper().replace(' ', '')

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
    extended_list.append("FORRÁSOK")
    extended_list.append("FELHASZNÁLT IRODALOM")

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

    def find_index(namelist, indexlist, creatorname, rev):
        authorpos = []
        otherauthorpos = []
        indexes = []
        for g in range(0, len(namelist)):
            if namelist[g] == creatorname or namelist[g] == rev:
                authorpos.append(indexlist[g])
                otherauthorpos.append(indexlist[g + 1])
        indexes.append(authorpos[1])
        indexes.append(otherauthorpos[1])
        return indexes


    indexes = find_index(creator_line_names, creator_line_indexes, bigcreatorname, bigcreatorname_rev)

    done = False
    lineindex = 0
    with open(f"../data/txt/{filename}", encoding="utf-8", errors="ignore") as in_file:
        while not done:
            with open(f"txtoutputs/{creator_name_f}___{addition}", "w", encoding="windows-1250",
                      errors="ignore") as out_file:
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

    if done is True:
        print("Kész! ")
        if multiple is True:
            output = f"{creator_name_f}___{addition}"
            print(f"A(z) {output} nevű fájl több művet tartalmaz. Továbbdarabolás... ")
            multiple_splitter(output, creationsbyfile, creator_name_f)
            print("Kész! ")
            restart = input("Újra? (igen/nem) ")
        else:
            restart = input("Újra? (igen/nem) ")

    # print(' '.encode('utf-16'))
    # print('	'.encode('utf-16'))
