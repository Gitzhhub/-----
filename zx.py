Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
====================== RESTART: C:\emmmmmm\old file.py ======================
>>> mi = minimize()
>>> next(mi)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    next(mi)
  File "C:\emmmmmm\old file.py", line 4, in minimize
    alist.append(val)
UnboundLocalError: local variable 'val' referenced before assignment
>>> 
====================== RESTART: C:\emmmmmm\old file.py ======================
>>> mi = minimize()
>>> next(mi)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    next(mi)
  File "C:\emmmmmm\old file.py", line 3, in minimize
    for val in alist:
UnboundLocalError: local variable 'alist' referenced before assignment
>>> 
====================== RESTART: C:\emmmmmm\old file.py ======================
>>> mi = minimize()
>>> next(mi)
>>> mi.send(1)
1
>>> mi.send(2)
2
>>> 
>>> 
====================== RESTART: C:\emmmmmm\old file.py ======================
>>> mi = minimize()
>>> next(mi)
>>> mi.send([1,2,3,4,5])
1
>>> 
====================== RESTART: C:\emmmmmm\old file.py ======================
>>> mi = minimize()
>>> mi.send(1)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    mi.send(1)
TypeError: can't send non-None value to a just-started generator
>>> mi.send(None)
>>> mi.send(1)
1
>>> mi.send(2)
2
>>> mi.send(3)
3
>>> 
====================== RESTART: C:\emmmmmm\old file.py ======================
>>> mi = minimize()
>>> mi.send(1)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    mi.send(1)
TypeError: can't send non-None value to a just-started generator
>>> mi.send(None)
>>> mi.send(1)
1
>>> mi.send(2)
1
>>> mi.send(3)
1
>>> 
====================== RESTART: C:\emmmmmm\new file.py ======================
>>> con = consumer()
>>> p = producer(con)
>>> next(p)
producer ready
>>> next(con)
1 ready
>>> p.send(1)
1
None
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    p.send(1)
  File "C:\emmmmmm\new file.py", line 9, in producer
    consumer.send(value)
AttributeError: 'NoneType' object has no attribute 'send'
>>> p.send(None)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    p.send(None)
StopIteration
>>> 
====================== RESTART: C:\emmmmmm\new file.py ======================
>>> con = consumer()
>>> p = producer(con)

>>> next(p)
producer ready
>>> next(con)
1 ready
>>> p.send(1)
1
None
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    p.send(1)
  File "C:\emmmmmm\new file.py", line 8, in producer
    consumer.send(val)
AttributeError: 'NoneType' object has no attribute 'send'
>>> 
====================== RESTART: C:\emmmmmm\new file.py ======================
>>> con = consumer()
>>> p = producer(con)
>>> next(p)
producer ready
>>> next(con)
1 ready
>>> p.send(1)
1
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    p.send(1)
  File "C:\emmmmmm\new file.py", line 7, in producer
    consumer.send(val)
UnboundLocalError: local variable 'consumer' referenced before assignment
>>> 
====================== RESTART: C:\emmmmmm\new file.py ======================
>>> con = consumer()
>>> p = producer(con)
>>> next(p)
producer ready
>>> next(con)
1 ready
>>> p.send(1)
1
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    p.send(1)
  File "C:\emmmmmm\new file.py", line 7, in producer
    for consumer in consumers:
  File "C:\emmmmmm\new file.py", line 21, in consumer
    v = min(alist)
TypeError: '<' not supported between instances of 'NoneType' and 'int'
>>> 
====================== RESTART: C:\emmmmmm\new file.py ======================
>>> con = consumer()
>>> p = producer(con)
>>> next(p)
producer ready
>>> next(con)
1 ready
>>> p.send(None)
None
None
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    p.send(None)
  File "C:\emmmmmm\new file.py", line 8, in producer
    consumer.send(val)
AttributeError: 'NoneType' object has no attribute 'send'
>>> 
