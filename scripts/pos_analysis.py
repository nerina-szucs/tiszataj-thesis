#!/usr/bin/env python3.9
import csv
import json
import os
from collections import Counter
from urllib.parse import unquote
import sys

cwd = os.getcwd()

php_param = sys.argv[1]
php_param2 = unquote(php_param)

words_list = []
words_list2 = []


def read_file(filename):
    with open(f'{cwd}\\scripts\\txtoutputs\\mloutputs\\{filename}', 'r', encoding="windows-1250") as words:
        word_reader = csv.DictReader(words, delimiter="\t")
        for word in word_reader:
            words_list.append(dict(word))


def words_by_pos(list_name, pos):
    output = [word for word in list_name if str(word["SZOFAJ"]) == pos]
    return output


counts = []


def multiple_appends(list):
    for i in range(len(list)):
        counts.append(list[i])


read_file(php_param2)

words_count_all = [words_list.count(p) for p in words_list]
words_freq = dict(list(zip(words_count_all, words_list)))

noun_dict = words_by_pos(words_list, "NOUN")
verb_dict = words_by_pos(words_list, "VERB")
adj_dict = words_by_pos(words_list, "ADJ")
adv_dict = words_by_pos(words_list, "ADV")
propn_dict = words_by_pos(words_list, "PROPN")
intj_dict = words_by_pos(words_list, "INTJ")
pron_dict = words_by_pos(words_list, "PRON")
det_dict = words_by_pos(words_list, "DET")
adp_dict = words_by_pos(words_list, "ADP")
aux_dict = words_by_pos(words_list, "AUX")
conj_dict = words_by_pos(words_list, "CONJ")

num_dict = words_by_pos(words_list, "NUM")
part_dict = words_by_pos(words_list, "PART")

noun_count = len(noun_dict)
verb_count = len(verb_dict)
adj_count = len(adj_dict)
adv_count = len(adv_dict)
propn_count = len(propn_dict)
intj_count = len(intj_dict)
pron_count = len(pron_dict)
det_count = len(det_dict)
adp_count = len(adp_dict)
aux_count = len(aux_dict)
conj_count = len(conj_dict)

num_count = len(num_dict)
part_count = len(part_dict)

multiple_appends(
    [noun_count, verb_count, adj_count, adv_count, propn_count, intj_count, pron_count, det_count, adp_count, aux_count,
     conj_count])

words_counter = counts
words_counter.append(num_count)
words_counter.append(part_count)

words_count = sum(words_counter)

output = counts
output.insert(0, words_count)

to_title = php_param2.removesuffix('.txt').replace('__', ' ').split('_')
creator_name = to_title[0]
if to_title[1].isdecimal():
    creation_title = to_title[1] + ' ' + to_title[2]
else:
    creation_title = to_title[1]
output.insert(0, creator_name)
output.insert(1, creation_title)


def get_max_word(filename):
    with open(f'{cwd}\\scripts\\txtoutputs\\mloutputs\\{filename}', 'r', encoding="windows-1250") as words:
        csv_file = csv.DictReader(words, delimiter="\t")

        szo_stat = Counter(k['SZO'] for k in csv_file if str(k["SZOFAJ"]) != "DET" and str(k["SZOFAJ"]) != "PUNCT" and
                           str(k["SZOFAJ"]) != "CONJ" and str(k["SZOFAJ"]) != "SCONJ" and str(k["SZOFAJ"]) != "ADV" and
                           str(k["SZOFAJ"]) != "PART")
        mostused = max(szo_stat, key=szo_stat.get)
        return mostused


def get_freq_word(filename, pos):
    with open(f'{cwd}\\scripts\\txtoutputs\\mloutputs\\{filename}', 'r', encoding="windows-1250") as words:
        csv_file = csv.DictReader(words, delimiter="\t")

        szo_stat = Counter(k['SZO'] for k in csv_file if str(k["SZOFAJ"]) != "DET" and str(k["SZOFAJ"]) != "PUNCT" and
                           str(k["SZOFAJ"]) != "PART")

        firstten = szo_stat.most_common(20)
        valami = firstten[pos]
        valami2 = valami[0]
        return valami2


