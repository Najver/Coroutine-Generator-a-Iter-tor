def chatbot():
    yield "Ahoj jak se mas?"

    odpoved = yield

    if(odpoved =="Konec"):
        yield "Loucim se"
    elif "co ty?" in odpoved:
        yield "Mam se dobre"
    else:
        yield "Nerozumim otazce"


chat = chatbot()  #nastartuje corutinu

print(next(chat))  #spusti prvni cast a pozdravi

next(chat)  #spusti druhou cast, ktera ocekava data
print(chat.send("ahoj, mam se dobre, co ty? "))  #posle data a nacte si vysledek

chat.close()  #ukonci corutinu