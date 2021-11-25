import re


def preprocessing(line):
    line = line.replace('‐', '-').strip()
    formatted_line = re.sub(r'[^\w !?.,;:()/„”"$€£@\-\[\]\n]', '', line)
    return formatted_line

# szoveg = """
# •
#
# 67
#
# KÉKESDI: Ú J KEMENCE
# !
#
# Nyomta háromszoros iga
# Az asszony vállát, a fiát
# öreggé tette, mostoha
# Sorsa; ma már ez ú j világ!
#
# : '
#
# I
#
# . :'"""

# def preprocessing(line):
#     formatted_line1 = line.replace('‐', '-').strip()
#     formatted_line2 = re.sub(r'[^\w !?.,;:()/„”"$€£@\-\[\]\n]', '', formatted_line1)
#     return formatted_line2