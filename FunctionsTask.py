import time

"""Task 1"""
def Delay(x):
    print("Delay started\nStart time: " + time.ctime(time.time()))
    time.sleep(x)
    print("Delay ended\nEnd time: " + time.ctime(time.time()))

print("TASK 1")

print("Enter delay in seconds: ")
x = int(input())
Delay(x)
"""//////////////////////////////////////////////////"""

"""Task 3"""
print("TASK 3")

lambdaFuncResult = lambda b1, b2, X : b1 + b2 * X
print("Enter b1:")
b1 = int(input())
print("Enter b2:")
b2 = int(input())
print("Enter X:")
X = int(input())

print("lambdaFuncResult: " + str(lambdaFuncResult(b1,b2,X)))
"""//////////////////////////////////////////////////"""
