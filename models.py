from dataclasses import dataclass
from typing import List

@dataclass
class UserInfo():
    """
    Classe para representar informações
    de usuário, como nome e cargo em uma
    empresa.
    """
    nome: str
    cargo: str


@dataclass
class Compra():
    """
    Classe para representar informações
    de uma compra, contendo o produto e o preço.
    """
    id: str
    produto: str
    preco: float

@dataclass
class Cliente():
    """
    Classe para representar informações
    de um cliente, contendo o id, nome e lista de compras.
    """
    id: str
    nome: str
    compras: List[Compra]
    novo: bool = True
    
    def get_recent_purchases(self, n: int = 3) -> List[Compra]:
        """
        Método da classe Cliente que retorna as 3 últimas compras.
        """
        return self.compras[-n:]
