class kelas_2023d:
    def __init__(self, nama, kelas, nim, jurusan, fakultas, kampus):
        self.nama = nama
        self.kelas = kelas
        self.nim = nim
        self.jurusan = jurusan
        self.fakultas = fakultas
        self.kampus = kampus

    def print_DataDiri(self):
        print(f"Nama        = {self.nama}")
        print(f"Kelas       = {self.kelas}")
        print(f"NIM         = {self.nim}")
        print(f"Jurusan     = {self.jurusan}")
        print(f"Fakultas    = {self.fakultas}")
        print(f"Kampus      = {self.kampus}")

mhs1 = kelas_2023d("Ditrya", "D", "23091397138", "Manajemen Informatika", "Vokasi", "1")

mhs1.print_DataDiri()
