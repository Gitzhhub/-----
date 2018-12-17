def producer(consumers):
    print( 'producer ready')
    count = 0
    try:
        while True:
            val = yield
            count += 1
            if count%2 == 0:
                for consumer1 in consumers:
                    consumer1.send(val*val)
            else:
                for consumer2 in consumers:
                    consumer2.send(val*val)

    except GeneratorExit:
        for consumer in consumers:
            consumer.close()

def consumer1():
    alist1 = []
    print('1 ready')
    try:
        while True:
            val = yield
            if val >= 1:
                alist1.append(val)
                v = min(alist1)
                print('min',v)
    except GeneratorExit:
        print('1 close',alist1)
def consumer2():
    alist2 = []
    print('2 ready')
    try:
        while True:
            val = yield
            if val >= 1:
                alist2.append(val)
                v = max(alist2)
                print('max',v)
    except GeneratorExit:
        print('2 close',alist2)
con1=consumer1()
con2=consumer2()
p=producer([con1,con2])
next(p)
next(con1)
next(con2)
p.send(1)
p.send(2)
p.send(3)
p.send(4)
p.send(5)
p.close()
