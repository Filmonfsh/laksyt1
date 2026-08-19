#Kysytään massalukuja
leiviskat = float(input(f"Anna leiviskät: " ))
naula = int(input("Anna naula: "))
luoti = int(input("Anna luoti: "))

# Massan arvot muuttujiin
gram_leiviska = 20 * 32 * 13.3
gram_naula = 32 * 13.3
gram_luoti = 13.3

#Lasketaan massalukuja
yhteensa_grammoina = leiviskat * gram_leiviska + naula * gram_naula + luoti * gram_luoti
kilogrammja = int(yhteensa_grammoina // 1000)
jaljella_grammoja = yhteensa_grammoina % 1000

#Tulostetaan arvot
print ("Tulos, ", kilogrammja, "kg", jaljella_grammoja , "gramma")