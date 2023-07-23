from andGate import AND_GATE
import json
from Bus import Bus
from notGate import NotGate
from NandGate import NandGate
from OrGate import OrGate
from NorGate import NorGate
from Circuit import Circuit
from DFF import DFF
from DLatch import DLatch


if __name__ == "__main__":
    """
    A bus should have two ends left end and the right end
    and the left end must have only one edge where as the right end should have multiple ends

    when a bus is given a value from the left end it passes the signal to the right end
    and it loops through all the edges in the right end and passes that signal to all of those nodes

    now a gate will have two functions related to communication one being recieve and one being send
    the recieve will be the function which should be called by the bus and the bus will pass down the data with an id
    the gate will save all the input busses within a hashmap where the key will be an id and the value will be the bus itself
    """
    x0 = Bus()
    x1 = Bus()
    x2 = Bus()
    y0 = Bus()
    y1 = Bus()
    y2 = Bus()
    a1 = AND_GATE()
    a2 = AND_GATE()

    a1.appendInput(x0)
    a1.appendInput(x1)
    a1.appendOutput(y1)
    a2.appendInput(y1)
    a2.appendInput(x2)
    a2.appendOutput(y2)

    x0.recieveLeft(1)
    x1.recieveLeft(1)
    x2.recieveLeft(1)
    a1.process()
    a2.process()
    c = Circuit(3, 1)
    c.appendBus(x0)
    c.appendBus(x1)
    c.appendBus(x2)
    c.appendBus(y1)
    c.appendBus(y2)
    c.appendGate(a1)
    c.appendGate(a2)
    c.appendInput(x0)
    c.appendInput(x1)
    c.appendInput(x2)
    c.appendOutput(y2)

    c.export("./BuiltCircuits/threeWayAndGate.json")

