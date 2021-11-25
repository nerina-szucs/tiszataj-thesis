import os


# example = "Abaf=E1y-De=E1k=3ACsillag=3A=3A"
# example2 = "L==0151rincz=3ACsongor=3A=3A"


def renameXML(XMLname):
    positions = []
    doublePositions = []
    XMLname = XMLname.removesuffix(".xml")
    newname = XMLname

    for doublepos in range(len(XMLname)):
        dchar = XMLname[doublepos]
        if dchar == "=":
            if XMLname[doublepos + 1] == "=":
                doublePositions.append(doublepos + 1)
        if doublepos == len(XMLname):
            break

    for doublePosition in doublePositions:
        for dpos2 in range(len(XMLname)):
            if dpos2 == doublePosition:
                dsubstring = XMLname[dpos2 + 1:dpos2 + 5]
                dsubstringbyte = "\\u" + str(dsubstring)
                dsubstringchar = dsubstringbyte.encode("utf-8").decode('unicode-escape')
                newname = newname.replace(dsubstring, dsubstringchar)

    XMLname = XMLname.replace("==", "")

    for pos in range(len(XMLname)):
        char = XMLname[pos]
        if char == "=":
            positions.append(pos + 1)
        if pos == len(XMLname):
            break

    for position in positions:
        for pos2 in range(len(XMLname)):
            if pos2 == position:
                substring = XMLname[pos2:pos2 + 2]
                substringbyte = "\\u" + "00" + str(substring)
                substringchar = substringbyte.encode("utf-8").decode('unicode-escape')
                newname = newname.replace(substring, substringchar)

    XMLname = newname.replace("=", "")
    XMLname = XMLname[:-2].replace(":", "__") + ".xml"
    return XMLname


# print(renameXML(example2))
# print("á".encode("unicode-escape"))

for filename in os.listdir("../data/xml"):
    dst = renameXML(filename)
    src = filename
    old_file = os.path.join("../data/xml", filename)
    new_file = os.path.join("xmloutputs", dst)
    os.rename(old_file, new_file)
