def bandingkan_file(file1_path, file2_path):
    try:
        with open(file1_path, 'r') as f1, open(file2_path, 'r') as f2:
            baris1 = f1.readlines()
            baris2 = f2.readlines()

        print(f"Membandingkan '{file1_path}' dengan '{file2_path}':\n")
        jumlah_baris = max(len(baris1), len(baris2))
        perbedaan_ditemukan = False

        for i in range(jumlah_baris):
            isi1 = baris1[i].strip() if i < len(baris1) else '[Tidak ada baris]'
            isi2 = baris2[i].strip() if i < len(baris2) else '[Tidak ada baris]'

            if isi1 != isi2:
                perbedaan_ditemukan = True
                print(f">>> Perbedaan pada baris {i+1}:")
                print(f"    File 1: {isi1}")
                print(f"    File 2: {isi2}\n")

        if not perbedaan_ditemukan:
            print("Tidak ada perbedaan. Kedua file sama persis.")

    except FileNotFoundError as e:
        print(f"File tidak ditemukan: {e}")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

# Ganti dengan nama file yang ingin dibandingkan
file1 = "file1.txt"
file2 = "file2.txt"

bandingkan_file(file1, file2)
