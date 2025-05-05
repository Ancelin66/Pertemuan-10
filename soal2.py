def kuis_dari_file(nama_file):
    try:
        with open(nama_file, 'r') as file:
            for line in file:
                if '||' in line:
                    soal, jawaban_benar = line.strip().split('||')
                    soal = soal.strip()
                    jawaban_benar = jawaban_benar.strip().lower()

                    print(soal)
                    jawaban_user = input("Jawab: ").strip().lower()

                    if jawaban_user == jawaban_benar:
                        print("Jawaban benar!\n")
                    else:
                        print("Jawaban salah!\n")
                else:
                    print("Format soal tidak sesuai.\n")
    except FileNotFoundError:
        print("File tidak ditemukan.")

nama_file = input("nama file1: ")
kuis_dari_file(nama_file)
