def hitung_angka(a,b):
    return a + b
def hitung(a, operasi, b):
    return operasi(a,b)
jumlah = hitung(4, hitung_angka, 5)
print(jumlah)