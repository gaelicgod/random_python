#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3

# testing how to make a fibonacci func
def fibs(currentNum) -> int:
    limiter = 10
    startNum, nextNum = 0, 1
    while currentNum < limiter:
        #print("iter => " , str(currentNum))
        yield startNum
        startNum, nextNum = nextNum, startNum + nextNum
        currentNum += 1
    return currentNum

if __name__ == '__main__':
    counter = 2
    num = fibs(counter)
    for i in num:
        print(i, " ", end="")
    print(type(num))


[int(i) for i in str('111')]