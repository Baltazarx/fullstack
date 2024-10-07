def hitung_gaji(golongan, jam_kerja):
    upah_per_jam_dict = {
        'A': 5000,
        'B': 7000,
        'C': 8000,
        'D': 10000
    }
    
    upah_per_jam = upah_per_jam_dict.get(golongan)
    if upah_per_jam is None:
        return "Golongan tidak valid."

    upah = upah_per_jam * jam_kerja
    
    lembur = max(0, (jam_kerja - 48) * 4000)
    
    total_gaji = upah + lembur
    
    return total_gaji

nama_karyawan = input("Masukkan nama karyawan: ")
golongan_karyawan = input("Masukkan golongan karyawan (A/B/C/D): ").upper()
jam_kerja_karyawan = int(input("Masukkan jumlah jam kerja karyawan dalam seminggu: "))

gaji_diterima = hitung_gaji(golongan_karyawan, jam_kerja_karyawan)

print(f"Nama Karyawan: {nama_karyawan}")
print(f"Golongan: {golongan_karyawan}")
print(f"Jumlah Jam Kerja: {jam_kerja_karyawan}")
print(f"{nama_karyawan} menerima upah Rp. {gaji_diterima} per minggu")