def magic_division(*args):
    for i in args:
        x = str(i)
        sum = 0
        for j in range(0, len(x)):
            sum += int(x[j])
        if(int(x)%sum == 0):
            print("{0} / {1} = {2}".format(int(x), sum,int(x)//sum))

magic_division(111, 222, 333, 444, 555, 666, 777, 888, 999)



