class Kategoria:
    def __init__(self, beolvasott_sor:str) -> None:
        darabok:list[str] = beolvasott_sor.strip().split(';')
        self.kategoria_nev:str = darabok[0]
        self.tulelok_szama:int = int(darabok[1])
        self.eltuntek_szama:int = int(darabok[2])