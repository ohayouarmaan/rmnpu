from Gate import Gate
from Bus import Bus
from OrGate import OrGate
from notGate import NotGate

class NorGate(Gate):
    def __init__(self) -> None:
        super().__init__(2, 1, "NorGate")
        self.b1 = Bus()
        self.b2 = Bus()
        self.b3 = Bus()
        self.b4 = Bus()
        self.g = OrGate()
        self.n = NotGate()
        self.g.appendInput(self.b1)
        self.g.appendInput(self.b2)
        self.g.appendOutput(self.b3)
        self.n.appendInput(self.b3)
        self.n.appendOutput(self.b4)

        # self.b1.appendRight(self.g)
        # self.b2.appendRight(self.g)
        # self.b3.appendRight(self.n)
    
    def process(self):


        self.b1.recieveLeft(self.inputs[0].leftNode)
        self.b2.recieveLeft(self.inputs[1].leftNode)

        self.g.process()
        self.n.process()
        self.values = [ self.b4.leftNode ]
        self.send(self.b4.leftNode)

