parola_uno = input("Inserisci la prima parola: ")
parola_due = input("Ineserisci la seconda parola: ")
parola_tre = input("Inserisci la terza parola: ")


if parola_uno <= parola_due and parola_uno <= parola_tre:
    primo = parola_uno
    if parola_due <= parola_tre:
        secondo = parola_due
        terzo = parola_tre
    else:
        secondo = parola_tre
        terzo = parola_due

if parola_due <= parola_uno and parola_due <= parola_tre:
    primo = parola_due
    if parola_uno < parola_tre:
        secondo = parola_uno 
        terzo = parola_tre
    else:
        secondo = parola_tre
        terzo = parola_uno

if parola_tre <= parola_due and parola_tre <= parola_uno:
    primo = parola_tre
    if parola_uno < parola_due:
        secondo = parola_uno
        terzo = parola_due
    else:
        secondo = parola_due
        terzo = parola_uno

print(f"Ordine alfabetico: {primo}, {secondo}, {terzo}")