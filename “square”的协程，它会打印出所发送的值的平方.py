def square():
    while True:
        val = yield
        print(val*val)
        
