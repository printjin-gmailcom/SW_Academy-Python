# 아무 데이터나 수집 X
# robots.txt (O)
# 트래픽 (delay)
# 이용약관 (반드시 확인)
# DB (저작권)
# 개인정보 X
# -> 개인, 공적, 연구용, 배포 및 공유 불가, Opt-out 관리

# HTTP (HyperText)
# TCP / IP : 요청 - 응답 (Header)
# Header
# - Status Code, Reason 반드시 확인
# - Content - type ; text/html*, application/*, image/*, video/*, ....
#                   byte -> text
# - User-agent, X-CSRFTOKEN, Referer

# HTTP - Urllib - Request (Hight-level*)
# - URL parsing : Bytes 주고 받아야함
# Requests
# - Response 객체
# - Request 객체
# - Error 에 대한 처리 ; HTTP Error ; raise_for_status()



from requests import request

url = 'https://httpbin.org/post'
resp = request('POST', url, params={'이름1':'값1'}, data={'이름':'값'})

resp.status_code, resp.reason

resp.headers['content-type']

# application - json, xml

import json

# json.load(fp), loads(str)
# json.dump(fp), dump(str)

json.loads(resp.text)['args']

json.loads(resp.text)['args'].keys(),\
json.loads(resp.text)['args'].values()

json.loads(resp.text)['form']

resp.text

resp.json()

resp.request.body

resp.request.url

from requests.compat import urlparse

urlparse(resp.request.url).query, resp.request.body
# ----query string                    form-data

# <form action='주소' method='POST'>
#    <input name="이름" value="값">...
#</form>

# Commented out IPython magic to ensure Python compatibility.
# %%writefile text.xml
# <xml>
# <url>
# <LOC>https://www.korea.ac.kr/>/LOC>
# <lastmod>2023-05-17</lastmod>
# <changefreq>always</changefreq>
# <priority>0.9</priority>
# </url>
# </xml>

# 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
url = 'https://www.google.com/search'
params = {
    'q' : '수지',
    'sourceid' : 'chrome',
    'ie' : 'UTF-8'
}

resp = request('GET', url, params=params)
resp.status_code, resp.reason

resp.headers, resp.request.headers

resp.text

from requests.compat import unquote
unquote(resp.text)

from requests.compat import unquote
from html import unescape
unescape(resp.text)

from requests.compat import unquote
from html import unescape
resp.text

# <h3 class="LC20lb MBeuO DKV0Md">수지(1994)</h3>

ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
url = 'https://www.google.com/search'
params = {
    'q':'수지',
    'sourceid':'chrome',
    'ie':'UTF-8'
}

resp = request('GET', url, params=params, headers={'user-agent':ua})
resp.status_code, resp.reason

resp.headers, resp.request.headers

from requests.compat import unquote
from html import unescape
resp.text

from requests.compat import unquote
from html import unescape
import re

len(re.findall(r'<h3 class="LC20lb MBeuO DKV0Md">(.+?)</h3>', resp.text))

from requests.compat import unquote
from html import unescape
import re

re.findall(r'<h3 class="LC20lb MBeuO DKV0Md">(.+?)</h3>', resp.text)

resp.text

# <a jsname="UWckNb" href="https://namu.wiki/w/%수지(1994)" data-ved="2ahUKEwi5_tLGl_iEAxX9gK8BHU7fBqQQFnoECBUQAQ" ping="/url?sa=t&amp;source=web&amp;rct=j&amp;opi=89978449&amp;url=https://namu.wiki/w/%25EC%2588%2598%25EC%25A7%2580(1994)&amp;ved=2ahUKEwi5_tLGl_iEAxX9gK8BHU7fBqQQFnoECBUQAQ">

from requests.compat import unquote
from html import unescape
import re

re.findall(r'<a jsname="UWckNb" href="(.+?)"[^>]+?><br><h3 class="LC20lb MBeuO DKV0Md">(.+?)</h3>', resp.text)



