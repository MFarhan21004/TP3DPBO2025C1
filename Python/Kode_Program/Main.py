from Cpu import Cpu
from Ram import Ram
from Harddrive import Harddrive
from Komputer import Komputer

def main():
    # Membuat beberapa objek CPU
    cpu1 = Cpu(8, 3.4, "Intel", "Core i7")
    cpu2 = Cpu(6, 3.0, "AMD", "Ryzen 5")
    cpu3 = Cpu(10, 3.8, "Intel", "Core i9")
    cpu4 = Cpu(12, 3.6, "AMD", "Ryzen 7")

    # Membuat beberapa objek RAM
    ram1 = Ram(16, "DDR5", "Corsair", "Vengeance")
    ram2 = Ram(8, "DDR4", "Kingston", "HyperX")
    ram3 = Ram(32, "DDR5", "G.Skill", "Trident Z")
    ram4 = Ram(16, "DDR4", "Crucial", "Ballistix")
    ram5 = Ram(8, "DDR3", "Samsung", "Green")
    ram6 = Ram(32, "DDR5", "Corsair", "Dominator")
    ram7 = Ram(16, "DDR4", "Adata", "XPG")

    # Membuat beberapa objek Harddrive
    hdd1 = Harddrive(1024, "SSD", "Samsung", "Evo")
    hdd2 = Harddrive(2000, "HDD", "Seagate", "Barracuda")
    hdd3 = Harddrive(512, "SSD", "Western Digital", "Black")
    hdd4 = Harddrive(4000, "HDD", "Toshiba", "X300")

    # Membuat array of object Komputer
    komputer_array = [
        Komputer("PC Abdul", cpu1, [ram1, ram2], hdd1),
        Komputer("PC Budi", cpu2, [ram3], hdd2),
        Komputer("PC Citra", cpu3, [ram4, ram5], hdd3),
        Komputer("PC Dedi", cpu4, [ram6, ram7], hdd4)
    ]

    # Menambahkan RAM tambahan ke masing-masing komputer
    komputer_array[0].add_ram(Ram(16, "DDR5", "Kingston", "FURY"))
    komputer_array[1].add_ram(Ram(8, "DDR4", "Corsair", "Vengeance"))
    komputer_array[2].add_ram(Ram(8, "DDR3", "Kingston", "ValueRAM"))
    komputer_array[3].add_ram(Ram(32, "DDR5", "G.Skill", "Ripjaws"))

    # Menampilkan informasi komputer
    for i, komputer in enumerate(komputer_array, start=1):
        print("======================================")
        print(f"Informasi Komputer {i}:")
        print(f"Nama      : {komputer.get_nama()}")
        print(f"Cpu       : {komputer.get_cpu().get_merk()} {komputer.get_cpu().get_nama()} "
              f"({komputer.get_cpu().get_jumlah_core()} Core) ~{komputer.get_cpu().get_kecepatan_ghz()}GHz")

        for ram in komputer.get_ram_list():
            print(f"Ram       : {ram.get_merk()} {ram.get_nama()} "
                  f"({ram.get_kapasitas_gb()} GB) {ram.get_ddr()}")

        print(f"Harddrive : {komputer.get_harddrive().get_tipe_drive()} {komputer.get_harddrive().get_merk()} "
              f"{komputer.get_harddrive().get_nama()} ({komputer.get_harddrive().get_kapasitas_gb()} GB)")

if __name__ == "__main__":
    main()
