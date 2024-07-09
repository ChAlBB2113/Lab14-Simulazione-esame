from dataclasses import dataclass

@dataclass
class Interaction():
    GeneID1: str
    GeneID2: str
    Type: str
    Expression_Corr: float

