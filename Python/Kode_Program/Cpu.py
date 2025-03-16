from Komponen import Komponen  # Import kelas Komponen

class Cpu(Komponen):
    def __init__(self, jumlah_core=0, kecepatan_ghz=0.0, merk="", nama=""):
        super().__init__(merk, nama)  # Memanggil konstruktor kelas induk
        self.__jumlah_core = jumlah_core
        self.__kecepatan_ghz = kecepatan_ghz

    # Setter
    def set_jumlah_core(self, jumlah_core):
        self.__jumlah_core = jumlah_core

    def set_kecepatan_ghz(self, kecepatan_ghz):
        self.__kecepatan_ghz = kecepatan_ghz

    # Getter
    def get_jumlah_core(self):
        return self.__jumlah_core

    def get_kecepatan_ghz(self):
        return self.__kecepatan_ghz
