# https://leetcode.com/problems/print-in-order/
from threading import Semaphore
class Foo:
    def __init__(self):
        self.done=(Semaphore(0),Semaphore(0))


    def first(self, printFirst: 'Callable[[], None]') -> None:
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.done[0].release()


    def second(self, printSecond: 'Callable[[], None]') -> None:
        with self.done[0]:
            # printSecond() outputs "second". Do not change or remove this line.
            printSecond()
            self.done[1].release()


    def third(self, printThird: 'Callable[[], None]') -> None:
        with self.done[1]:
            # printThird() outputs "third". Do not change or remove this line.
            printThird()
        