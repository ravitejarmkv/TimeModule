import time


def calcProd():
    product = 1
    for i in range(1, 10000):
        product = product * i
    return product


startTime = time.time()
prodTime = calcProd()
endTime = time.time()
print("The digit is {} digits long.".format(len(str(prodTime))))
print("Took {} long to calculate.".format(endTime- startTime))
