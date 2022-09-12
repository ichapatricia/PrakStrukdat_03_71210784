from collections import Counter
n = input('Masukkan seluruh kalimat: ')
kecil = Counter((n.lower().split()))
m = input('Masukkan kata yang dicari: ')

print(kecil[m])