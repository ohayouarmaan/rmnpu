import uuid

class Bus:
    def __init__(self) -> None:
        self.rightNodes = {}
        self.id = str(uuid.uuid4())
    
    def appendRight(self, g):
        self.rightNodes[g.id] = g
    
    def recieveLeft(self, value):
        self.leftNode = value
        for x in list(self.rightNodes.keys()):
            self.rightNodes[x].recieve(value, x)
    
    def toJson(self):
        return {
            "rightNodes": [x for x in self.rightNodes],
            "leftNode": self.leftNode,
            "id": self.id
        }
