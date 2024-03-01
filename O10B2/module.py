class Kategoria:
    def __init__(self, beolvasott_sor:str) -> None:
        darabok:list[str] = beolvasott_sor.strip().split(';')
        self.nev:str = darabok[0]
        self.tulelok:int = int(darabok[1])
        self.eltuntek:int = int(darabok[2])