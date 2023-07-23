from Gate import Gate

class NotGate(Gate):
    def __init__(self) -> None:
        super().__init__(1, 1, "NotGate")

    def process(self):
        if(len(self.inputs.keys()) < self.nr_inputs):
            raise Exception("inputs underflow error")
        else:
            if self.inputs[0].leftNode == 0:
                self.values = [1]
                self.send(1)
            else:
                self.values = [0]
                self.send(0)
