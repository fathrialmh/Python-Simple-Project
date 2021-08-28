my_list = []
swapped = True
num = int(input("Jumlah angka yang mau di urutkan: "))

for i in range(num):
    val = int(input("Masukkan Angka: "))
    my_list.append(val)

while swapped:
    swapped = False
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print("\nHasil Urutan:")
print(my_list)
