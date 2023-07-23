from NorGate import NorGate
from andGate import AND_GATE
from OrGate import OrGate
from NandGate import NandGate
from notGate import NotGate
from DFF import DFF
from DLatch import DLatch

nor = NorGate()
nand = NandGate()
o = OrGate()
ng = NotGate()
a = AND_GATE()

ALL_GATES = {
    "NorGate": NorGate,
    "NandGate": NandGate,
    "OrGate": OrGate,
    "NotGate": NotGate,
    "AndGate": AND_GATE,
    "DFFE": DFF,
    "DLatch": DLatch
}
