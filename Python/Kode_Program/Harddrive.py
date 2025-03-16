from Komponen import Komponen  # Import kelas Komponen

class Harddrive(Komponen):
    def __init__(self, kapasitas_gb=0, tipe_drive="", merk="", nama=""):
        super().__init__(merk, nama)  # Memanggil konstruktor kelas induk
        self.__kapasitas_gb = kapasitas_gb
        self.__tipe_drive = tipe_drive

    # Setter
    def set_kapasitas_gb(self, kapasitas_gb):
        self.__kapasitas_gb = kapasitas_gb

    def set_tipe_drive(self, tipe_drive):
        self.__tipe_drive = tipe_drive

    # Getter
    def get_kapasitas_gb(self):
        return self.__kapasitas_gb

    def get_tipe_drive(self):
        return self.__tipe_drive
