from threading import Lock
from typing import Callable

class Foo:
    def __init__(self):
        self.lock1 = Lock()
        self.lock2 = Lock()
        self.lock1.acquire()
        self.lock2.acquire()


    def first(self, printFirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.lock1.release()
        


    def second(self, printSecond: 'Callable[[], None]') -> None:
        with self.lock1:
            # printSecond() outputs "second". Do not change or remove this line.
            printSecond()
            self.lock2.release()


    def third(self, printThird: 'Callable[[], None]') -> None:
        with self.lock2:
            # printThird() outputs "third". Do not change or remove this line.
            printThird()