def get_freq_number(filename, pos):
    with open(f'{cwd}\\scripts\\txtoutputs\\mloutputs\\{filename}', 'r', encoding="windows-1250") as words:
        csv_file = csv.DictReader(words, delimiter="\t")

        szo_stat = Counter(k['SZO'] for k in csv_file if str(k["SZOFAJ"]) != "DET" and str(k["SZOFAJ"]) != "PUNCT" and
                           str(k["SZOFAJ"]) != "PART")

        firstten = szo_stat.most_common(20)
        valami = firstten[pos]
        valami2 = valami[0]
        szam = szo_stat[f'{valami2}']
        return szam


def get_freq_word_adj(filename, pos):
    with open(f'{cwd}\\scripts\\txtoutputs\\mloutputs\\{filename}', 'r', encoding="windows-1250") as words:
        csv_file = csv.DictReader(words, delimiter="\t")

        szo_stat = Counter(k['SZO'] for k in csv_file if str(k["SZOFAJ"]) == "ADJ")

        firstten = szo_stat.most_common(5)
        valami = firstten[pos]
        valami2 = valami[0]
        return valami2


def get_freq_number_adj(filename, pos):
    with open(f'{cwd}\\scripts\\txtoutputs\\mloutputs\\{filename}', 'r', encoding="windows-1250") as words:
        csv_file = csv.DictReader(words, delimiter="\t")

        szo_stat = Counter(k['SZO'] for k in csv_file if str(k["SZOFAJ"]) == "ADJ")

        firstten = szo_stat.most_common(5)
        valami = firstten[pos]
        valami2 = valami[0]
        szam = szo_stat[f'{valami2}']
        return szam


output.append(get_max_word(php_param2))
output.append(get_freq_word(php_param2, 0))
output.append(get_freq_number(php_param2, 0))
output.append(get_freq_word(php_param2, 1))
output.append(get_freq_number(php_param2, 1))
output.append(get_freq_word(php_param2, 2))
output.append(get_freq_number(php_param2, 2))
output.append(get_freq_word(php_param2, 3))
output.append(get_freq_number(php_param2, 3))
output.append(get_freq_word(php_param2, 4))
output.append(get_freq_number(php_param2, 4))
output.append(get_freq_word(php_param2, 5))
output.append(get_freq_number(php_param2, 5))
output.append(get_freq_word(php_param2, 6))
output.append(get_freq_number(php_param2, 6))
output.append(get_freq_word(php_param2, 7))
output.append(get_freq_number(php_param2, 7))
output.append(get_freq_word(php_param2, 8))
output.append(get_freq_number(php_param2, 8))
output.append(get_freq_word(php_param2, 9))
output.append(get_freq_number(php_param2, 9))
output.append(get_freq_word(php_param2, 10))
output.append(get_freq_number(php_param2, 10))
output.append(get_freq_word(php_param2, 11))
output.append(get_freq_number(php_param2, 11))
output.append(get_freq_word(php_param2, 12))
output.append(get_freq_number(php_param2, 12))
output.append(get_freq_word(php_param2, 13))
output.append(get_freq_number(php_param2, 13))
output.append(get_freq_word(php_param2, 14))
output.append(get_freq_number(php_param2, 14))
output.append(get_freq_word(php_param2, 15))
output.append(get_freq_number(php_param2, 15))
output.append(get_freq_word(php_param2, 16))
output.append(get_freq_number(php_param2, 16))
output.append(get_freq_word_adj(php_param2, 0))
output.append(get_freq_number_adj(php_param2, 0))
output.append(get_freq_word_adj(php_param2, 1))
output.append(get_freq_number_adj(php_param2, 1))
output.append(get_freq_word_adj(php_param2, 2))
output.append(get_freq_number_adj(php_param2, 2))
output.append(get_freq_word_adj(php_param2, 3))
output.append(get_freq_number_adj(php_param2, 3))
output.append(get_freq_word_adj(php_param2, 4))
output.append(get_freq_number_adj(php_param2, 4))

countJson = json.dumps(output)
print(countJson)
