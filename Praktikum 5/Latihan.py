kota = ['Ngawi','Jakarta','Madiun','Bandung','Nganjuk']

print(kota[2])
print(kota[1:4])
print(kota[4])


kota[3] = 'Tulungagung'


kota[3:4] = 'Cilacap','Batam'

kota1 = [kota[0],kota[1]]
print(kota1)

kota1.append('Pekalongan')
print(kota1)

kota1.extend(['Surakarta','Karawang','Cirebon'])
print (kota1)

kota3 = kota1 + kota

print(kota3)