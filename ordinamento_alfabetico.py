print ('''
------ Programma di Ordinamento Alfabetico ------
*************************************************
------------- ORDINAMENTO DI PAROLE -------------
*************************************************
Questo programma ti chiederà di inserire tre parole
e le ordinerà in ordine alfabetico.

''')

parola_uno = input("Inserisci la prima parola: ")
parola_due = input("Ineserisci la seconda parola: ")
parola_tre = input("Inserisci la terza parola: ")

#controllo che la parola uno venga prima o sia uguale rispetto alla due e della tre
if parola_uno <= parola_due and parola_uno <= parola_tre:
    primo = parola_uno
    #confronto per capire quale viene prima tra la due e la tre
    if parola_due <= parola_tre:
        secondo = parola_due
        terzo = parola_tre
    else:
        secondo = parola_tre
        terzo = parola_due

#stesso controlla ma con la due
if parola_due <= parola_uno and parola_due <= parola_tre:
    primo = parola_due
    #confronto per capire quale viene prima tra la uno e la tre
    if parola_uno < parola_tre:
        secondo = parola_uno 
        terzo = parola_tre
    else:
        secondo = parola_tre
        terzo = parola_uno

#stesso controllo ma con la tre
if parola_tre <= parola_due and parola_tre <= parola_uno:
    primo = parola_tre
    #confronto per capire quale viene prima tra la uno e la due
    if parola_uno < parola_due:
        secondo = parola_uno
        terzo = parola_due
    else:
        secondo = parola_due
        terzo = parola_uno

print(f'''
      
Ordine alfabetico: {primo}, {secondo}, {terzo}''')