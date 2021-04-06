# input jumlah nilai yang ingin dimasukkan data
n = int(input("Banyak nilai yang ingin dimasukkan : "))
print()
data = []

# pengulangan memasukkan nilai
i = 1
while i <= n:
    nilai = int(input("Masukkan nilai ke-%d : " %i))
    data.append(nilai)
    i = i + 1
print()

# menghitung rata-rata
rata = sum(data)/n
print("Nilai rata-rata : %d" %rata)