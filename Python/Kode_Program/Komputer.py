from Cpu import Cpu
from Harddrive import Harddrive
from Ram import Ram


class Komputer:
    def __init__(self, nama="", cpu=None, ram_list=None, harddrive=None):
        self.__nama = nama
        self.__cpu = cpu if cpu else Cpu()  # Default objek kosong jika tidak diberikan
        self.__ram_list = ram_list if ram_list else []  # Default list kosong
        self.__harddrive = harddrive if harddrive else Harddrive()

    # Setter
    def set_nama(self, nama):
        self.__nama = nama

    def set_cpu(self, cpu):
        self.__cpu = cpu

    def set_ram(self, ram_list):
        self.__ram_list = ram_list

    def set_harddrive(self, harddrive):
        self.__harddrive = harddrive

    def add_ram(self, ram):
        self.__ram_list.append(ram)

    # Getter
    def get_nama(self):
        return self.__nama

    def get_cpu(self):
        return self.__cpu

    def get_ram_list(self):
        return self.__ram_list

    def get_harddrive(self):
        return self.__harddrive