url = 'https://search.naver.com/search.naver'
params = {
    'where' : 'nexearch',
    'sm':'top_hty',
    'fbm' : '0',
    'ie' : 'utf',
    'query' : '수지'
}

resp = request('GET', url, params=params)
resp.status_code, resp.reason

resp.headers, resp.request.headers, resp.request.url, resp.request.body

re.findall(r'<a href="([^"]+?)" class="news_tit"[^>]+?>(.+?)</a>', resp.text)

re.findall(r'<a target="_blank" href="([^"]+?)" class="link_tit"[^>]+?>(.+?)</a>', resp.text)

url = 'https://search.daum.net/search'
params = {
    'w' : 'tot',
    'DA' : 'YZR',
    't_nil_searchbox':'btm',
    'q' : '수지'
}

resp = request('GET', url, params=params)
resp.status_code, resp.reason

resp.text

re.findall(r'<c-menu-share .+? data-title="(.+?)" .+? data-href="(.+?)"[^>]+?>(.+?)</c-title>', resp.text)

url = 'https://search.naver.com/search.naver'
params = {
    'where' : 'nexearch',
    'sm':'top_hty',
    'fbm' : '0',
    'ie' : 'utf',
    'query' : '수지'
}

resp = request('GET', url, params=params)
resp.status_code, resp.reason

re.findall(r'<img data-image-viewer-trigger .+? src="(.+?)"', resp.text)

data = '''
<a href ="/" asdf=asdasd b=c>
'''
re.findall(r'<\w+(\s*.+?=.+?)*>',data)

data = '''
<a href="/" a=1 b=2 c=3>
'''
re.findall(r'<\w+((?:\s*.+?=[\'\"]?.+?[\'\"]?)*)>',data)

# 검색결과(구글, 네이버, 다음)에서 링크/제목 가져왔고,
# 네이버 이미지 링크 가져옴. => RE



# dom

from bs4 import BeautifulSoup

# Commented out IPython magic to ensure Python compatibility.
# %%writefile test.html
# <html>
#     <head></head>
#         <body>
#         <p>내용<?p>
#         </body>
# </HTML>

# Commented out IPython magic to ensure Python compatibility.
# %%writefile test.html
# <html>
#         <p>내용<?p>
# </HTML>

html='''
<html>
    <head></head>
    <body>
    <div>
    <ul>
    <li> 첫번째
    <li> 두번쩨
    </div>
    </ul>
    </body>
</HTML>
'''

pip install html5lib

pip install lxml

dom1 = BeautifulSoup(html, 'html.parser')
dom2 = BeautifulSoup(html, 'lxml')
dom3 = BeautifulSoup(html, 'html5lib')

dom1

dom2

dom3

html='''
<html>
    <head></head>
    <body>
    <div>
    <p><a>go to page</a>
    </div>
    </ul>
    </body>
</HTML>
'''

dom1 = BeautifulSoup(html, 'html.parser')
dom2 = BeautifulSoup(html, 'lxml')
dom3 = BeautifulSoup(html, 'html5lib')

dom1

dom2

dom3

html='''
<html>
    <head></head>
    <body>
    <div>
    <p>
    <a>go to page</a>
    </p>
    </div>
    </ul>
    </body>
</HTML>
'''

dom = BeautifulSoup(html, 'html.parser')

type(dom), type(dom.html), type(dom.html.body)

dom.html.body.div.p.a is dom.body.a

dom.div.a is dom.a

html='''
<html>
    <head></head>
    <body>
    <div>
    <p>
    <a href="/a.html">go to page</a>
    </p>
    </div>
    </ul>
    </body>
</HTML>
'''

dom = BeautifulSoup(html, 'html.parser')

type(dom), type(dom.html), type(dom.html.body)

dom.html.body.div.p.a is dom.body.a

