# 띄어쓰기 -> Ngram(LanguageModel)

# q = 'ABCD..'
# i =  ^
# r = ''

# 2gram
# while i < len(q)-(n-1)
#     1. i = 0
#        r += q[:i+(n-1)]
#        q[i] = 'A'
#        keys = freq('A?'), ....]
#        max => condProb. key[-1] => ' '
#        r += ' '
#     2. i = 1
#        r += q[i:i+(n-1)]
#        q[i] = 'B'
#        keys = freq('B?'), ....]
#        max => condProb. key[-1] => ' '
#        r += ' '


# 3gram
# r += q[:(n-1)]
# while i < len(q)-(n-1)
#     1. i = 0
#        k = r[-(n-1):]
#        p1 = freq('AB')
#        keys = freq('AB'), ....]
#        max => condProb. key[-1] => ' '
#        r += ' '
#     2. i = 0
#        k = r[-(n-1):]
#        r += q[i:i+(n-1)]
#        q[i] = 'B'
#        keys = freq('B?'), ....]
#        max => condProb. key[-1] => ' '
#        r += q[i+(n-1)]
#        i += 1
#     3. i = 1

from os import listdir

def fileids(path):
    return list(map(lambda f:path + ('' if path[-1] == '/' else '/') +f, listdir(path)))

def ngram(s, n=2, t=True): # t=True;어절, False;음절
    result = []

    if not t:
        s = list(s)

    for i in range(len(s)-(n-1)):
        result.append(tuple(s[i:i+n]))

    return result

def findKey(gram, key):
    k = tuple(key)
    return list(filter(lambda g:g[:len(k)] == k, gram.keys()))

def autoSpacing(q, n=2):
    i = 0

    while i < len(q)-(n-1):
        i += 1

    return r

autoSpacing()

fileids('news')

import re

corpus = list()

for f in fileids('news'):
    with open(f, 'r', encoding='utf8') as fp:
        corpus.append(
            re.sub(r'^\s+|\s+$', '',
               re.sub(r'\s+', ' ',
                    re.sub(r'\sCopyright.+$', ' ',
                      re.sub(r'[\xa0-\xff]', ' ', fp.read())))))

corpus[0]

# .
# 다음문장

import os
'JAVA_HOME' in os.environ
os.environ['JAVA_HOME'] = r'C:\Program Files\Java\jdk-22'

from nltk.tokenize import sent_tokenize

gram = {2:list(), 3:list(), 4:[], 5:[]}
for c in corpus:
    for s in sent_tokenize(c):
        gram[2].extend(ngram(s,2,False))
        gram[3].extend(ngram(s,3,False))
        gram[4].extend(ngram(s,4,False))
        gram[5].extend(ngram(s,5,False))

from collections import Counter

gram = {2:Counter(gram[2]), 3:Counter(gram[3]), 4:Counter(gram[4]), 5:Counter(gram[5])}

def autoSpacing(q, n=2):
    i = 0
    r = list()

    r.append(q[i:i+(n-1)])

    while i < len(q)-(n-1):
        k = ''.join(r[-(n-1):])
        keys = findKey(gram[n], k)
        candidates = {j : gram[n][j] for j in keys}
        try:
            best = sorted(candidates.items(), key = lambda r:r[1], reverse=True)[0]
            if best[0][-1] == ' ':
                r.append(' ')
        except :
            print(k ,keys)

        r.append(q[i+(n-1)])
        i += 1

    return ''.join(r)

autoSpacing(sent_tokenize(corpus[0])[0].replace(' ',''), 2)

findKey(gram[2], '롯')

# 2gram => P(A,B)/P(A) -> 1음절단어 + 공백
# 3gram => P(A,B,C)/P(A,B) -> 2음절단어

{k:gram[2][k] for k in findKey(gram[2], '롯')}

k = '롯'
max({k:gram[2][k] for k in findKey(gram[2], k)}.values())

k = '가'
max({k:gram[2][k] for k in findKey(gram[2], k)}.values())

k = '다'
max({k:gram[2][k] for k in findKey(gram[2], k)}.values())

autoSpacing(sent_tokenize(corpus[0])[0].replace(' ',''), 2), sent_tokenize(corpus[0])[0]

# Branch Entropy -> Stemming

# sum (p*log p)
# p => P(x_i|x_o ...  x_i-1)
#   => P(?/A)
#   => P(A,?)/P(A)

'\n'.join(corpus)

'\n'.join(corpus).split()

tokens = Counter('\n'.join(corpus).split())

from math import log

def stemming(q):
    result = list()
    for i in range(len(q)):
        given = sum([tokens[k] for k in tokens.keys() if re.match(q[:i+1], k)])
        p = [tokens[k]/given for k in tokens.keys() if re.match(q[:i+2], k)]
        result.append(-sum([cp*log(cp) for cp in p]))

    return result

stemming('실시한다')

from math import log

def stemming(q):
    result = list()
    for i in range(len(q)-1):
        print(q[:i+1], q[:i+2])
        given = sum([tokens[k] for k in tokens.keys() if re.match(q[:i+1], k)])
        p = [tokens[k]/given for k in tokens.keys() if re.match(q[:i+2], k)]
        print(given for k in tokens.keys() if re.match(q[:i+2], k))
        result.append(-sum([cp*log(cp) for cp in p]))

    return result

stemming('실시한다')

from math import log

