def konverzace():
    yield "Dobrý den"

    jmeno = yield "Jak se jmenuješ?"

    yield "Zdravím Tě "+ str(jmeno)

    yield "Naschledanou"

k = konverzace()

odpoved = next(k) #posun k prvnimu yieldu
print(odpoved)

odpoved = next(k) #posun k druhemu yieldu + zacatek naslouchani vstupu
print(odpoved)

odpoved = k.send("Ondra")  #poslani vstypu + posun na treti yield
print(odpoved)

odpoved = next(k) #posun na ctvrty yield
print(odpoved)
k.close()


ko = konverzace()

odpoved = ko.send(None) #posun k prvnimu yieldu
print(odpoved)

odpoved = ko.send(None) #posun k druhemu yieldu + zacatek naslouchani vstupu
print(odpoved)

odpoved = ko.send("Petr") #poslani vstypu + posun na treti yield
print(odpoved)

odpoved = ko.send(None) #posun na ctvrty yield
print(odpoved)
ko.close()