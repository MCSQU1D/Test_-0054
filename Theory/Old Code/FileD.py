


while True:

    Temperature = float(input("Temp: "))
    Atom_Temperature = float(input("Atom Temp: "))

    if Atom_Temperature < Temperature:
        Atom_Temperature += 1/10*(Temperature - Atom_Temperature)
    if Atom_Temperature > Temperature:
        Atom_Temperature += 1/10*(Temperature - Atom_Temperature)

    print(Temperature)
    print(Atom_Temperature)
