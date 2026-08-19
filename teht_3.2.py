print("Tervetuloa valitsemaan seuraavista hyttiluokista.!")
print("LUX")
print("A")
print("B")
print("C")
hytti = input("Valitse hytti luokat: " )


if "lux" == hytti:
    print("LUX on parvekkeellinen hytti yläkannella. ")
elif "a" == hytti:
    print("A on ikkunallinen hytti autokannen yläpuolella. ")
elif "b" == hytti:
    print("B on ikkunaton hytti autokannen yläpuolella.")
elif "c" == hytti:
    print("C on ikkunaton hytti autokannen alapuolella.")

else:
    print("Virheellinen hyttiluokka")