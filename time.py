from multiprocessing import Process
import time

def f(name):
    s = 0
    m = 0
    h = 0
    while s <= 60:
        print(h, 'Hours', m, 'Minutes', s, 'Seconds')
        time.sleep(1)
        s += 1
        if s == 60:
            m += 1
            s = 0
        elif m == 60:
            h += 1
            m = 0
            s = 0

def d(name):
    print('test2', name)
    time.sleep(2)
    print('test2', name)
    time.sleep(2)
    print('test2', name)
    time.sleep(2)

if __name__ == '__main__':
    p1 = Process(target=f, args=('bob',))
    p2 = Process(target=d, args=('alice',))
    p1.start()
    p2.start()
    p1.join()
    p2.join()