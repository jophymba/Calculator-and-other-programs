zadana_veta = input("Zadejte větu: ")
veta = zadana_veta.lower()

samohlasky = 0 #  Nastavíme výchozí počty proměnných
souhlasky = 0
ostatni = 0
cisel = 0

samohlasky_sada = "aáeéěiíoóuúůyý" #  Definujeme sady typů znaků
souhlasky_sada = "bcčdďfghjklmnňpqrřsštťvwxzž"
cisla_sada = "0123456789"

for znak in veta: #  V hlavním cyklu programu analyzujeme druh a počet znaků
    if znak in samohlasky_sada:      # Nejprve samohlásky
        samohlasky += 1
    elif znak in souhlasky_sada:     # Pak souhlásky
        souhlasky += 1
    elif znak in cisla_sada:         # Poté čísla
        cisel += 1
    else:
        ostatni += 1        # Vše, co zbylo, jsou ostatní znaky (mezery, tečky atd...)

# Zde využijeme původní nezměněnou větu
print(f'Vaše věta: "{zadana_veta}" má:')
print("samohlásek:", samohlasky)
print("souhlásek:", souhlasky)
print("čísel:", cisel)
print("ostatních znaků:", ostatni)

input("\nAplikaci ukončíte stisknutím klávesy Enter...")