from NandGate import NandGate
from notGate import NotGate
from Gate import Gate
from Bus import Bus

class OrGate(Gate):
    def __init__(self) -> None:
        super().__init__(2, 1, "OrGate")
        self.b1 = Bus()
        self.b2 = Bus()
        self.b3 = Bus()
        self.b4 = Bus()
        self.b5 = Bus()
        self.n1 = NotGate()
        self.n2 = NotGate()
        self.nand = NandGate()

        self.n1.appendInput(self.b1)
        self.n2.appendInput(self.b2)
        self.n1.appendOutput(self.b3)
        self.n2.appendOutput(self.b4)
        self.nand.appendInput(self.b3)
        self.nand.appendInput(self.b4)
        self.nand.appendOutput(self.b5)

        # self.b1.appendRight(self.n1)
        # self.b2.appendRight(self.n2)

        # self.b3.appendRight(self.nand)
        # self.b4.appendRight(self.nand)

    def process(self):
        
        self.b1.recieveLeft(self.inputs[0].leftNode)
        self.b2.recieveLeft(self.inputs[1].leftNode)

        self.n1.process()
        self.n2.process()
        self.nand.process()
        self.values = [ self.b5.leftNode ]
        self.send(self.b5.leftNode)

