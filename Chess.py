print("== Chess in Pyhon by Jophy ==")
print()
for i in range(8):
    print(8-i, end="\t")
    for j in range(8):
        if (i + j) % 2 == 0:
            print("#", end="  ")
        else:
            print(" ", end="  ")
    print()

print(end="\t")

for pismeno in "ABCDEFGH":
    print(pismeno, end="  ")