def stemming(q):
    result = list()
    for i in range(len(q)-1):
        print(q[:i+1], q[:i+2])
        given = sum([tokens[k] for k in tokens.keys() if re.match(q[:i+1], k)])
        p = [tokens[k]/given for k in tokens.keys() if re.match(q[:i+2], k)]
        print(p)
        result.append(-sum([cp*log(cp) for cp in p]))

    return result

stemming('실시한다')

# defaultdict, 없는 키가 나오면 디폴트 값 제공으로 키에러 방지

from collections import defaultdict

{1:1}[2], {1:1}.get(s), {1:1}.get(2,0)

temp = defaultdict(lambda:0)

temp[2]

from math import log
from collections import defaultdict

def stemming(q):
    threshold = 10.0
    for i in range(len(q)-1):
        candidates = defaultdict(lambda:0)
        given = sum([tokens[k] for k in tokens.keys() if re.match(q[:i+1], k)])
        for k in [t for t in tokens.keys() if re.match(q[:i+1], t)]:
            candidates[k[:i+2]] += tokens[k]
        be = -sum([(v/given)*log(v/given) for k, v in candidates.items()])

        if be > threshold:
            # print(i, q[:i+1], q[i+1:])
            break

        threshold = be

    return q if i == len(q)-1 else (q[:i+1], q[i+1:])

stemming('실시')

[(k, tokens[k]) for k in tokens.keys() if re.match('실시', k)]

from math import log
from collections import defaultdict

def stemming(q):
    threshold = 10.0
    for i in range(len(q)-1):
        candidates = defaultdict(lambda:0)
        given = sum([tokens[k] for k in tokens.keys() if re.match(q[:i+1], k)])
        for k in [t for t in tokens.keys() if re.match(q[:i+1], t)]:
            candidates[k[:i+2]] += tokens[k]
        be = -sum([(v/given)*log(v/given) for k, v in candidates.items()])

        if be > threshold:
            # print(i, q[:i+1], q[i+1:])
            break

        threshold = be

    return (q,) if i == len(q)-1 else (q[:i+1], q[i+1:])

stemming('롯데마트')

for t in corpus[0].split():
    r = stemming(t)
    if len(r) > 1:
        print(r)

# L (어근, 어간), R (접사, 어미)

import re

# 문자 오류나면 구두점 제거하고 실행하기

from string import punctuation

punctuation, re.escape(punctuation)



# Perplexity - 클러스터링의 성능 평가로 주로 활용, 자연어 처리 시에 사용

# 전체음절 πP(Xt+1|x1...xt)

def cohesion(t):
    t1 = t[:1]
    freq_t1 = sum([tokens[x] for x in list(filter(lambda k:re.match (t1, k), tokens.keys()))])
    print(t1, freq_t1)

    for i in range(1, len(t)):
        t2 = t[:i+1]
        tokens.keys()
        freq_t2 = sum([tokens[x] for x in list(filter(lambda k:re.match (t2, k), tokens.keys()))])

cohesion('실시한다')

def cohesion(t):
    t1 = t[:1]
    freq_t1 = sum([tokens[x] for x in list(filter(lambda k:re.match (t1, k), tokens.keys()))])

    for i in range(1, len(t)):
        t2 = t[:i+1]
        tokens.keys()
        freq_t2 = sum([tokens[x] for x in list(filter(lambda k:re.match (t2, k), tokens.keys()))])
        print(t2, freq_t2, freq_t2/freq_t1)

cohesion('실시한다')

def cohesion(t):
    t1 = t[:1]
    freq_t1 = sum([tokens[x] for x in list(filter(lambda k:re.match (t1, k), tokens.keys()))])

    threshold = 0.0

    for i in range(1, len(t)):
        t2 = t[:i+1]
        freq_t2 = sum([tokens[x] for x in list(filter(lambda k:re.match (t2, k), tokens.keys()))])
        score = (freq_t2/freq_t1)**(len(t2))
        if score < threshold:
            print(i)
        threshold = score

    return (t,) if i == len(t)-1 else (t[:i], t[i:])

cohesion('실시한다')

for t in re.sub(r'[{}]'.format(punctuation), '', corpus[0]).split():
    if len(t) > 2:
        r = cohesion(t)
        if len(r) > 1:
            print(r)

# Tokenizing
# split(), splitlines()
# sent_tokenize, word_tokenize, regex_tokenize, TweetTokenize < 언어적 특징 x, 구두점
# 한국어 > 형태소분석기, 명사추출기, 품사추출기
# 언어적 특징 : Ngram
# 통계적 방법 ; Branch-entropy, Perplexity (-> Cohesion score) -> 분절을 생성
#              BPE -> 분절을 생성, 패던 -> 불용어 처리

# Byte Pair Encoding (Digram Coding) (모스부호)

from nltk.corpus import stopwords

import nltk
nltk.download('stopwords')

stopwords.fileids()

stopwords.open(stopwords.fileids()[8]).read().split()

stop = stopwords.open('english').read()

d = 'I love you. SOTA(State-Of-The-Art)'
d.lower() # 대소문자 일치

re.sub(f'[{punctuation}]', '', d.lower()) # 문장기호 삭제

r = []
for t in re.sub(f'[{punctuation}]', '', d.lower()).split():
    if t not in stop:
        r.append(t)
r

d = "To be or not to be"
r = []
for t in re.sub(f'[{punctuation}]', '', d.lower()).split():
    if t not in stop:
        r.append(t)
r



