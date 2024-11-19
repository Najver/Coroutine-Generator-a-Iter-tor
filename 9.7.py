def vydej_obedu():
    menu = [
         "vitamínový nápoj",
         "polévka česneková s bramborem",
         "segedínský guláš, houskové knedlíky",
         "rizek s bramborovou kasi",
         "jablko",
    ]
    yield f"{menu[0]}"
    jidlo = yield "Jake mas jidlo A nebo B?"
    if jidlo == "A":
        yield f"{menu[1]} \n{menu[2]} \n{menu[4]}"
    elif jidlo == "B":
        yield f"{menu[1]} \n{menu[3]} \n{menu[4]}"
    else:
        yield f"neni na menu"

corutina1 = vydej_obedu()
odpoved = next(corutina1)
print(odpoved)
odpoved = next(corutina1)
print(odpoved)
odpoved = corutina1.send("A")
print(odpoved)
corutina1.close()
