def generatorRaselinnychJezerCR():
    try:
        yield "Černé jezero"  # Největší jezero na Šumavě
        yield "Čertovo jezero"  # Šumava
        yield "Plešné jezero"  # Šumava
        yield "Prášilské jezero"  # Šumava
        yield "Mechové jezírko"  # Rezervace SOOS u Františkových Lázní
    except GeneratorExit:
        print("Generovani preruseno")

print("Rašelinná jezera v ČR")
for jezero in generatorRaselinnychJezerCR():
    print(jezero)
    input("zadej hodnotu")
