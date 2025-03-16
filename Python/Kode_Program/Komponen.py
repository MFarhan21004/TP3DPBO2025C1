class Komponen:
    def __init__(self, merk="", nama=""):
        self.__merk = merk
        self.__nama = nama

    def set_merk(self, merk):
        self.__merk = merk

    def set_nama(self, nama):
        self.__nama = nama

    def get_merk(self):
        return self.__merk

    def get_nama(self):
        return self.__nama
