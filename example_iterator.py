import time

class FiboIter():

    def __init__(self):
        pass
    
    def __iter__(self):
        self.n1 = 0
        self.n2 = 1
        self.counter = 0
        return self

    def __next__(self):
        if self.counter == 0:
            self.counter += 1
            return self.n1
        elif self.counter == 1:
            self.counter += 1
            return self.n2
        else:
            self.counter += 1
            self.n2, self.n1 = self.n1 + self.n2, self.n2
            return self.n2

if __name__ == "__main__":
    fibo = FiboIter()
    for i in fibo:
        if i < 100:
            print(i)
            time.sleep(0.25)
        else:
            break