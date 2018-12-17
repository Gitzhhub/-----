def minimize():
    alist = []
    while True:
            val = yield
            if val >= 1:
                alist.append(val)
                v = min(alist)
            print(v)

mi = minimize() 
mi.send(None)
mi.send(1)
mi.send(2)
mi.send(3)
mi.send(4)
mi.send(5)
