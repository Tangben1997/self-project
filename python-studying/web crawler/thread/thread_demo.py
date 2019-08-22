
import threading
import time

def coding():
    for x in range(3):
        print('coding...........')
        time.sleep(1)
        print(threading.current_thread())

def drawing():
    for x in range(3):
        print('drawing..........')
        time.sleep(1)

def main():
    t1 = threading.Thread(target=coding)
    t2 = threading.Thread(target=drawing)
    t1.start()
    t2.start()
    print(threading.enumerate())

if __name__ == '__main__':
    main()