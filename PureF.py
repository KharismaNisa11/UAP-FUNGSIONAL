angka = [{'number': 1}, {'number': 2}]
def tambah_angka(angka):
    total = 0
    for item in angka:
        total += item['number']
    return total
total = tambah_angka(angka)
print(total)
