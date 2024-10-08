# Relevance => Similarity(Likelihood, Bayes, )
#           => Vector Space

# Dimension => Concepts(Orthogonal, Independent) = Bag of Words
#           => Term(Token), Class(Category), Cluster...

# V = {w1, w2, ..., wn}
# Q = {t1, t2, ..., tm ㅌ V}
# Di = {ti1, ti2, ..., tik ㅌ V}
# C = {d1, d2, ..., di}
# Rel(Q, D) = Sim(Q, D) => Sim(Rep(Q), Rep(D))

# Document-Term Matrix(DTM) => 색인(느림)
# Term-Document Matrix(TDM) => 역색인(Linked List)
# in-memory     on-disk(Inverted Index)
#   Term1   -   Doc1, Doc2, ...

#                             Zipf
# Rep? => Dim's importance => Weight(문서내 많이 나온 중요TF, 다른 문서에서 안나온 중요IDF)



from math import log

tf1 = lambda f: 1 if f > 0 else 0
tf2 = lambda f: f
tf3 = lambda f, s : f/s
tf4 = lambda f : log(f+1)
tf5 = lambda f, m : .5 + .5*(f/m)
tf6 = lambda k, f, m : k + (1-k)*(f/m)

import matplotlib.pyplot as plt

f = [1, 10, 100, 1000, 10000]

plt.plot([tf1(v) for v in f ], c = 'k')
# plt.plot([tf2(v) for v in f ])
plt.plot([tf3(v, sum(f)) for v in f ], c = 'r')
# plt.plot([tf4(v) for v in f ], c='g')
plt.plot([tf5(v, max(f)) for v in f ], c = 'b')
plt.plot([tf6(0, v, max(f)) for v in f ])



idf1 = lambda df : 1
idf2 = lambda df, n: log(n/df)
idf3 = lambda df, n :log(n/(1+df)) + 1
idf4 = lambda df, m : log(m/(1+df))
idf5 = lambda df, n : log((n-df)/df)

df = [1, 10, 100, 1000, 10000]

plt.plot([idf1(v) for v in df], c='k')
plt.plot([idf2(v, max(df)+1) for v in df], c='r')
plt.plot([idf3(v, max(df)+1) for v in df], c='g')
plt.plot([idf4(v, max(df)) for v in df], c='b')
# plt.plot([idf5(v, max(df)+1) for v in df])

# tf6(k=0), idf2

plt.plot([tf6(0, f[0], max(f)) * idf2(v, max(df)+1) for v in df], c='r')
plt.plot([tf6(0, f[1], max(f)) * idf2(v, max(df)+1) for v in df], c='g')
plt.plot([tf6(0, f[2], max(f)) * idf2(v, max(df)+1) for v in df], c='b')
plt.plot([tf6(0, f[3], max(f)) * idf2(v, max(df)+1) for v in df], c='k')
plt.plot([tf6(0, f[4], max(f)) * idf2(v, max(df)+1) for v in df], c='r')



# Dictionay              Posting
# 단어:위치               문서번호:빈도:다음위치
# - TF: 문서별로 max freq 찾아야 함
# - IDF: df



import os
'JAVA_HOME' in os.environ
os.environ['JAVA_HOME'] = r'C:\Program Files\Java\jdk-22'

from konlpy.corpus import kobill
from konlpy.tag import Komoran
from nltk.tokenize import word_tokenize, sent_tokenize
from struct import pack, unpack
import re

ma = Komoran()

def ngram(s, n=2):
    rst = list()
    for i in range(len(s)-(n-1)):
        rst.append(s[i:i+n])
    return rst

from os import listdir

def fileids(path):
    return [path + ('/' if path[-1] != '/' else '') + f for f in listdir(path) if re.search(r'[.]txt$', f)]

len(fileids('./news'))

def preprocessing(d):
    d = re.sub(r'\s+', ' ', d)
    d = re.sub(r'^\s|s$', '', d)
    return d

def indexer(f): # Map
    with open(f, 'r', encoding='utf8') as fp:
        text = preprocessing(fp.read())

    localMap = dict()
    for t in word_tokenize(text):
        if t not in localMap:
            localMap[t] = 0
        localMap[t] += 1

    for s in sent_tokenize(text): # 메모리 오류
        for t in ma.morphs(s):
            if t not in localMap:
                localMap[t] = 0
            localMap[t] += 1

    for t in ngram(text):
        if t not in localMap:
            localMap[t] = 0
        localMap[t] += 1

    return localMap

def indexing(path):
    C = [{'no':i+1,'name':f,'maxfreq':0} for i,f in enumerate(fileids(path))]
    Dictionary = dict()
    Posting = 'posting.dat'

    fp = open(Posting, 'wb')

    for i, f in enumerate(C):
        mapped = indexer(f['name'])
        # reducing
        for t, f in mapped.items():
            if f > C[i]['maxfreq']:
                C[i]['maxfreq'] = f

            if t not in Dictionary.keys():
                Dictionary[t] = dict()
                Dictionary[t]['ppos'] = fp.tell()
                Dictionary[t]['wpos'] = -1
                Dictionary[t]['df'] = 1
                fp.write(pack('iii', i, f, -1))
            else:
                Dictionary[t]['df'] += 1
                pos = Dictionary[t]['ppos']
                Dictionary[t]['ppos'] = fp.tell()
                fp.write(pack('iii', i, f, pos))

    fp.close()

    return C, Dictionary, Posting

C, V, posting = indexing('./news/')

N = len(C)

fp2 = open('weight.dat', 'wb')

with open(posting, 'rb') as fp:
    for t, info in V.items():
#         df = 0
#         opos = pos
#         while pos != -1:
#             fp.seek(pos)
#             i, f, pos = unpack('iii', fp.read(12))
#             df += 1
#
#         pos = opos

        df = info['df']
        V[t]['wpos'] = fp2.tell()
        pos = info['ppos']
        while pos != -1:
            fp.seek(pos)
            i, f, pos = unpack('iii', fp.read(12))
            w = tf6(0, f, C[i]['maxfreq']) * idf2(df, N)
            fp2.write(pack('if', i, w))
fp2.close()

with open('weight.dat', 'rb') as fp:
    for t, info in V.items():
        i = 0
        while i < info['df']:
            fp.seek(info['wpos']+8*i)
            no, w = unpack('if', fp.read(8))
            i += 1

2/34, log(N/1), (2/34)*log(N/1)

fileids('./news/')[5]



qkv = indexer(fileids('./news/')[5])
qw = dict()
maxfreq = max(qkv.values())
N = len(C)
for t, f in qkv.items():
    w = tf6(0, f, maxfreq)*idf2(V[t]['df'], N)
    qw[t] = w

# Distance
result = dict()

with open('weight.dat', 'rb') as fp:
    for t, info in V.items():
        i = 0
        while i < info['df']:
            fp.seek(info['wpos']+8*i)
            no, w = unpack('if', fp.read(8))

            if no not in result:
                result[no] = 0.0

            result[no] += ((qw[t] if t in qw else 0) - w)**2

            i += 1

# list(map(lambda r:(C[r[0]], r), sorted(result.items(), key=lambda r:r[1])))

for i, dist in sorted(result.items(), key=lambda r:r[1]):
    print(C[i]['name'], dist)
    with open(C[i]['name'], 'r', encoding='utf8') as f:
        d = f.read()
        kv = indexer(C[i]['name'])
        print(len(d), len(kv), sum(kv.values()))

with open('./news/0011689136.txt', 'r', encoding='utf8') as f:
    print(preprocessing(f.read()))

