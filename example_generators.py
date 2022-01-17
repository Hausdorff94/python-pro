import time

def fibo_generator():
    n1=0
    n2=1
    counter = 0

    while True:
        if counter==0:
            counter+=1
            yield n1
        elif counter==1:
            counter+=1
            yield n2
        else:
            counter+=1
            n2, n1 = n1 + n2, n2
            yield n2

if __name__ == "__main__":
    fibo = fibo_generator()
    for i in fibo:
        if i < 100:
            print(i)
            time.sleep(0.25)
        else:
            break