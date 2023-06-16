from dataclasses import dataclass
from .pessoa import Pessoa

@dataclass
class Usuario:
    email : str
    pessoa: Pessoa
    
    