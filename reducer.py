from operator import itemgetter
import sys

tags = []
counts = []

for line in sys.stdin:
    tag  =line.strip()

    if tag in tags:
        counts[tags.index(tag)] += 1
    else:
        counts.append(1)
        tags.append(tag)

for tag in tags :
	print (tag, counts[tags.index(tag)])