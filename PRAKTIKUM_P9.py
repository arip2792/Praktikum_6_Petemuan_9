
print("==================== ARIEF ADJI ====================")

def hitung_nilai_akhir(tugas, uts, uas):
    return (tugas * 0.3) + (uts * 0.35) + (uas * 0.35)

data_mahasiswa = []

while True:
    nama = input("Masukkan nama mahasiswa: ")
    nim = input("Masukkan NIM mahasiswa: ")
    tugas = float(input("Masukkan nilai tugas (0-100): "))
    uts = float(input("Masukkan nilai UTS (0-100): "))
    uas = float(input("Masukkan nilai UAS (0-100): "))

    nilai_akhir = hitung_nilai_akhir(tugas, uts, uas)
    data_mahasiswa.append({
        "Nama": nama,
        "NIM": nim,
        "Tugas": tugas,
        "UTS": uts,
        "UAS": uas,
        "Nilai Akhir": nilai_akhir
    })

    tambah_data = input("Apakah ingin menambahkan data lagi? (y/t): ").lower()
    if tambah_data == 't':
        break

print("\nDaftar Data Mahasiswa:")
print("=" * 95)
print(f"{'No':<5} {'Nama':<20} {'NIM':<15} {'Tugas':<10} {'UTS':<10} {'UAS':<10} {'Nilai Akhir':<10}")
print("=" * 95)

for idx, mahasiswa in enumerate(data_mahasiswa, start=1):
    print(f"{idx:<5} {mahasiswa['Nama']:<20} {mahasiswa['NIM']:<15} {mahasiswa['Tugas']:<10.2f} {mahasiswa['UTS']:<10.2f} {mahasiswa['UAS']:<10.2f} {mahasiswa['Nilai Akhir']:<10.2f}")
