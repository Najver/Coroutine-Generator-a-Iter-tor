def generatorRaselinnychJezerCR():
    try:
        yield "Černé jezero"  # Největší jezero na Šumavě
        yield "Čertovo jezero"  # Šumava
        yield "Plešné jezero"  # Šumava
        yield "Prášilské jezero"  # Šumava
        yield "Mechové jezírko"  # Rezervace SOOS u Františkových Lázní
    except StopIteration:
        print("Generovani preruseno")



jezera = generatorRaselinnychJezerCR()
print("Rašelinná jezera v ČR")
while(jezera):
    print(next(jezera))


