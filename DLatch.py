from Gate import Gate
from Bus import Bus
from DFF import DFF
from andGate import AND_GATE
from notGate import NotGate

class DLatch(Gate):
    def __init__(self) -> None:
        super().__init__(2, 1, "DLatch")
        self.b1 = Bus()
        self.b2 = Bus()
        self.b3 = Bus()
        self.b4 = Bus()
        self.b5 = Bus()
        self.b6 = Bus()
        self.dff = DFF()
        self.a1 = AND_GATE()
        self.n = NotGate()
        self.a2 = AND_GATE()

        self.a1.appendInput(self.b1)
        self.a1.appendInput(self.b2)
        self.a1.appendOutput(self.b3)

        self.n.appendInput(self.b1)
        self.n.appendOutput(self.b4)

        self.a2.appendInput(self.b2)
        self.a2.appendInput(self.b4)
        self.a2.appendOutput(self.b5)
        
        self.dff.appendInput(self.b3)
        self.dff.appendInput(self.b5)
        self.dff.appendOutput(self.b6)
    
    def process(self):
        self.b1.recieveLeft(self.inputs[0].leftNode)
        self.b2.recieveLeft(self.inputs[1].leftNode)
        
        self.n.process()
        self.a1.process()
        self.a2.process()
        self.dff.process()

        self.values = [ self.b6.leftNode ]
        self.send(self.b6.leftNode )
    