dom.div.a is dom.a

dom.a

dir(dom.a)

dom.a.attrs

dom.a.attrs['href'], dom.a.get_text()

html='''
<html>
    <head></head>
    <body>
    <div>
    <p>
    <a href="/a.html">go to page1</a>
    <a href="/a.html">go to page2</a>
    </p>
    </div>
    </ul>
    </body>
</HTML>
'''

dom = BeautifulSoup(html, 'html.parser')

dom.a

dom.p.children

[tag for tag in dom.p.children]

[type(tag) for tag in dom.p.children]

a2 = [tag for tag in dom.p.children][-2]

a2

a2 is dom.a

dom.a.attrs

a2.attrs

dom.p.find()

dom.p.find() is dom.a

dom.p.find_all()[-1]

dom.p.find_all()[-1] is a2

dom.find_all('a')

dom.find_all('p')

dom.p.find_all('p')

import re

dom.p.find_all((re.compile('h[1-6]'))

import re

# 1 - 태그이름(텍스트, 정규식)
dom.p.find_all('a')
dom.p.find_all(re.compile('h[1-6]'))

# 2 - 태그 속성(attributes), 정규식
# class="LC20lb Dsed"
dom.p.find_all(attrs={'href':re.compile('html$')})

import re

dom.p.find_all('a')
dom.p.find_all(re.compile('h[1-6]'))

# class="LC20lb Dsed"
dom.p.find_all(attrs={'href':re.compile('html$')})

# 3 - 자식/자손?
dom.p.find_all()

html = '''
<html>
 <head></head>
 <body>
  <div>
   <p>
    <a href="/a.html">go to page1</a>
    <a href="/b.html">go to page2</a>
    <div>
       <p>
        <a href="/c.html">go to page3</a>
        <a href="/d.html">go to page4</a>
       </p>
       <div>
       <p>
        <a href="/e.html">go to page5</a>
        <a href="/f.html">go to page6</a>
       </p>
      </div>
      </div>
   </p>
  </div>
 </body>
</HTML>
'''
dom = BeautifulSoup(html, 'html.parser')

# 3 - 자식/자손?
dom.p.find_all(recursive=False)

[tag.name for tag in dom.p.find_all(recursive=False)]

[tag.name for tag in dom.p.find_all(recursive=True)]

[tag.name for tag in dom.p.find_all(recursive=True)]

dom.p.find_all(string='go to page1')[0]

[tag.name for tag in dom.p.find_all(recursive=True)]

dom.p.find_all(string='go to page1')[0].find_parent() is dom.a

[tag.name for tag in dom.p.find_all(recursive=True)]

dom.p.find_all(string='go to page1')[0].find_parent() is dom.a
dom.p.find_all(string=re.compile('3|4$'))

[tag.name for tag in dom.p.find_all(recursive=True)]

dom.p.find_all(string='go to page1')[0].find_parent() is dom.a
dom.p.find_all(string=re.compile('3|4$'))

# 5 - 갯수
dom.p.find_all(limit=1)[0] is dom.p.find()

[tag.name for tag in dom.p.find_all(recursive=True)]

dom.p.find_all(string='go to page1')[0].find_parent() is dom.a
dom.p.find_all(string=re.compile('3|4$'))

dom.p.find_all(limit=1)[0] is dom.p.find()
dom.p.find() is dom.a

[tag.name for tag in dom.p.find_all(recursive=True)]

dom.p.find_all(string='go to page1')[0].find_parent() is dom.a
dom.p.find_all(string=re.compile('3|4$'))

dom.p.find_all(limit=1)[0] is dom.p.find()
dom.p.find() is dom.a

len(dom.p.find_all(limit=1))

dom.p.find_parents(name='html')

dom.p.find_parents(name='html')[0].name

[tag.name for tag in dom.p.find_parents()]

# div > p > a , a, div
#           *

len(dom.a.find_next_siblings())



