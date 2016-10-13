__author__ = 'Rok'
import unidecode

def toascii():
    with open(r'ready/slv.txt', 'r', encoding='utf8') as origfile, open(r'C:\log.toascii', 'w', encoding='ascii') as convertfile:
        for line in origfile:
            line = unidecode(line)
            print line
            convertfile.write(line)