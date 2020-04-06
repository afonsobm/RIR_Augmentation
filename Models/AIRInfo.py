class AIRInfo:
    description: str
    frequency: int
    name: str

    def __init__(self, description: str, frequency: int, name: str) -> None:
        self.description = description
        self.frequency = frequency
        self.name = name

    __init__.__defaults__ = tuple(None for name in __init__.__code__.co_varnames)
