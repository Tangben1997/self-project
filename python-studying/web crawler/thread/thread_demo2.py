import threading
import time

class codingthread(threading.Thread):
    def run(self):
        for x in range(3):
            print('coding...........')
            time.sleep(1)

class drawingthreaad(threading.Thread):
    def run(self):
        for x in range(3):
            print('drawing...................')
            time.sleep(1)


if __name__ == '__main__':
    t1 = codingthread()
    t2 = drawingthreaad()

    t1.start()
    t2.start()