"""Task 3"""
print("Task 3 started")

lambdaFuncResult = lambda b1, b2, X : b1 + b2 * X
print("Enter b1:")
b1 = int(input())
print("Enter b2:")
b2 = int(input())
print("Enter X:")
X = int(input())

print("lambdaFuncResult: " + str(lambdaFuncResult(b1,b2,X)))
