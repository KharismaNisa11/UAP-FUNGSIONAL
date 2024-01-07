angka = [{'number': 1}, {'number': 2}]

tambah_angka = lambda angka: sum(item['number'] for item in angka)
