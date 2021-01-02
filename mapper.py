import sys

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) == 4:
        id_twi, text, id_rule, tag = data
        print ("{0}".format(tag))