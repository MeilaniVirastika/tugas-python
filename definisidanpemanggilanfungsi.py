# Fungsi
def salam():
    print('Halo, Selamat Datang!')
# Memanggil Fungsi
salam()

# Fungsi dengan parameter
def salam_nama(nama):
  print(f'Halo, {nama}')
# Memanggil fungsi
salam_nama('Meilani')

# Fungsi dengan multiple parameter
def hitung_penjumlahan(angka1, angka2):
  hasil = angka1 + angka2
  return hasil
# Memanggil fungsi
hasil = hitung_penjumlahan(3,5)
print(f'Hasil penjumlahan: {hasil}')

# Fungsi dengan nilai default
def salam_default(nama='Teman'):
  print(f'Halo, {nama}!')
# Memanggil fungsi
salam_default()
salam_default('Meilani')