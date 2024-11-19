class GeneratorKrasovychJezer:
    i = 0
    j = 0

    jezera = [
        ["Dyje", ["Křivé jezero", "Květné jezero", "Kutnar", "Mahenovo jezero"]],
        ["Labe", ["Babinecká tůň", "Hrbáčkovy tůně"]],
        ["Bílina", ["Komořanské jezero"]],
        ["(bez řeky)", ["Antošovické jezero", "Holásecká jezera", "Krňák", "Kurfürstovo rameno", "Malá říčka", "Podhradská tůň"]]
    ]

    def __iter__(self):
        self.i = 0
        self.j = 0
        return self

    def __next__(self):
        if self.i >= len(self.jezera):
            raise StopIteration()

        reka = self.jezera[self.i][0]
        jezeraNaRece = self.jezera[self.i][1]

        if self.j >= len(jezeraNaRece):
            self.i += 1
            self.j = 0
            return self.__next__()

        jezero = jezeraNaRece[self.j]
        self.j += 1

        if reka != "(bez řeky)":
            jezero += f" ({reka})"

        return jezero


for jezero in GeneratorKrasovychJezer():
    print(jezero)
