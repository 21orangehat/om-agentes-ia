from dataclasses import dataclass

@dataclass
class UserInfo():
    """
    Classe para representar informações
    de usuário, como nome e cargo em uma
    empresa.
    """
    nome: str
    cargo: str
