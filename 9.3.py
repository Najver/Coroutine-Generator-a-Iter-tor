def generatorITVelikanu():
    try:
        yield "Mark Zuckerberg"
        yield "Sergey Brin"
        yield  "Jan Koum"
    except GeneratorExit:
        print("Generovani preruseno")


print("Velikani v IT")
for osoba in generatorITVelikanu():
    print(osoba)

