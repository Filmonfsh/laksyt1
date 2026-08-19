sukupuoli = input("Anna biologinen sukupuoli (nainen/mies): ")
hemoglobiini = float(input("Anna hemoglobiiniarvo (g/l): "))

if sukupuoli == "nainen":
    if hemoglobiini < 117:
        print("Hemoglobiiniarvo on alhainen")
    elif hemoglobiini > 175:
        print("Hemoglobiiniarvo on korkea")
    else:
        print("Hemoglobiiniarvo on normaali")

elif sukupuoli == "mies":
    if hemoglobiini < 134:
        print("Hemoglobiiniarvo on alhainen")
    elif hemoglobiini > 195:
        print("Hemoglobiiniarvo on korkea")
    else:
        print("Hemoglobiiniarvo on normaali")
else:
    print("Tuntematon sukupuoli. Anna 'nainen' tai 'mies'.")