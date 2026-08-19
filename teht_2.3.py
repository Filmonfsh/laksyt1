#Kysytään suorakulmio kanta ja korkea
kanta = float(input("Anna kanta: "))
korkea = float(input("Anna korkea: "))

#Lasketaan pinta-ala ja piiri
pinta_ala = kanta * korkea
piiri = 2 * kanta + 2 * korkea

#Tulostetaan tulos
print("pinta ala: ", pinta_ala)
print("piiri: ", piiri)