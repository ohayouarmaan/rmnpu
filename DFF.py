from Gate import Gate
from Bus import Bus
from andGate import AND_GATE
from NandGate import NandGate
from NorGate import NorGate

class DFF(Gate):
    def __init__(self) -> None:
        super().__init__(2, 1, "DFFE")
        self.busses = []
        self.b1 = Bus()
        self.b2 = Bus()
        self.b3 = Bus()
        self.b4 = Bus()
        self.b5 = Bus()
        self.o1 = NorGate()
        self.o2 = NorGate()

        self.o1.appendInput(self.b1)
        self.o1.appendOutput(self.b3)
        self.o1.appendInput(self.b4)
        self.o2.appendInput(self.b2)
        self.o2.appendInput(self.b3)
        self.o2.appendOutput(self.b4)
        self.o2.appendOutput(self.b5)
    
        self.b1.appendRight(self.o1)
        self.b2.appendRight(self.o2)
        self.b3.appendRight(self.o2)
        self.b4.appendRight(self.o1)


    def process(self):
        self.b1.recieveLeft(self.inputs[0].leftNode)
        self.b2.recieveLeft(self.inputs[1].leftNode)

        self.o1.process()
        self.o2.process()

        self.values = [ self.b5.leftNode ]
        self.send(self.values[0])

