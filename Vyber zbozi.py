zelenina = ["zelí", "okurka", "rajče", "paprika", "ředkev", "mrkev", "brokolice"]
ovoce = ["jablko", "hruška", "pomeranč", "jahoda", "banán", "kiwi", "malina"]
pocet_pokusu = 0
dalsi_pokus = "ano"
while dalsi_pokus == "ano":
   zapis =input("Zadej název libovolného ovoce nebo zeleniny:")
   if zapis in zelenina:
    print("Zadal jsi zeleninu")
   elif zapis in ovoce:
    print ("Zadal jsi ovoce")
   else: print ("Tvoje slovo nemám v seznamu")
   pocet_pokusu +=1
   dalsi_pokus = input("Přeješ si zadat další slovo? (ano/ne) ")
print("Zadal jsi", pocet_pokusu, "slov")