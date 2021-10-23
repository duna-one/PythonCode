from typing import Final
import matplotlib.pyplot as plt
import numpy as np

class Adder:
    staticmethod
    def Sum(a, b):
        return a+b

class Amplifier:
    staticmethod
    def Amplify(K, value):
        return K*value

class InertionLink:

    def __init__(self):
        self.w = []
    pass
    
    def GetValue(self, value, T, i):
        if i-1<=0:
            self.w.append((value + 0 * T) / (1 + T))            
        else:
            self.w.append((value + self.w[i-1] * T)/(1 + T))
        return self.w[i]

"""Data input area"""
while(True):
    print("Enter the number of iterations(more than 100)")
    iterations_count = input()

    if not iterations_count.isdecimal():
        print("Incorrect input.")
        continue

    if int(iterations_count) < 100:
        print("Need more than 100")
        continue
    else:
        break


K1 = 4
K2 = -0.2
T1: Final = 0.1
T2: Final = 0.01
T3: Final = 0.01
DELTA: Final = 1 

while(True):
    print("Use the standard values K1 and K2?(Y/N)")
    inputValue = input()
    if inputValue == 'N':
        print("Enter K1:")
        K1 = int(input())
        print("Enter K2:")
        K2 = int(input())
        break
    elif inputValue == 'Y':
        print("The standard values K1=4 and K2=-0.2 are used")
        break
    else:
        print("Incorrect input.")
        continue
"""End of data input area"""

"""Magic Area"""
x = []
y = []
intermediateValue = 0
inertionLink_1 = InertionLink()
inertionLink_2 = InertionLink()
inertionLink_3 = InertionLink()
iterations_count = int(iterations_count)

for i in range(0, iterations_count):
    x.append(np.random.randint(-1*DELTA,DELTA+1))
    intermediateValue = Adder.Sum(x[i], intermediateValue)
    intermediateValue = Amplifier.Amplify(K1, intermediateValue)
    intermediateValue = inertionLink_1.GetValue(intermediateValue, T1, i)
    intermediateValue = inertionLink_2.GetValue(intermediateValue, T2, i)
    intermediateValue = inertionLink_3.GetValue(intermediateValue, T3, i)
    y.append(intermediateValue)
    intermediateValue = Amplifier.Amplify(K2, intermediateValue)
"""End of magic Area"""

"""Save to txt file area"""
_file = open("output.txt", 'w')
for i in range(0, iterations_count):
    _file.write(str(i) + ": " + str(x[i]) + ", " + str(y[i]) + "\n")
"""End of save to txt file area"""

"""Grafical output area"""
print("Input values are black, output values are red")
i = range(0, iterations_count)
plt.plot(i, x, color = 'k')
plt.plot(i, y, color = 'r')
plt.show()
"""End of grafical output area"""