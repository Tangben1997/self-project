import threading
import random
import time

gMoney = 1000
gLock = threading.Lock()
gTotalTimes = 10
gTimes = 0


class Producer(threading.Thread):
    def run(self):
        global gMoney
        global gTimes
        while (True):
            money = random.randint(100, 1000)
            gLock.acquire()
            if gTimes >= 10:
                gLock.release()
                break
            gMoney += money
            gTimes += 1
            print('%s生产了%d元钱，总共剩余%d元钱' % (threading.current_thread().name, money, gMoney))
            gLock.release()
            time.sleep(1)


class Consumer(threading.Thread):
    def run(self):
        global gMoney
        global gTimes
        while (True):
            money = random.randint(100, 1000)
            gLock.acquire()
            if gMoney >= money:
                gMoney -= money
                print('%s消费了%d元钱，总共剩余%d元钱' % (threading.current_thread().name, money, gMoney))
            else:
                if gTimes >= gTotalTimes:
                    gLock.release()
                    break
                print('%s想花%d元钱，但是只剩%d元钱不够花' % (threading.current_thread().name, money, gMoney))
            gLock.release()
            time.sleep(1)


def main():
    for x in range(3):
        t = Producer(name='生产员%d号' % x)
        t.start()

    for x in range(4):
        t = Consumer(name='消费者%d号' % x)
        t.start()


if __name__ == '__main__':
    main()
