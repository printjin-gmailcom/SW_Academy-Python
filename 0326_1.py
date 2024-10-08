# P =  MLAE, MAP(Bayes) -> p = theta optimization -> derivation
# PAC learning -> Model (error 수반) < error(^-N)
# P(A) -> 조건부(conditional), 결합(joint)
# P(B|A) -> P(A,B) / P(A)
# P(A|B) -> P(A,B) / P(B)
# P(B|A) -> P(A|B)P(B) / P(A)
# -> P(A,B) = P(B|A)P(A)
# -> sum_a P(B) = P(A=true, B) + P(A=false, B) ; marginalization, summing out
# P(A={}, B={}, C={}, D={}, E={}) -> P(B,C,D,E|A)P(A)
#                                 -> P(E|A,B,C,D,E)P(A,B,C,D,E)
#                                                 P(E|A,B,C,D,)P(A,B,C,D) ... P(B|A) P(A)
# 1sr Markov Assumption           -> P(E|D)P(D|C)P(C|B)P(B|A)P(A) -> N-gram (2-gram)
#                                                      ----------
#                                                      P(A, B)   P(A)=freq(a/N)
#                                                     freq(A,B)/freq(A)
# N-gram = Language Model -> s,s,... P(s) 계산 가능
#                             s를 생성
# Preprocessing -> tokenizing -> sentence -> tokens (word, regexp, tweet tokenizer)
#                                splitlines(X)      split(기호 문제)    + P, MA(konlpy)



import os
'JAVA_HOME' in os.environ
os.environ['JAVA_HOME'] = r'C:\Program Files\Java\jdk-22'



# pip uninstall nltk

# pip install -U nltk



from konlpy.tag import Hannanum, Kkma, Komoran, Okt

han = Hannanum()

kkm = Kkma()

kom = Komoran()

okt = Okt()

len(han.tagset), len(kkm.tagset), len(kom.tagset), len(okt.tagset)

from nltk.tokenize import treebank
from nltk.tag import pos_tag
from nltk.help import upenn_tagset

import nltk
nltk.download('tagsets')

upenn_tagset('NN')

from nltk.corpus import gutenberg

emma = gutenberg.open (gutenberg.fileids()[0]).read()

from nltk.text import Text
from nltk.tokenize import word_tokenize

t1 = Text(word_tokenize(emma))

tokenizer = treebank.TreebankWordTokenizer()
t2 = Text(tokenizer.tokenize(emma))

t1.vocab().B(), t2.vocab().B()

list(zip(t1.vocab().most_common(20), t2.vocab().most_common(20)))

data = '''

중국 젊은이들 사이에서 캐릭터 잠옷 여러 개를 겹쳐 입는 등 우스꽝스러운 복장으로 출근하는 문화가 유행인 것으로 전해졌다. 이들은 "옷을 잘 입는다고 월급을 더 주지 않으니 초라하게 입을 것"이라며 이 같은 복장을 고수한다고 말한다.

지난 24일(현지시간) 뉴욕타임스(NYT)에 따르면 지난달 중국 소셜미디어(SNS) '더우인'에 잠옷으로 보이는 회색 체크무늬 바지와 펑퍼짐한 갈색 원피스, 분홍색 상의, 갈색 어그 부츠, 빨간색 장갑, 얼굴 전체를 감싼 검은 마스크 등을 착용한 젊은 여성이 등장했다.

'''

han.pos(data)

han.morphs(data)

kkm.pos(data)

kkm.morphs(data)

kom.pos(data)

kom.morphs(data)

okt.pos(data)

okt.morphs(data)



# from konlpy.tag import Mecab # Mecab는 윈도우에서 미작동

# Mecab.tagset



han.pos('알잘딱깔센')

kkm.pos('알잘딱깔센')

kkm.tagset['MAG']

kkm.tagset['EPH']

han.tagset['J']

# 코퍼스 (말뭉치) -> 시대상을 반영



t1.vocab().most_common(50)

t2.vocab().most_common(50)



import matplotlib.pyplot as plt

plt.plot([1/i for i in range(1,101)])
plt.plot([r[1]/12016 for r in t1.vocab().most_common(100)])

