Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a.b=9,2
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    a.b=9,2
NameError: name 'a' is not defined
>>> a,b=9,2
>>> print(a**b)
81
>>> print(a%b)
1
>>> print(a//b)
4
>>> a,b=9,0,2.0
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    a,b=9,0,2.0
ValueError: too many values to unpack (expected 2)
>>> a,b=9,0,2.0
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    a,b=9,0,2.0
ValueError: too many values to unpack (expected 2)
>>> print(a//b)
4
>>> a,b=9.0,2.0
>>> print(a//b)
4.0
>>> print(a/b)
4.5
>>> a=(100==100)
>>> a
True
>>> b=(10>100)
>>> b
False
>>> a="안녕하세요. \"반가워요/"
>>> ㅁ
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    ㅁ
NameError: name 'ᄆ' is not defined
>>> a
'안녕하세요. "반가워요/'
>>> a=
SyntaxError: invalid syntax
>>> a='안녕하세요. "반가워요.'
>>> a
'안녕하세요. "반가워요.'
>>> a='''파이썬 입니다.
오늘 수업은 재미있나요?'''
>>> a='김종희입니다.
SyntaxError: EOL while scanning string literal
>>> a
'파이썬 입니다.\n오늘 수업은 재미있나요?'
>>> print(a)
파이썬 입니다.
오늘 수업은 재미있나요?
>>> 