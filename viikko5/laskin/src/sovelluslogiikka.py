class Sovelluslogiikka:
    def __init__(self, tulos=0):
        self.tulos = tulos
        self.edellinen = [tulos]

    def miinus(self, arvo):
        self._tallenna_edellinen()
        self.tulos = self.tulos - arvo

    def plus(self, arvo):
        self._tallenna_edellinen()
        self.tulos = self.tulos + arvo

    def nollaa(self):
        self._tallenna_edellinen()
        self.tulos = 0

    def kumoa(self):
        if len(self.edellinen) > 0:
            self.tulos = self.edellinen.pop()

    def aseta_arvo(self, arvo):
        self._tallenna_edellinen()
        self.tulos = arvo

    def _tallenna_edellinen(self):
        self.edellinen.append(self.tulos)