plt.plot([1/i for i in range(1,51)])
plt.plot([r[1]/12016 for r in t1.vocab().most_common(50)])
plt.plot([r[1]/12016 for r in t2.vocab().most_common(50)])

from konlpy.corpus import kolaw, kobill

law = kolaw.open(kolaw.fileids()[0]).read()

import nltk
nltk.download('averaged_perceptron_tagger')

from nltk.tokenize import regexp_tokenize



kt1 = Text(law.split())

kt2 = Text(word_tokenize(law))

kt3 = Text(regexp_tokenize(law, r'\b\w+\b'))

kt4 = Text(pos_tag(word_tokenize(law)))

kt5 = Text(han.morphs(law))

kt6 = Text(kkm.morphs(law))

kt7 = Text(kom.morphs(law))

kt8 = Text(okt.morphs(law))

kt9 = Text(han.pos(law))

kt10 = Text(kkm.pos(law))

kt11 = Text(kom.pos(law))

kt12 = Text(okt.pos(law))

n = 50
plt.plot([1/i for i in range(1,n+1)], c='k')
plt.plot([r[1]/kt1.count(kt1.vocab().max()) for r in kt1.vocab().most_common(n)], c='r')
plt.plot([r[1]/kt2.count(kt2.vocab().max()) for r in kt2.vocab().most_common(n)], c='g')
plt.plot([r[1]/kt3.count(kt3.vocab().max()) for r in kt3.vocab().most_common(n)], c='b')
plt.plot([r[1]/kt4.count(kt4.vocab().max()) for r in kt4.vocab().most_common(n)], c='c')

n = 50
plt.plot([1/i for i in range(1,n+1)], c='k')
plt.plot([r[1]/kt1.count(kt1.vocab().max()) for r in kt1.vocab().most_common(n)], c='k')
plt.plot([r[1]/kt4.count(kt4.vocab().max()) for r in kt4.vocab().most_common(n)], c='r')
plt.plot([r[1]/kt5.count(kt5.vocab().max()) for r in kt5.vocab().most_common(n)])
plt.plot([r[1]/kt6.count(kt6.vocab().max()) for r in kt6.vocab().most_common(n)], c='b')
plt.plot([r[1]/kt7.count(kt7.vocab().max()) for r in kt7.vocab().most_common(n)])
plt.plot([r[1]/kt8.count(kt8.vocab().max()) for r in kt8.vocab().most_common(n)])

t1.vocab().N(), t1.vocab().B(), kt1.vocab().N(), kt1.vocab().B()

n = 50
plt.plot([1/i for i in range(1,n+1)], c='k')
plt.plot([r[1]/kt1.count(kt1.vocab().max()) for r in kt1.vocab().most_common(n)], c='k')
plt.plot([r[1]/kt4.count(kt4.vocab().max()) for r in kt4.vocab().most_common(n)], c='r')
plt.plot([r[1]/kt9.count(kt9.vocab().max()) for r in kt9.vocab().most_common(n)])
plt.plot([r[1]/kt10.count(kt10.vocab().max()) for r in kt10.vocab().most_common(n)], c='r')
plt.plot([r[1]/kt11.count(kt11.vocab().max()) for r in kt11.vocab().most_common(n)],)
plt.plot([r[1]/kt12.count(kt12.vocab().max()) for r in kt12.vocab().most_common(n)])

list(zip(kt6.vocab().most_common(10), kt10.vocab().most_common(10)))

t1.vocab().N(), t1.vocab().B()

n = 50
s1 = 0.0
s2 = 0.0

for r in t1.vocab().most_common(n):
    s1 += r[1]
    s2 += r[1]/t1.vocab().N()

    print(r[0], r[1]/t1.vocab().N(), t1.vocab().freq(r[0]))
s1, s2

n = 7300
s1 = 0.0
s2 = 0.0

for r in t1.vocab().most_common()[::-1][:n]:
    s1 += r[1]
    s2 += r[1]/t1.vocab().N()
s1, s2

n = 30
s1 = 0.0
s2 = 0.0

for r in kt6.vocab().most_common(n):
    s1 += r[1]
    s2 += r[1]/kt6.vocab().N()

    print(r[0], r[1]/kt6.vocab().N(), kt6.vocab().freq(r[0]))
