import uuid

class Gate:
    def __init__(self, nr_inputs, nr_outputs, type=None) -> None:
        self.nr_inputs = nr_inputs
        self.nr_outputs = nr_outputs
        self.type = type
        self.inputs = {}
        self.inp_values = []
        self.outputs = {}
        self.id = str(uuid.uuid4())
    
    def appendInput(self, b):
        b.appendRight(self)
        self.inputs[len(list(self.inputs.keys()))] = b
    
    def appendOutput(self, b):
        self.outputs[len(list(self.outputs.keys()))] = b

    def recieve(self, value, x):
        # rerun the processing
        self.inp_values.append(value)
        if len(self.inp_values) < self.nr_inputs:
            self.send(value)
    
    def send(self, y):
        for x in list(self.outputs.keys()):
            self.outputs[x].recieveLeft(y)

    def toJson(self):
        return {
            "leftNodes": [self.inputs[x].id for x in self.inputs],
            "rightNodes": [self.inputs[x].id for x in self.outputs],
            "type": self.type,
            "id": self.id
        }