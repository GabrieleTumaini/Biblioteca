class Libro:
    def __init__(self, titolo: str, autore: str, anno: int, editore: str, pagine: int) -> None:
        self.titolo = titolo
        self.autore = autore
        self.anno = anno
        self.editore = editore
        self.pagine = pagine

    def reading_time(self) -> str:
        if self.pagine < 100:
            return "1 ora"
        if self.pagine <= 200:
            return "2 ore"
        return "più di 2 ore"

    def __str__(self) -> str:
        return f"{self.titolo} - {self.autore} ({self.anno}), {self.pagine} pagine"