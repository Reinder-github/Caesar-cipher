def verhul(tekst):
    teVertalen = tekst
    nieuweLetters = []
    
    for i in range (len(teVertalen)):
        positie = ord(teVertalen[i])
        if positie < 97 or positie > 122:
            nieuwePositie = positie
        else:
            nieuwePositie = positie + 3
        if nieuwePositie > 122 and positie < 123 and positie > 119:
            nieuwePositie = nieuwePositie - 26
        letterNieuw = chr(nieuwePositie)
        nieuweLetters.append(letterNieuw)
    geheim = ""
    geheim = geheim.join(nieuweLetters)
    return geheim

def onthul(tekst):
    teVertalen = tekst
    nieuweLetters = []
    
    for i in range (len(teVertalen)):
        positie = ord(teVertalen[i])
        if positie < 97 or positie > 122:
            nieuwePositie = positie
        else:
            nieuwePositie = positie - 3
        if nieuwePositie < 97 and positie < 100 and positie > 98:
            nieuwePositie = nieuwePositie + 26
        letterNieuw = chr(nieuwePositie)
        nieuweLetters.append(letterNieuw)
    geheim = ""
    geheim = geheim.join(nieuweLetters)
    return geheim

def keuze():
    print("Caesarrotatie\nVersleutelen met de caesarrotatie")
    keuze = input("Wil je gaan Versleutelen? Of wil je gaan Ontsleutelen? Typ je antwoord: ")
    if (keuze.lower() == "ontsleutelen"):
        caesar = input("Welk woord wil je gaan ontsleutelen? ")
        geheimtaal = onthul(caesar.lower())
        print("Resultaat: " + geheimtaal)
    elif (keuze.lower() == "versleutelen"):
        caesar = input("Welk woord wil je gaan versleutelen? ")
        woord = verhul(caesar.lower())
        print("Resultaat: " + woord)
     
keuze()
    

