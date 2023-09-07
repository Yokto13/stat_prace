import gzip
import numpy as np

path = "qids.txt"

qids =[]

with open(path, 'r') as fi:
    for line in fi:
        qids.append(int(line[1:]))

qids = np.array(qids, 'int32')

half = len(qids) // 2

first = qids[:half]
second = qids[half:]

with gzip.open(path + '.1.gz', 'w') as fo:
    np.save(file=fo, arr=first)
with gzip.open(path + '.2.gz', 'w') as fo:
    np.save(file=fo, arr=second)


