from Bus import Bus
from andGate import AND_GATE
from notGate import NotGate
from NandGate import NandGate
from DFF import DFFE
import matplotlib.pyplot as plt
import random

basic_clock = 0
b1 = Bus()
b2 = Bus()
b3 = Bus()
b4 = Bus()
b5 = Bus()
b6 = Bus()
b7 = Bus()
b8 = Bus()

n = NotGate()
dlatch1 = DFFE()
dlatch2 = DFFE()

dlatch1.appendInput(b1)
n.appendInput(b2)
n.appendOutput(b3)
dlatch1.appendInput(b3)
dlatch1.appendOutput(b4)
dlatch2.appendInput(b4)
dlatch2.appendInput(b2)
dlatch2.appendOutput(b7)

b2.appendRight(n)
b2.appendRight(b7)
b1.appendRight(dlatch1)
b3.appendRight(dlatch1)
b4.appendRight(dlatch2)
b2.appendRight(dlatch2)

data = {}

def printData(ds):
    y_axis = ds.values()
    str = u""
    prev = None
    for y in y_axis:
        if prev is not None:
            if prev != y:
                str += "|"

        if y == 0:
            str += "__"
        else:
            str += u"\u0305 \u0305 "
        prev = y
    
    print(str)


random_data = [random.choice([0, 1]) for _ in range(25)]

print(random_data)
for i in range(25):
    b1 = Bus()
    basic_clock = int(not basic_clock)


printData(data)
print(" ".join(map(lambda x: str(x), list(data.values()))))
print(data)