s1, s2

n = 800
s1 = 0.0
s2 = 0.0

for r in kt6.vocab().most_common()[::-1][:n]:
    s1 += r[1]
    s2 += r[1]/kt6.vocab().N()
s1, s2

kt6.vocab().N(), kt6.vocab().B()

800/1247

threshold = .3
s = 0.0
mfw = list()
mrw = list()

for r in kt6.vocab().most_common():
    s += kt6.vocab().freq(r[0])

    if s > threshold:
        break

    mfw.append(r[0])

s = 0.0
for r in kt6.vocab().most_common()[::-1]:
    s += kt6.vocab().freq(r[0])

    if s > threshold:
        break

    mrw.append(r[0])

len(mfw), len(mrw), 1247



1247-(9+1156)

list(set(kt6.tokens) - set(mfw) - set(mrw))

k = 10, 100
b = .4, .6

heaps = []
heaps.append(Text(word_tokenize(gutenberg.open(gutenberg.fileids()[0]).read())).vocab())
for file in gutenberg.fileids()[1:]:
    corpus = gutenberg.open(file).read()
    heaps.append(heaps[-1]+Text(word_tokenize(corpus)).vocab())

len(heaps), heaps[0].N(), heaps[-1].N(), heaps[0].B(), heaps[-1].B()

k = 15
b = .55
plt.plot([h.B() for h in heaps])
plt.plot([k*h.N()**b for h in heaps])

(k*10000000**b) * .07

(9+1156)/1247

heaps = []
heaps.append(Text(kkm.morphs(kobill.open(kobill.fileids()[0]).read())).vocab())
for file in kobill.fileids()[1:]:
    corpus = kobill.open(file).read()
    heaps.append(heaps[-1]+Text(kkm.morphs(corpus)).vocab())

k = 12
b = .48
plt.plot([h.B() for h in heaps])
plt.plot([k*h.N()**b for h in heaps])

heaps[-1].N(), (k*heaps[-1].N()**b) * .07

heaps[-1].B(), (k*10000000**b) * .07

# N-gram: N개의 token 구성된 시퀀스 freq(A,B,C,...) => P(A,B,C,...) => 결합확률
#                               P(?|A,B) = P(A,B,?)/P(A,B)
#                                        = freq(A,B,?)/N / freq(A,B)/N
#                                        = freq(A,B,?)/freq(A,B)

def ngram(s, n=2, t=True): # t=True;어절, False;음절
    result = []

    if not t:
        s = list(s)

    for i in range(len(s)-(n-1)):
        result.append(''.join(s[i:i+n]))

    return result

ngram('아버지가방에들어가신다.', t=False), ngram('아버지가 방에 들어가신다.'.split())

tokens = kkm.morphs(law)
bigram = Text(ngram(tokens))
unigram = Text(ngram(tokens, n=1))

# NLU -> NLG
import re

seed = '대통령' # 대통령 은(0.33) 법률(0.22)
c = 0
s = 0.0

for i in range(10):
    result = {}
    for t in list(set(filter(lambda t:t.startswith(seed), bigram.tokens))):
        result[t] = bigram.count(t)/unigram.count(seed)
    n = sorted(result.items(), key=lambda r:r[1], reverse=True)[0]
    print(n)
    seed = re.sub(seed, '', n[0])

plaw = re.sub(r'^\s+|\s+$', '', re.sub(r'\s+', ' ', law))

trigram = Text(ngram(plaw, n=3, t=False))
bigram = Text(ngram(plaw, t=False))
unigram = Text(ngram(plaw, n=1, t=False))

# seed = '대통령은 국회의 국회의 국회의 ...' # 대통령 은(0.33) 법률(0.22)
# => P(B|A)
seed = '대통령은 법률이 정하는 바에 의하여 국회의 자유를 가진다. '
# => P(C|A,B)
c = 0
s = 0.0

result = {}
for t in list(set(filter(lambda t:t.startswith(seed[-2:]), trigram.tokens))):
    result[t] = trigram.count(t)/bigram.count(seed[-2:])
sorted(result.items(), key=lambda r:r[1], reverse=True)[0]



