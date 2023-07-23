from Gate import Gate

class AND_GATE(Gate):
    def __init__(self) -> None:
        super().__init__(2, 1, type="AndGate")

    def process(self):
        if(len(self.inputs.keys()) < self.nr_inputs):
            raise Exception("inputs underflow error")
        else:
            if self.inputs[0].leftNode == 1 and self.inputs[1].leftNode == 1:
                self.values = [1]
                self.send(1)
            else:
                self.values = [0]
                self.send(0)
